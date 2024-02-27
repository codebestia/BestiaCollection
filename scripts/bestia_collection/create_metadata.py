from brownie import network, BestiaCollection
from scripts.helpers import get_art
from pathlib import Path
from metadata.metadata_template import metedata
import requests
import json
import os
"""
Steps
Create Metadata
Upload to ipfs and pinata
set token uri of all minted nfts
"""
art_to_image_uri = {
    'AQUA':"https://ipfs.io/ipfs/Qmd8rXQCE6QyA5xHiHonTSnqBbozPRDGUQVavPkh6Tn3WV?filename=aqua.jpg",
    "BLACK":"https://ipfs.io/ipfs/QmX95uQCexUDPbUP22NKjUV1kPR3eFhEGNUmNXHagysyfA?filename=black.jpg",
    "BLUE":"https://ipfs.io/ipfs/QmT8AAwJbhWaCmdsCw4J3Lv1aNwo65GyjiKcQfQQKB5puZ?filename=blue.jpg",
    "PURPLE":"https://ipfs.io/ipfs/QmW9vdfV5Mz6vjwg47PdvcFh7gF6a3jjaQxj2gpVj7zxcp?filename=purple.jpg"
}

def create_metadata():
    """
    ## Steps in creating metadata
    - get the imported template
    - Loop through all the images
    - create a metadata file for it and save it to metadata folder

    """
    collection = BestiaCollection[-1]
    number_of_collections = collection.tokenCounter()
    print(f"You have created {number_of_collections} collectibles!")
    for token_id in range(number_of_collections):
        art = get_art(collection.tokenIdtoArt(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{art}.json"
        
        collectible_metadata = metedata.copy()
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = art
            collectible_metadata["description"] = f"An Bestia {art} art design"
            image_path = "./img/" + art.lower() +".jpg"

            image_uri = None
            if os.getenv("UPLOAD_TO_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else art_to_image_uri[art]

            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)

def upload_to_ipfs(file_path):
    with Path(file_path).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:8080"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = file_path.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri

def main():
    create_metadata()