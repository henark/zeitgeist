// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title TimeChain
 * @author Jules, AI Engineer
 * @notice This contract is a prototype implementation of the TimeChain concept,
 * designed to run on the Ethereum Virtual Machine (EVM). It creates a
 * verifiable, on-chain timeline by linking discrete "Chronon" blocks.
 *
 * @dev This implementation requires a hybrid on-chain/off-chain architecture.
 * The time-consuming VDF computation is performed by off-chain "Keeper" nodes.
 * These Keepers then submit the VDF proof to this contract for verification
 * and the minting of a new Chronon.
 */
contract TimeChain {

    // =================================================================
    //  STATE VARIABLES
    // =================================================================

    // The core data structure for a single unit of time.
    struct Chronon {
        uint256 blockHeight;    // The height of the TimeChain.
        uint256 timestamp;      // The real-world timestamp when the Chronon was minted.
        bytes32 challenge;      // The challenge used to generate the VDF proof for the *next* Chronon.
        bytes proof;            // The VDF proof submitted for *this* Chronon.
    }

    // The immutable, append-only timeline. The array index is the blockHeight.
    Chronon[] public timechain;

    // The address authorized to submit new Chronons.
    // In a production system, this could be a permissionless role or a DAO-controlled multisig.
    address public keeper;

    // The target time interval (in seconds) for each Chronon block.
    // This defines the "tick" rate of the TimeChain.
    uint256 public constant CHRONON_INTERVAL = 10; // e.g., 10 seconds

    // =================================================================
    //  EVENTS
    // =================================================================

    event NewChronon(uint256 indexed blockHeight, uint256 timestamp, address indexed submittedBy);
    event KeeperUpdated(address indexed newKeeper);

    // =================================================================
    //  CONSTRUCTOR
    // =================================================================

    constructor(address _initialKeeper) {
        keeper = _initialKeeper;

        // Create the Genesis Chronon (Block 0)
        // The challenge for the next block is derived from a predictable source,
        // like the hash of the genesis block details.
        bytes32 genesisChallenge = keccak256(abi.encodePacked(block.chainid, address(this), "GENESIS"));
        timechain.push(Chronon({
            blockHeight: 0,
            timestamp: block.timestamp,
            challenge: genesisChallenge,
            proof: "GENESIS_PROOF"
        }));

        emit NewChronon(0, block.timestamp, msg.sender);
    }

    // =================================================================
    //  KEEPER-ONLY FUNCTIONS (The "Heartbeat" of the Chain)
    // =================================================================

    /**
     * @notice The core function for extending the timeline.
     * @dev Called by an off-chain Keeper after it has computed the VDF.
     * The Keeper must compute VDF(challenge, CHRONON_INTERVAL) and submit the result.
     * @param _proof The VDF proof from the off-chain computation.
     */
    function submitNewChronon(bytes memory _proof) external {
        require(msg.sender == keeper, "TimeChain: Not the authorized Keeper.");

        Chronon memory latestChronon = timechain[timechain.length - 1];

        // 1. Verify that enough real time has passed since the last block.
        require(block.timestamp >= latestChronon.timestamp + CHRONON_INTERVAL, "TimeChain: Interval not yet passed.");

        // 2. Verify the submitted VDF proof.
        //    --> This is a placeholder for actual VDF verification logic.
        //    --> A real implementation would require a precompiled contract or complex assembly.
        require(verifyVDF(latestChronon.challenge, _proof), "TimeChain: Invalid VDF proof.");

        // 3. All checks passed. Mint the new Chronon.
        uint256 newBlockHeight = timechain.length;
        bytes32 nextChallenge = keccak256(abi.encodePacked(latestChronon.challenge, _proof));

        timechain.push(Chronon({
            blockHeight: newBlockHeight,
            timestamp: block.timestamp,
            challenge: nextChallenge,
            proof: _proof
        }));

        emit NewChronon(newBlockHeight, block.timestamp, msg.sender);
    }

    // =================================================================
    //  VDF VERIFICATION (Placeholder)
    // =================================================================

    /**
     * @dev Placeholder for VDF proof verification. In a real system, this would be
     * a call to a highly optimized cryptographic library or a precompiled contract.
     * For this prototype, it simply returns true.
     */
    function verifyVDF(bytes32 _challenge, bytes memory _proof) internal pure returns (bool) {
        // To avoid compilation warnings about unused parameters.
        // In a real implementation, these would be used.
        bytes32 challenge = _challenge;
        bytes memory proof = _proof;
        challenge;
        proof;

        // Placeholder: a real verification function would go here.
        return true;
    }

    // =================================================================
    //  ADMIN & VIEW FUNCTIONS
    // =================================================================

    /**
     * @notice Allows the owner to update the authorized Keeper address.
     */
    function setKeeper(address _newKeeper) external {
        // In a real system, this would be controlled by `onlyOwner` or a DAO vote.
        // For simplicity, leaving it open in this prototype.
        require(_newKeeper != address(0), "TimeChain: Cannot set keeper to zero address.");
        keeper = _newKeeper;
        emit KeeperUpdated(_newKeeper);
    }

    /**
     * @notice Returns the total number of Chronons in the timeline.
     */
    function getChainLength() external view returns (uint256) {
        return timechain.length;
    }

    /**
     * @notice Returns the most recently minted Chronon.
     */
    function getLatestChronon() external view returns (Chronon memory) {
        return timechain[timechain.length - 1];
    }
}
