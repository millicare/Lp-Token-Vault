from brownie import StakingMultiRewards, ComethVault, UniswapV2BPTMUSTPair
from scripts.helpful_scripts import get_account


def deposit(creator, user1):
    print("Fund account")
    lpToken = UniswapV2BPTMUSTPair[-1]
    farm = StakingMultiRewards[-1]
    vault = ComethVault[-1]

    amount = 200  # 1 ?
    # user1 allow vault to spend lpToken
    approveTx = lpToken.approve(vault.address, amount, {"from": user1})
    approveTx.wait(1)
    # current allowance
    print(lpToken.allowance(user1.address, vault.address, {"from": creator}))
    # user1 deposit token in vault
    depositTx = vault.deposit(amount, {"from": user1})

    depositTx.wait(1)
    # check deposit
    depositedAmount = vault.getDeposit({"from": user1})
    print(f"Deposited {depositedAmount} LP tokens")


def main():
    creator = get_account(index=0)
    user1 = get_account(index=1)
    deposit(creator, user1)
