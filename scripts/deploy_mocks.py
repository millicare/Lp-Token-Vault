from brownie import (
    UniswapV2Factory,
    UniswapV2BPT,
    UniswapV2MUST,
    UniswapV2BPTMUSTPair,
    StakingMultiRewards,
    network,
    Contract,
)
from scripts.helpful_scripts import get_account

MUST_INITIAL_BALANCE = 100000
BPT_INITIAL_BALANCE = 500000


def deploy_must(creator):
    print("\nDeploying UniswapV2MUST...")
    # creator gets the tokens
    must = UniswapV2MUST.deploy(MUST_INITIAL_BALANCE, {"from": creator})
    print("UniswapV2MUST deployed.")
    return must


def deploy_bpt(creator):
    print("\nDeploying UniswapV2BPT...")
    bpt = UniswapV2BPT.deploy(BPT_INITIAL_BALANCE, {"from": creator})
    print("UniswapV2BPT deployed.")
    return bpt


"""def deploy_factory(account):
    print("\nDeploying UniswapV2Factory...")
    factory = UniswapV2Factory.deploy({"from": account})
    factory.createPair
    print("Deployed UniswapV2Factory.")"""


def deploy_bptmust_pool(creator, user1, bptContract, mustContract):
    print("\nDeploying UniswapV2BPTMUSTPair...")
    lpToken = UniswapV2BPTMUSTPair.deploy({"from": creator})
    lpToken.initialize(bptContract.address, mustContract.address, {"from": creator})
    print("UniswapV2BPTMUSTPair deployed.")

    print("Funding UniswapV2BPTMUSTPair...")
    mustTransferTx = mustContract.transfer(
        lpToken.address, MUST_INITIAL_BALANCE, {"from": creator}
    )
    bptTransfeerTx = bptContract.transfer(
        lpToken.address, BPT_INITIAL_BALANCE, {"from": creator}
    )
    mustTransferTx.wait(1)
    bptTransfeerTx.wait(1)
    print("LP Contract MUST Balance: ")
    print(mustContract.balanceOf(lpToken.address, {"from": creator}))
    print("LP Contract BPT Balance: ")
    print(bptContract.balanceOf(lpToken.address, {"from": creator}))
    print("UniswapV2BPTMUSTPair funded.")

    print("Minting UniswapV2BPTMUSTPair LP Token to user1...")
    mintTx = lpToken.mint(user1.address, {"from": creator})
    mintTx.wait(1)
    print("UniswapV2BPTMUSTPair LP Token minted.")

    print("Reserves: ")
    print(lpToken.getReserves({"from": creator}))
    print("TotalSupply: ")
    print(lpToken.totalSupply({"from": creator}))

    return lpToken


def deploy_farm(creator, mustToken, bptToken, lpToken):
    print("Deploying farm...")
    farm = StakingMultiRewards.deploy(
        creator.address, [mustToken, bptToken], lpToken.address, {"from": creator}
    )
    print("Farm deployed!")
    return farm


def deploy_mocks(creator, user1):
    # MUST Token
    mustToken = deploy_must(creator)
    # BPT Token
    bptToken = deploy_bpt(creator)
    # BPT/MUST LP Token
    lpToken = deploy_bptmust_pool(creator, user1, bptToken, mustToken)
    # Farm
    deploy_farm(creator, mustToken, bptToken, lpToken)


def main():
    print(f"The active network is {network.show_active()}")
    creator = get_account(index=0)
    user1 = get_account(index=1)
    deploy_mocks(creator, user1)
