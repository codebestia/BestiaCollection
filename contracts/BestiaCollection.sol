// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract BestiaCollection is ERC721, VRFConsumerBase {
    uint256 public tokenCounter; //Token Counter
    bytes32 public keyhash;
    uint256 public fee;
    enum Art{AQUA, BLACK, BLUE, PURPLE}
    mapping(uint256 => Art) public tokenIdtoArt;
    mapping(bytes32 => address) public requestIdToSender;
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event artAssigned(uint256 indexed tokenId, Art art);

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee) public 
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("BestiaArt", "BAR")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns (bytes32){
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
        return requestId;
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        Art art = Art(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tokenIdtoArt[newTokenId] = art;
        emit artAssigned(newTokenId, art);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // aqua, black, blue, purple
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner or not approved");
        _setTokenURI(tokenId, _tokenURI);
    }
}