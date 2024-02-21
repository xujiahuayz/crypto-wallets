class Wallet:
    def __init__(self, balance=0):
        self.balance = balance
        self.private_key = None
        self.address = None

    def key_generation(self, random_seed:int) -> hex:
        # private key - randomness and hash
        self.private_key = generate_pk(random_seed)

        # public key - uses ec cryptography -> secp256k1, ed25519... etc
        public_key = elliptic_curve('curve', private_key)

        # address - hash(public key)
        self.address = Hashing_Algorithm(public_key)
        return private_key, address

    def key_storage(self, private_key:hex, password:str) -> bin:
        # any encryption algorithm
        self.private_key = Encryption_Algorithm(private_key, password)
        return encrypted_private_key

    def txn_sign(self, encrypted_private_key:bin, password:str, transaction_data) -> hex:
        self.private_key = Decryption_Algorithm(encrypted_private_key, password)
        transaction_hash = Hashing_Algorithm(transaction)

        signature = Sign(transaction_hash, private_key)
        signed_transaction = {
            "transaction_data": transaction,
            "signature": signature
        }

        return signed_transaction
        
    def txn_valid(self, transaction, public_key:hex) -> bool:
        signature = transaction.signature
        originalData = transaction.transaction_data

        dataHash = Hash(originalData)
        isValid = Verify(dataHash, signature, publicKey)

        return isValid
