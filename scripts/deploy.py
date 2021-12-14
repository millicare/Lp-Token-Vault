from brownie import (
    ComethVault,
    StakingMultiRewards,
    UniswapV2BPTMUSTPair,
    network,
    config,
)
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.deploy_mocks import deploy_mocks

"""
ComethVault constructor
  address _farm,
  address _lpToken,
  address _user
"""


def deploy_cometh_vault(creator, user):
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        """price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]"""
        print("Environment not configured for live network")
    else:
        deploy_mocks(creator)
        lpTokenAddr = UniswapV2BPTMUSTPair[-1].address
        farmAddr = StakingMultiRewards[-1].address

    print(f"Deploy ComethVault [farm={farmAddr}, lpToken={lpTokenAddr}]")
    cometh_vault = ComethVault.deploy(
        farmAddr,
        lpTokenAddr,
        user.address,
        {"from": creator},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {cometh_vault.address}")
    return cometh_vault


def main():
    print(f"The active network is {network.show_active()}")
    creator = get_account(index=0)
    user = get_account(index=1)
    deploy_cometh_vault(creator, user)
