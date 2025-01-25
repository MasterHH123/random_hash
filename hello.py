import hashlib, os

def random_hash():
    n = 1000

    for _ in range(n):
        generated_hash = hashlib.md5(os.urandom(32)).hexdigest()
        if generated_hash[0] == '0' and generated_hash[1] == '0':
            #found = True
            #break
            return generated_hash
    return None

