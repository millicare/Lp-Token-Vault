from brownie import (
    ComethVault,
    network,
    config,
)
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    retrieve_live_contracts,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)
from scripts.deploy_mocks import deploy_mocks


def deploy_cometh_vault(creator, user1):
    activenetwork = network.show_active()
    if (
        activenetwork not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        and activenetwork in FORKED_LOCAL_ENVIRONMENTS
    ):
        print("Retrieving live contracts")
        retrieve_live_contracts()
    else:
        print("Deploying mocks")
        deploy_mocks(creator, user1)

    lpTokenAddr = get_contract("bptmustpool").address
    farmAddr = get_contract("bptmustfarm").address

    print(f"Deploy ComethVault [farm={farmAddr}, lpToken={lpTokenAddr}]")
    cometh_vault = ComethVault.deploy(
        farmAddr,
        lpTokenAddr,
        user1.address,
        {"from": creator},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {cometh_vault.address}")
    return cometh_vault


def main():
    print(f"The active network is {network.show_active()}")
    creator = get_account(index=0)
    user1 = get_account(index=1)
    deploy_cometh_vault(creator, user1)
