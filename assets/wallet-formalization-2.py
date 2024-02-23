def generate_key_pair(random_seed: int) -> (hex, hex, hex):
        private_key = generate_private_key(random_seed)
        public_key = elliptic_curve('curve', private_key) # curve - secp256k1, ed25519... etc
        address = hash_algorithm(public_key)
        return (private_key, public_key, address)

def key_storage(private_key: hex, password: str) -> bytes:
    if private_key is None:
        raise ValueError("Private key not generated.")
    encrypted_private_key = encryption_algorithm(private_key, password)
    return encrypted_private_key

def create_transaction(prev_nonce: int, sender_address: hex, recipient_address: hex, amount: float, gas_fee: float, smart_contract_data=None) -> (int, dict):
    user_balance = update_user_balance(sender_address)
    if user_balance < amount + gas_fee:
        raise Exception("Insufficient balance to perform the transaction")
    nonce = prev_nonce + 1
    transaction = {
        "from": self.address,
        "to": recipient_address,
        "nonce": nonce,
        "amount": amount,
        "gas_fee": gas_fee,
        "smart_contract_data": smart_contract_data,  # For smart contract interactions
    }
    return (nonce, transaction)

def sign_transaction(encrypted_private_key: bytes, password: str, transaction_data: dict) -> dict:
    private_key = decryption_algorithm(encrypted_private_key, password)
    transaction_hash = hash_algorithm(transaction_data)
    signature = sign(transaction_hash, decrypted_private_key)
    signed_transaction = {
        "transaction_data": transaction_data,
        "signature": signature
    }
    return signed_transaction

def broadcast_transaction(signed_transaction: dict, public_key: hex, sender_address: hex) -> bool:
    verified = broadcast_to_network(signed_transaction, public_key)
    if(verified):
        balance = update_user_balance(sender_address)
        print("Transaction Successful")
        return True
    else:
        raise Exception("Transaction Failed")
        return False


class Wallet:
    def __init__(self, password: str, balance: float =0, nonce: int =0):
        key_pair = generate_key_pair()
        self.nonce = nonce
        self.balance = balance
        self.private_key = key_storage(key_pair[0], password)
        self.public_key = key_pair[1]
        self.address = key_pair[2]

    def transact(self, password: str, amount: float, recipient_address: hex, gas_fee: float, smart_contract_data: dict):
        transaction = create_transaction(self.address, recipient_address, amount, gas_fee, smart_contract_data)
        self.nonce = transaction[0]
        signed_transaction = sign_transaction(self.private_key, password, transaction[1])
        broadcast_transaction(signed_transaction, self.public_key, self.address)
