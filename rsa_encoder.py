import math
from rsa_key_generator import RSAKeyGenerator

class RSAEncoder:
    @staticmethod
    def encode(msg):
        print(f'Original message: {msg}')
        
        public_key, private_key = RSAKeyGenerator.generate_keys()
        n, e = public_key
        n, d = private_key
        
        # szyfrowanie
        C = pow(msg, e)
        C = math.fmod(C, n)
        print(f'Encrypted message: {C}')
        
        # deszyfrowanie
        M = pow(C, d)
        M = math.fmod(M, n)
        
        print(f'Decrypted message: {M}')
    
if __name__ == "__main__":
    RSAEncoder.encode(2)
    