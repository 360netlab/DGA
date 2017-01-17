import hashlib
from datetime import datetime 
import argparse

def serialize(digest):
    result = 20*[0]
    for i, s in enumerate(digest):
        result[3 - i % 4 + i / 4 * 4] = s
    return result

        
def dga(date, nr, length):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    tlds = ['.com', '.org', '.net', '.biz', '.info', '.ru', '.cn']

    for index in range(nr):
        seed = 16*[0]
        seed[0] = ((date.year & 0xFF) + 0x30) & 0xFF
        seed[1] = date.month & 0xFF
        seed[2] = date.day & 0xFF
        seed[3] = index & 0xFF
        seed[4] = (index >> 8) & 0xFF

        seed_str = ""
        for i in range(16):
            seed_str += chr(seed[i])

        s = hashlib.sha1()
        s.update(seed_str)
        sha1 = serialize(s.digest())

        domain = ""
        for i in range(length):
            domain += alpha[ord(sha1[i]) % 36]

        domain += tlds[ord(sha1[length]) % 7]

        print(domain)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help="Seconds since January 1, 1970 UTC")
    parser.add_argument("-n", "--nr", help="nr of domains to generate")
    parser.add_argument("-l", "--len", help="Length of SLD")
    args = parser.parse_args()
    
    d = datetime.utcfromtimestamp(int(args.time))
    
    dga(d, int(args.nr), int(args.len))
