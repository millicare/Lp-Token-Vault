# ComethVault

This repository contains the ComethVault smartcontract.

## Workflow

1. User deposit LP token in the Vault (first, user has to approve LP token to the Vault)
2. The Vault deposits the LP token in the Farm
3. Chainlink Keepers calls the Vault to compound interests periodically
4. User can withdraw LP token from the Vault

## Links

[ComethSwap](https://swap.cometh.io/)

## Notes

This is a project in development, mainly used to get familiar with solidity and defi smartcontracts.

Thanks to @PatrickAlphaC for [this course](https://github.com/smartcontractkit/full-blockchain-solidity-course-py).

# Tools

## Install brownie

`pip install brownie`

## Install ganache

`npm install -g ganache-cli`

# Local deployment

Use brownie to run the deploy script

`brownie run scripts/deploy --network=ganache-cli`

Explore other scripts


# Live deployment

## Setup your environment variables

Create a ".env" file in the root directory

`touch .env`

Add your private key to deploy on a live testnet

`export PRIVATE_KEY=0xyourprivatekey`

Add your Etherscan token to publish your code

`export ETHERSCAN_TOKEN=yourtoken`
