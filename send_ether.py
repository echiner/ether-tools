import sys
import configparser
import argparse
from web3 import Web3, HTTPProvider

def send_ether_to_addresses(filename, amount_ether, config_file):
    # Read the configuration from the config.ini file
    config = configparser.ConfigParser()
    config.read(config_file)
    sender_private_key = config.get('ethereum', 'private_key')
    provider_url = config.get('ethereum', 'provider_url')

    # Connect to Ethereum node
    w3 = Web3(HTTPProvider(provider_url))

    # Check if connected
    if not w3.is_connected():
        print("Error: Not connected to the Ethereum network.")
        sys.exit(1)

    # Get the sender's public address
    sender_address = w3.eth.account.from_key(sender_private_key).address
    print("---------------------------------------------------")
    print("Sender address: " + sender_address)
    print("Amount to be sent: " + str(amount_ether))
    print("---------------------------------------------------")

    # Read the list of addresses from the file
    with open(filename, 'r') as f:
        addresses = f.readlines()
    addresses = [address.strip() for address in addresses]

    # Convert the Ether amount to Wei
    amount_wei = w3.to_wei(amount_ether, 'ether')

    # Convert list to set to REMOVE DUPLICATES, then convert back to list
    addresses = list(set(addresses))

    # Ask for confirmation
    print(f"About to send {amount_ether} Ether to the following {len(addresses)} addresses:")
    for address in addresses:
        print(" - " + address)

    confirmation = input("\nAre you sure you want to proceed? (yes/no): ").lower()
    if confirmation != 'yes':
        print("Operation cancelled.")
        return

    # Get the nonce for the sender's address
    nonce = w3.eth.get_transaction_count(sender_address)

    trx_count = 1

    # Send Ether to each address
    for address in addresses:

        # Remove commented out addresses
        if address.startswith('#'):
            print(f'Skipping commented address: {address}')
            continue

        # Check if the address is valid
        if not w3.is_address(address):
            print(f"ERROR: Invalid address ({address})")
            continue

        # Estimate the gas required for the transaction
        gas_estimate = w3.eth.estimate_gas({
            "from": sender_address,
            "to": address,
            "value": amount_wei
        })


        # Calculate gas price
        gas_price = w3.eth.gas_price
        increased_gas_price = gas_price + (gas_price // 10)  # increase by 10%

        # Create a raw transaction
        raw_transaction = {
            'nonce': nonce,
            'to': address,
            'value': w3.to_wei(amount_ether, 'ether'),
            'gas': 21000,
            'gasPrice': increased_gas_price,
        }

        # Sign the transaction
        signed_transaction = w3.eth.account.sign_transaction(raw_transaction, sender_private_key)

        # Send the transaction
        transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        print(f"{trx_count}: Sent {amount_ether} Ether to {address}. Transaction hash: {transaction_hash.hex()}")

        # increment nonce for the next transaction
        nonce += 1
        trx_count += 1

if __name__ == "__main__":
    # Get the amount as a parameter
    parser = argparse.ArgumentParser(description='Send Ether to a list of addresses.')
    parser.add_argument('amount', type=float, help='Amount of Ether to send.')
    args = parser.parse_args()

    # Example usage:
    # Replace the following placeholders with actual values:
    # - <filename> with the file name containing the list of Ethereum addresses
    # - <amount_ether> with the amount of Ether to send (e.g., 0.01)
    # - <config_file> with the path to the config.ini file
    send_ether_to_addresses('send_ether.addresses', args.amount, 'send_ether.ini')
