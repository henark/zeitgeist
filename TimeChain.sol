// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/AccessControl.sol";

/**
 * @title TimeChain (Nomic Upgrade)
 * @author Jules, AI Engineer
 * @notice This contract is a self-contained implementation of a TimeChain that is also
 * an ERC-20 token ($NOM). It demonstrates the "Nomic" principle, where the system's
 * rules can evolve. The fundamental rule change implemented here is the introduction
 * of a native, transferable token to create an economic engine.
 *
 * @dev This contract includes basic ERC-20 functionality directly to be self-contained.
 * It features a "Proof-of-Time" mining mechanism where Keepers are rewarded with $NOM
 * for extending the on-chain timeline.
 * This version uses OpenZeppelin's AccessControl for role management.
 */
contract TimeChain is AccessControl {

    // =================================================================
    // Roles
    // =================================================================
    bytes32 public constant KEEPER_ROLE = keccak256("KEEPER_ROLE");

    // =================================================================
    // ERC-20 State Variables
    // =================================================================
    string public constant name = "Nomic Time";
    string public constant symbol = "NOM";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // =================================================================
    // TimeChain State Variables
    // =================================================================
    struct Chronon {
        uint256 blockHeight;
        uint256 timestamp;
        bytes32 challenge;
        bytes proof;
    }

    Chronon[] public timechain;
    uint256 public constant CHRONON_INTERVAL = 10; // 10 seconds
    uint256 public constant MINT_REWARD = 10 * 10**18; // Reward 10 NOM per chronon

    // =================================================================
    // Events
    // =================================================================
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event NewChronon(uint256 indexed blockHeight, uint256 timestamp, address indexed submittedBy, uint256 reward);

    // =================================================================
    // Constructor
    // =================================================================
    constructor(address _initialKeeper) {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(KEEPER_ROLE, _initialKeeper);

        // Create the Genesis Chronon (Block 0)
        bytes32 genesisChallenge = keccak256(abi.encodePacked(block.chainid, address(this), "GENESIS"));
        timechain.push(Chronon({
            blockHeight: 0,
            timestamp: block.timestamp,
            challenge: genesisChallenge,
            proof: "GENESIS_PROOF"
        }));
        emit NewChronon(0, block.timestamp, msg.sender, 0);

        // Mint initial supply for the ecosystem/treasury (optional)
        _mint(msg.sender, 1_000_000 * 10**18);
    }

    // =================================================================
    // Core TimeChain Function ("Proof-of-Time Mining")
    // =================================================================
    function submitNewChronon(bytes memory _proof) external {
        require(hasRole(KEEPER_ROLE, msg.sender), "TimeChain: Not an authorized Keeper.");
        Chronon memory latestChronon = timechain[timechain.length - 1];
        require(block.timestamp >= latestChronon.timestamp + CHRONON_INTERVAL, "TimeChain: Interval not yet passed.");
        require(verifyVDF(latestChronon.challenge, _proof), "TimeChain: Invalid VDF proof.");

        // Mint new tokens as a reward for the Keeper
        _mint(msg.sender, MINT_REWARD);

        // Create and store the new Chronon
        uint256 newBlockHeight = timechain.length;
        bytes32 nextChallenge = keccak256(abi.encodePacked(latestChronon.challenge, _proof));
        timechain.push(Chronon({
            blockHeight: newBlockHeight,
            timestamp: block.timestamp,
            challenge: nextChallenge,
            proof: _proof
        }));
        emit NewChronon(newBlockHeight, block.timestamp, msg.sender, MINT_REWARD);
    }

    // =================================================================
    // Role Management Functions
    // =================================================================
    function grantKeeperRole(address _newKeeper) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(_newKeeper != address(0), "TimeChain: Cannot grant role to the zero address.");
        _grantRole(KEEPER_ROLE, _newKeeper);
    }

    function revokeKeeperRole(address _oldKeeper) external onlyRole(DEFAULT_ADMIN_ROLE) {
        _revokeRole(KEEPER_ROLE, _oldKeeper);
    }

    // =================================================================
    // ERC-20 Transfer Functions
    // =================================================================
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "ERC20: transfer amount exceeds balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= balanceOf[_from], "ERC20: transfer amount exceeds balance");
        require(_value <= allowance[_from][msg.sender], "ERC20: transfer amount exceeds allowance");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // =================================================================
    // Internal & View Functions
    // =================================================================
    function _mint(address _to, uint256 _value) internal {
        require(_to != address(0), "ERC20: mint to the zero address");
        totalSupply += _value;
        balanceOf[_to] += _value;
        emit Transfer(address(0), _to, _value);
    }

    function verifyVDF(bytes32 _challenge, bytes memory _proof) internal pure returns (bool) {
        // Placeholder for VDF verification logic.
        return true;
    }

    function getChainLength() external view returns (uint256) {
        return timechain.length;
    }
}
