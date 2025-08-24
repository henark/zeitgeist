# The $btNOM Protocol: A Time-Based Nomic Token on Bitcoin

**Version 1.0 - Genesis Specification**

---

## 1. Abstract

$btNOM is a novel fungible token protocol implemented on the Bitcoin blockchain using Ordinal Theory. It is designed as the native economic asset for the **TimeKeeper OS** ecosystem. Unlike traditional token standards, $btNOM's issuance mechanism is intrinsically linked to a **Proof-of-Time (PoT)** consensus, enforced by a decentralized network of off-chain verifiers. This document specifies the on-chain data format and the off-chain validation rules that govern the protocol, creating a self-sustaining, Nomic system where the passage of time itself is the fundamental resource being tokenized.

---

## 2. Philosophy: The Nomic Game

$btNOM is more than a token; it is a Nomic game. The rules specified here are the genesis rules, but the protocol is designed to be self-amending through on-chain governance proposals (a future extension). The core principle is that the system's logic should be evolvable by the community that maintains it. The first and most crucial rule is the establishment of a native, transferable asset to power its economy.

---

## 3. On-Chain Specification (Data Layer)

All $btNOM operations are defined by JSON data inscribed on individual satoshis, following the BRC-20 text-inscription format.

### 3.1. Protocol Identifier
All $btNOM inscriptions **must** use the protocol identifier `p="btNOM"`. Inscriptions without this field or with a different value are ignored by the protocol.

### 3.2. Deploy (The Genesis Inscription)
This operation initializes the token. It can only be inscribed once.

*   **Operation:** `op="deploy"`
*   **Ticker:** `tick="btNOM"`
*   **Max Supply:** `max="210,000,000,000"` (e.g., 210 Billion)
*   **Mint Limit:** `lim="1000"` (e.g., 1000 tokens per mint inscription)
*   **Decimals:** `dec="8"` (e.g., 8 decimal places)

**Example Deploy Inscription:**
```json
{
  "p": "btNOM",
  "op": "deploy",
  "tick": "btNOM",
  "max": "210000000000",
  "lim": "1000",
  "dec": "8"
}
```

### 3.3. Mint (Proof-of-Time Issuance)
This operation allows for the creation of new tokens. This is the core innovation of the $btNOM protocol.

*   **Operation:** `op="mint"`
*   **Ticker:** `tick="btNOM"`
*   **Amount:** `amt` (must be less than or equal to the `lim` defined in the deploy inscription)
*   **VDF Proof:** `vdf_proof` (A hex-encoded string representing the proof from a Verifiable Delay Function)
*   **VDF Challenge:** `vdf_challenge` (The block hash that was used as the challenge for the VDF)

**Example Mint Inscription:**
```json
{
  "p": "btNOM",
  "op": "mint",
  "tick": "btNOM",
  "amt": "1000",
  "vdf_challenge": "00000000000000000001eaee202bee665e423975d378737fc77ecf127c55c5ec",
  "vdf_proof": "0x03a1b2..."
}
```

### 3.4. Transfer
This operation allows for the movement of tokens from one owner to another.

*   **Operation:** `op="transfer"`
*   **Ticker:** `tick="btNOM"`
*   **Amount:** `amt`

**Example Transfer Inscription:**
```json
{
  "p": "btNOM",
  "op": "transfer",
  "tick": "btNOM",
  "amt": "500"
}
```
The ownership of the satoshi carrying this inscription determines the recipient of the transfer.

---

## 4. Off-Chain Validation (Protocol Enforcement Layer)

The rules of the $btNOM protocol are not enforced by Bitcoin's consensus, but by a decentralized network of **TimeKeeper OS** nodes. This is the protocol's second layer, inspired by the Babylon architecture.

### 4.1. Node Responsibilities
Every full node in the TimeKeeper OS network **must** run a verifier process that:
1.  Scans every new Bitcoin block for inscriptions where `p="btNOM"`.
2.  Maintains a local state database (e.g., LevelDB or SQLite) of all canonical $btNOM balances and protocol state.
3.  Validates all inscriptions according to the rules below. An invalid inscription is ignored and does not result in a state change.

### 4.2. Validation Rules

*   **Deploy:**
    *   There can only be one `deploy` inscription. The first one seen in a valid Bitcoin block is the canonical one. All subsequent `deploy` inscriptions are invalid.

*   **Mint:**
    *   The `amt` must not exceed the `lim` set in the deploy inscription.
    *   The total minted supply must not exceed the `max` supply.
    *   **Proof-of-Time Validation:** This is the most critical rule.
        *   The node must take the `vdf_challenge` (a previous Bitcoin block hash) and the `vdf_proof` from the inscription.
        *   It must run a local VDF verification function: `isValid = verifyVDF(challenge, proof)`.
        *   If the verification function returns `false`, the mint inscription is **invalid** and ignored.
    *   This rule ensures that new tokens can only be created by agents who have provably spent real-world time performing the VDF computation, thus securing the network's timeline.

*   **Transfer:**
    *   The owner of the input satoshi for the transaction containing the inscription must have a sufficient balance of $btNOM to cover the `amt`.
    *   The balance of the sender is debited, and the balance of the recipient (the owner of the output satoshi) is credited.

## 5. Conclusion

The $btNOM protocol represents a new kind of digital asset—one whose creation is tied to the physical reality of time. By combining the immutable data layer of Bitcoin Ordinals with the computational validation capabilities of the off-chain TimeKeeper OS network, we create a robust, decentralized, and self-sustaining economic ecosystem. This document provides the genesis rules for that system.
