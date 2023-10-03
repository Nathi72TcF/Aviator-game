import matplotlib.pyplot as plt
import numpy as np
import hashlib
import random
import string
import hmac

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"

# game_hash = '100af1b49f5e9f87efc81f838bf9b1f5e38293e5b4cf6d0b366c004e0a8d9987'
game_hash = '92bcf32f57b4d71895c557919bf98744178d366023c2c74f6ed800b4dd060ece46fc5c68e88ff8dd55d375244283c6aff4093d4580a1d410414e9c49ad3d0081'
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"

def get_result(game_hash):
    # hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha512)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    return (((100 * e - h) / (e - h)) // 1) / 100.0

def get_prev_game(hash_code):
    # m = hashlib.sha256()
    m = hashlib.sha512()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()

results = []
count = 0
while game_hash != first_game:
    count += 1
    results.append(get_result(game_hash))
    game_hash = get_prev_game(game_hash)
    
results = np.array(results)



def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    print(HashedPassword)

# Sha512Hash('Hi')
# print(Sha512Hash('Hi'))

# print(count)
print(get_prev_game(game_hash))
