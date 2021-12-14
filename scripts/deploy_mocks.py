from brownie import (
    UniswapV2Factory,
    UniswapV2BPT,
    UniswapV2MUST,
    UniswapV2BPTMUSTPair,
    StakingMultiRewards,
    network,
)
from scripts.helpful_scripts import get_account


def deploy_must(creator):
    print("\nDeploying UniswapV2MUST...")
    token = UniswapV2MUST.deploy({"from": creator})
    print("UniswapV2MUST deployed.")
    return token


def deploy_bpt(creator):
    print("\nDeploying UniswapV2BPT...")
    token = UniswapV2BPT.deploy({"from": creator})
    print("UniswapV2BPT deployed.")
    return token


"""def deploy_factory(account):
    print("\nDeploying UniswapV2Factory...")
    factory = UniswapV2Factory.deploy({"from": account})
    factory.createPair
    print("Deployed UniswapV2Factory.")"""


def deploy_bptmust_pool(creator, bptAddr, mustAddr):
    print("\nDeploying UniswapV2BPTMUSTPair...")
    lpToken = UniswapV2BPTMUSTPair.deploy({"from": creator})
    lpToken.initialize(bptAddr, mustAddr, {"from": creator})
    lpToken.sync({"from": creator})
    print("UniswapV2BPTMUSTPair deployed.")
    return lpToken


def deploy_farm(creator, mustToken, bptToken, lpToken):
    print("Deploying farm...")
    farm = StakingMultiRewards.deploy(
        creator.address, [mustToken, bptToken], lpToken.address, {"from": creator}
    )
    print("Farm deployed!")
    return farm


def deploy_mocks(creator):
    # MUST Token
    mustToken = deploy_must(creator)
    # BPT Token
    bptToken = deploy_bpt(creator)
    # BPT/MUST LP Token
    lpToken = deploy_bptmust_pool(creator, bptToken.address, mustToken.address)
    # Farm
    deploy_farm(creator, mustToken, bptToken, lpToken)


def main():
    print(f"The active network is {network.show_active()}")
    creator = get_account(index=0)
    deploy_mocks(creator)
