import requests
import csv

def load_addresses_list(path) -> list:
    """
    Read in csv of address keys
    Output a list, ready for querying API of explorer
    """
    all_addresses = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            all_addresses.append(row[0])
    return all_addresses

def get_permission_tree(account_list):
    """
    Input a list of address keys
    Queries API for permission tree of validator
    Returns a dictionary for that address list 
    """
    web_address = "https://0l.interblockcha.in:444/permission-tree/validator/"
    genesis_dict = {}
    for account in account_list:
        # print(web_address+account)
        response = requests.get(web_address+account)
        genesis_dict[str(account)] = response.json()
        # print(response.json())

    return genesis_dict

def get_epoch():
    """
    get current epoch
    """
    web_address = "https://0l.interblockcha.in:444/epochs"

    response = requests.get(web_address)
    epochs = response.json()

    return epochs