from brownie import (
    ComethVault,
    UniswapV2BPT,
    UniswapV2MUST,
    UniswapV2BPTMUSTPair,
    StakingMultiRewards,
    network,
    Contract,
    config,
    accounts,
)

from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev", "polygon-main-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def privatekey_fromseed(private_key_seed_ascii):
    print(private_key_seed_ascii)
    priv_key = Web3.sha3(text=private_key_seed_ascii)
    print(priv_key.hex())


def retrieve_live_contracts():
    if network.show_active() == "polygon-main-fork":
        for contractalias in config["networks"][network.show_active()]["addresses"]:
            addr = config["networks"][network.show_active()]["addresses"][contractalias]
            print("Getting " + contractalias + " contract at " + addr + "...")
            contract = Contract.from_explorer(addr)
            contract.set_alias(contractalias)
        # account = get_account()
        # print(Contract("bptmustfarm").totalSupply({"from": account}))
    else:
        print("bad network")


def get_contract(alias):
    try:
        return Contract(alias)
    except:
        if alias == "must":
            return UniswapV2MUST[-1]
        elif alias == "bpt":
            return UniswapV2BPT[-1]
        elif alias == "bptmustpool":
            return UniswapV2BPTMUSTPair[-1]
        elif alias == "bptmustfarm":
            return StakingMultiRewards[-1]
        elif alias == "vault":
            return ComethVault[-1]
        else:
            return None
