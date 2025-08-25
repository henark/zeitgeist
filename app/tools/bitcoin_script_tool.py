from __future__ import annotations
from typing import Any, Tuple, Optional
from .registry import Tool

# secp256k1 parameters
P_VAL = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N_VAL = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
# Generator point
G_POINT = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
Point = Tuple[int, int]

class BitcoinScriptTool(Tool):
    """
    A tool for simulating and interacting with Bitcoin scripts,
    including support for the proposed EC-OPS BIP.
    """
    name = "bitcoin_script"

    def __init__(self):
        super().__init__()
        self.actions = {
            "simulate": self.simulate_script,
        }

    # --- Core Elliptic Curve Operations ---

    def _is_infinite(self, P: Optional[Point]) -> bool:
        return P is None

    def _point_add(self, P1: Optional[Point], P2: Optional[Point]) -> Optional[Point]:
        if self._is_infinite(P1): return P2
        if self._is_infinite(P2): return P1

        if P1[0] == P2[0]:
            if P1[1] != P2[1]: return None
            lam = (3 * P1[0] * P1[0] * pow(2 * P1[1], P_VAL - 2, P_VAL)) % P_VAL
        else:
            lam = ((P2[1] - P1[1]) * pow(P2[0] - P1[0], P_VAL - 2, P_VAL)) % P_VAL

        x3 = (lam * lam - P1[0] - P2[0]) % P_VAL
        y3 = (lam * (P1[0] - x3) - P1[1]) % P_VAL
        return (x3, y3)

    def _point_mul(self, P: Optional[Point], k: int) -> Optional[Point]:
        if k == 0 or self._is_infinite(P): return None
        R = None
        for i in range(256):
            if (k >> i) & 1:
                R = self._point_add(R, P)
            P = self._point_add(P, P)
        return R

    def _point_negate(self, P: Optional[Point]) -> Optional[Point]:
        if self._is_infinite(P): return None
        return (P[0], (P_VAL - P[1]) % P_VAL)

    # --- Encoding/Decoding Functions ---

    def _decode_point(self, data: bytes) -> Optional[Point]:
        if len(data) != 33: raise ValueError(f"Invalid compressed point length: {len(data)}")
        prefix = data[0]
        if prefix not in [0x02, 0x03]: raise ValueError(f"Invalid compression prefix: {prefix:02x}")
        x = int.from_bytes(data[1:33], byteorder='big')
        if x >= P_VAL: raise ValueError("X coordinate >= field prime")

        y_sq = (pow(x, 3, P_VAL) + 7) % P_VAL
        y = pow(y_sq, (P_VAL + 1) // 4, P_VAL)
        if pow(y, 2, P_VAL) != y_sq: raise ValueError("Invalid point: not on curve")

        if (y & 1) != (prefix & 1): y = P_VAL - y
        return (x, y)

    def _encode_point(self, P: Point) -> bytes:
        prefix = 0x03 if P[1] & 1 else 0x02
        return bytes([prefix]) + P[0].to_bytes(32, byteorder='big')

    def _get_x_coord(self, P: Point) -> bytes:
        return P[0].to_bytes(32, byteorder='big')

    # --- Op-Code Logic ---

    def _op_ec_point_add(self, stack: list[bytes]):
        if len(stack) < 2: raise ValueError("OP_EC_POINT_ADD requires 2 stack elements")
        P2 = self._decode_point(stack.pop())
        P1 = self._decode_point(stack.pop())
        result = self._point_add(P1, P2)
        stack.append(b'' if self._is_infinite(result) else self._encode_point(result))

    def _op_ec_point_mul(self, stack: list[bytes]):
        if len(stack) < 2: raise ValueError("OP_EC_POINT_MUL requires 2 stack elements")
        scalar_bytes = stack.pop()
        point_bytes = stack.pop()

        if len(scalar_bytes) != 32: raise ValueError(f"Invalid scalar length: {len(scalar_bytes)}")
        scalar = int.from_bytes(scalar_bytes, byteorder='big') % N_VAL

        point = G_POINT if len(point_bytes) == 0 else self._decode_point(point_bytes)

        result = self._point_mul(point, scalar)
        stack.append(b'' if self._is_infinite(result) else self._encode_point(result))

    def _op_ec_point_negate(self, stack: list[bytes]):
        if len(stack) < 1: raise ValueError("OP_EC_POINT_NEGATE requires 1 stack element")
        point_bytes = stack.pop()
        if len(point_bytes) == 0:
            stack.append(b'')
            return
        point = self._decode_point(point_bytes)
        result = self._point_negate(point)
        stack.append(b'' if self._is_infinite(result) else self._encode_point(result))

    def _op_ec_point_x_coord(self, stack: list[bytes]):
        if len(stack) < 1: raise ValueError("OP_EC_POINT_X_COORD requires 1 stack element")
        point_bytes = stack.pop()
        if len(point_bytes) == 0: raise ValueError("Cannot extract x-coordinate from point at infinity")
        point = self._decode_point(point_bytes)
        stack.append(self._get_x_coord(point))

    # --- Public Tool Action ---

    def simulate_script(self, script: list[str], initial_stack: list[str] | None = None) -> dict[str, Any]:
        """
        Simulates the execution of a Bitcoin script.
        - script: A list of op-codes or hex-encoded data to push.
        - initial_stack: An optional list of hex-encoded data to pre-load onto the stack.
        """
        stack = [bytes.fromhex(item) for item in (initial_stack or [])]

        op_map = {
            "OP_EC_POINT_ADD": self._op_ec_point_add,
            "OP_EC_POINT_MUL": self._op_ec_point_mul,
            "OP_EC_POINT_NEGATE": self._op_ec_point_negate,
            "OP_EC_POINT_X_COORD": self._op_ec_point_x_coord,
        }

        try:
            for op in script:
                if op in op_map:
                    op_map[op](stack)
                else:
                    # Assume it's hex data to be pushed onto the stack
                    stack.append(bytes.fromhex(op))

            final_stack_hex = [item.hex() for item in stack]
            return {"final_stack": final_stack_hex}

        except (ValueError, IndexError) as e:
            raise ValueError(f"Script execution error: {e}") from e
