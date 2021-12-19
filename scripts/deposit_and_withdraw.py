from brownie import StakingMultiRewards, ComethVault, UniswapV2BPTMUSTPair
from scripts.helpful_scripts import get_account


def deposit(creator, user1):
    print("Deposit in vault")
    lpToken = UniswapV2BPTMUSTPair[-1]
    vault = ComethVault[-1]

    amount = 1000
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


def withdraw(creator, user1):
    print("Withdraw 10 per cent of the deposit amount from the Vault")
    vault = ComethVault[-1]
    lpToken = UniswapV2BPTMUSTPair[-1]
    farm = StakingMultiRewards[-1]

    vaultBalance = lpToken.balanceOf(vault.address, {"from": creator})
    print(f"Vault balance: {vaultBalance}")
    # current deposit
    depositedAmount = vault.getDeposit({"from": user1})
    print(f"Deposited amount: {depositedAmount}")
    # withdraw a portion of the LPTokens because user1 is the unique liquidity provider so cant withdraw all
    withDrawTx = vault.withdraw(depositedAmount / 10, {"from": user1})
    withDrawTx.wait(1)

    depositedAmount = vault.getDeposit({"from": user1})
    print(f"New deposited amount: {depositedAmount}")

    vaultBalance = lpToken.balanceOf(vault.address, {"from": creator})
    print(f"Vault balance: {vaultBalance}")

    vaultAllowance = lpToken.allowance(vault.address, user1.address, {"from": creator})
    print(f"Vault allowance: {vaultAllowance}")


def exit(creator, user1):
    print("Exit from vault")
    vault = ComethVault[-1]
    exitTx = vault.exit({"from": user1})
    exitTx.wait(1)


def main():
    creator = get_account(index=0)
    user1 = get_account(index=1)
    deposit(creator, user1)
    withdraw(creator, user1)  # exit
