from brownie import StakingMultiRewards, ComethVault, UniswapV2BPTMUSTPair
from scripts.helpful_scripts import get_account


def deposit(creator, user):
    print("Fund account")
    lpToken = UniswapV2BPTMUSTPair[-1]
    farm = StakingMultiRewards[-1]
    vault = ComethVault[-1]
    amount = 1  # 1 ?
    # allow vault to spend lpToken
    lpToken.approve(vault.address, amount, {"from": creator})
    # user deposit token in vault
    vault.deposit(amount, {"from": user})
    # check deposit
    depositedAmount = vault.getDeposit({"from": user})
    print(f"Deposited {depositedAmount} LP tokens")


def main():
    creator = get_account(index=0)
    user = get_account(index=1)
    deposit(creator, user)
