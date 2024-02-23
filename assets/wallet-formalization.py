class Wallet:
    def __init__(self, balance=0, nonce=0):
        self.balance = balance
        self.private_key = None
        self.public_key = None
        self.address = None
        self.nonce = nonce

    def generate_key_pair(self, random_seed: int) -> (hex, hex):
        self.private_key = generate_private_key(random_seed)
        self.public_key = elliptic_curve('curve', self.private_key) # curve - secp256k1, ed25519... etc
        self.address = hash_algorithm(public_key)
        return (self.private_key, self.public_key, self.address)

    def key_storage(self, password: str) -> bytes:
        if self.private_key is None:
            raise ValueError("Private key not generated.")
        encrypted_private_key = encryption_algorithm(self.private_key, password)
        return encrypted_private_key

    # def create_transaction(self, recipient_address: hex, amount: float) -> dict:
        # transaction = {
        #     'from': self.address,
        #     'to': recipient_address,
        #     'amount': amount
        # }
        # return transaction

    # def create_transaction(self, recipient_address: hex, amount: float, contract_address: hex = None, function_name: str = None, function_args: list = None) -> dict:
    #     if contract_address is None:
    #         transaction = {
    #             'from': self.address,
    #             'to': recipient_address,
    #             'amount': amount
    #         }
    #     else:
    #         transaction = {
    #             'from': self.address,
    #             'to': contract_address,
    #             'amount': amount,
    #             'data': {
    #                 'function': function_name,
    #                 'args': function_args
    #             }
    #         }
    #     return transaction

    def create_transaction(self, recipient_address, amount, gas_fee, data=None):
        self.balance = update_user_balance(self.address)
        if self.balance < amount + gas_fee:
            raise Exception("Insufficient balance to perform the transaction")
        self.nonce += 1
        transaction = {
            "from": self.address,
            "to": recipient_address,
            "nonce": self.nonce,
            "amount": amount,
            "gas_fee": gas_fee,
            "data": data,  # For smart contract interactions
        }
        return transaction

    def sign_transaction(self, encrypted_private_key: bytes, password: str, transaction_data) -> dict:
        private_key = decryption_algorithm(encrypted_private_key, password)
        transaction_hash = hash_algorithm(transaction_data)
        signature = sign(transaction_hash, decrypted_private_key)
        signed_transaction = {
            "transaction_data": transaction_data,
            "signature": signature
        }
        return signed_transaction

    def broadcast_transaction(self, signed_transaction: dict) -> bool:
        verified = verify_transaction(signed_transaction, self.public_key)
        if(verified):
            self.balance = update_user_balance(self.address)
            print("Transaction Successful")
            return True
        else:
            raise Exception("Transaction Failed")
            return False

    def verify_transaction(transaction, public_key: hex) -> bool:
        original_data = transaction['transaction_data']
        signature = transaction['signature']
        data_hash = hash_algorithm(original_data)
        is_valid = verify(data_hash, signature, public_key)
        return is_valid
