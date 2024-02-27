from brownie import network, JoshCollection
from scripts.helpers import get_account, OPENSEA_URL, LOCAL_DEVELOPMENT
token_uri = "https://ipfs.io/ipfs/QmaPUn5dnSr9aFdiztQK9vdneCrqL49voKkHSEYmET6vSN?filename=test_ipfs_file.json"
secondary_token_uri = "https://ipfs.io/ipns/k51qzi5uqu5dlan8sgi7m648dj9ahqwtx92nxnuzhvqlxadj564znytcefm5qc"

def deploy_create():
    account = get_account()
    if len(JoshCollection) < 1:
        collection = JoshCollection.deploy({'from':account})
    else:
        collection = JoshCollection[-1]
    tx = collection.createCollectible(secondary_token_uri,{'from':account})
    tx.wait(1)
    print("Collection Created")
    print("COllection Available at ",OPENSEA_URL.format(network.show_active(),collection.address, collection.tokenCounter() - 1))
    return collection

def main():
    deploy_create()