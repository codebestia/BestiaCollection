# Bestia Collection

This is an NFT collection smart contract program. This program contains two different nft programs. one for simple nft minting with little logic and one for advanced nft minting with more logics.

## Prerequisites
Please install or have installed the below program:

- [Python and pip](https://nodejs.org/en/download/)
- [nodejs and npm](https://nodejs.org/en/download/)

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```
Or, if that doesn't work, via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
2. Clone this repo
```
# open your terminal
git clone https://github.com/codebestia/BestiaCollection.git
cd BestiaCollection
```

3. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```
If you want to be able to deploy to testnets, do the following. 

4. Set your environment variables

Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). 

You can get a `WEB3_INFURA_PROJECT_ID` by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura with brownie. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/). 


You'll also want an [Etherscan API Key](https://etherscan.io/apis) to verify your smart contracts. 

Create a .env file in the contract directory and add your environment variables to the `.env` file:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
export ETHERSCAN_TOKEN=<YOUR_TOKEN>
```
> DO NOT SEND YOUR KEYS TO GITHUB
> If you do that, people can steal all your funds. Ideally use an account with no real money in it. 


Then, make sure your `brownie-config.yaml` has:

```
dotenv: .env
```



## Usage/Examples

1. Compile the NFT Collection token contract
```
brownie compile
```
2. Deploy the bestiacollection contract
For Ganache local chain
```
brownie run scripts/bestia_collection/deploy.py 
```
For testnet deployment
```
brownie run scripts/bestia_collection/deploy.py  --network sepolia
```

OR

3. Deploy the joshcollection contract
For Ganache local chain
```
brownie run scripts/josh_collection/deploy.py  
```
For testnet deployment
```
brownie run scripts/bestia_collection/deploy.py  --network sepolia

View and Interact with the nft contract

you can also view it on Opensea testnet. Information in Josh Collection Code


