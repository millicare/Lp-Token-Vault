pragma solidity ^0.5.16;

// Inheritancea
interface IStakingMultiRewards {
    // Views
    function lastTimeRewardApplicable() external view returns (uint256);

    function rewardsPerToken() external view returns (uint256[] memory);

    function earned(address account) external view returns (uint256[] memory);

    function getRewardsForDuration() external view returns (uint256[] memory);

    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);

    // Mutative

    function stake(uint256 amount) external;

    function withdraw(uint256 amount) external;

    function getReward() external;

    function exit() external;
}
