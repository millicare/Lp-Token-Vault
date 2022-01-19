from scripts.helpful_scripts import get_account, get_contract
from brownie import accounts, config
from web3 import Web3

# 0.1
AMOUNT = Web3.toWei(0.1, "ether")


def check(user):
    check_balance(user)
    check_earnings(user)


def check_balance(user):
    bptmustfarm = get_contract("bptmustfarm")
    bptmustpool = get_contract("bptmustpool")
    lpTokenInFarm = bptmustfarm.balanceOf(user, {"from": user}) / pow(
        10, bptmustpool.decimals({"from": user})
    )
    print("LP token in farm: " + str(lpTokenInFarm))


def check_earnings(user):
    bptmustfarm = get_contract("bptmustfarm")
    rewardsTokens = bptmustfarm.getRewardsTokens({"from": user})
    rewards = bptmustfarm.earned(user, {"from": user})
    i = 0
    for token in rewardsTokens:
        reward = rewards[i] / pow(10, 18)
        print(str(reward) + " of " + token + " to claim")
        i = i + 1


def add_ledger_public_address():
    accounts.at(config["wallets"]["ledger_public_key"], force=True)


def main():
    add_ledger_public_address()
    check(accounts.at(config["wallets"]["ledger_public_key"]))
