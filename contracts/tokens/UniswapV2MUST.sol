pragma solidity =0.5.16;

import "@Uniswap/contracts/UniswapV2ERC20.sol";
import "@Uniswap/contracts/libraries/SafeMath.sol";

contract UniswapV2MUST is UniswapV2ERC20 {
    constructor(uint256 _totalSupply) public {
        _mint(msg.sender, _totalSupply);
    }
}
