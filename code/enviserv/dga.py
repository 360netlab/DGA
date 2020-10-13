'''
    DGA of Enviserv
'''

import argparse
import hashlib
import struct

def dga(seed, nr, tlds):
    for i in range(nr):
        seed_str = seed + str(i)
        #print seed_str

        s = hashlib.md5()
        s.update(seed_str.encode('latin1'))
        x = s.digest()

        domain = ""
        for j in range(5):
            domain += "%02x" %(x[j])

        domain += '.' + tlds[i % 6]

        print(domain)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nr", help="nr of domains", type=int, default=500)
    parser.add_argument("-s", "--seed", help="random string", default="papa_koli")
    parser.add_argument("-T", "--tlds", help="TLD", default="com-net-org-info-biz-in")

    args = parser.parse_args()

    tlds = args.tlds.split('-')
    dga(args.seed, args.nr, tlds)
