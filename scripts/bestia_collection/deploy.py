from brownie import BestiaCollection,network, config
from scripts.helpers import get_account,get_contract, fund_with_link
from metadata.metadata_template import metedata
"""
Steps:
deploy mocks
deploy contract 
fund contract with link
create metadata

"""

def deploy_create():
    """
    Deploying the NFT collection and creating a collectible.
    """
    account = get_account()
    if len(BestiaCollection) < 3: # Create whether a contract has not already been deployed
        link_token_contract = get_contract('link_token')
        vrf_coordinator_contract = get_contract("vrf_coordinator")
        keyhash = config['networks'][network.show_active()]['keyhash']
        fee = config['networks'][network.show_active()]['fee']
        print("Deploying Collection Contract")
        collection = BestiaCollection.deploy(
            vrf_coordinator_contract,
            link_token_contract,
            keyhash,
            fee,
            {'from':account}
        )
        print("Funding Collection Contract with Link")
        fund_with_link(collection.address,account,link_token_contract)
    else:
        collection = BestiaCollection[-1]
    
    tx = collection.createCollectible({'from':account})
    tx.wait(1)
    print("New Collectible Created")
    return collection, tx

    

def main():
    deploy_create()