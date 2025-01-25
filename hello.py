import hashlib, os

def random_hash():
    n = 1000

    for _ in range(n):
        hash = hashlib.md5(os.urandom(32)).hexdigest()
        if hash[0] == '0' and hash[1] == '0':
            #found = True
            #break
            return hash
    return None

