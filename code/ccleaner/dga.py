'''
    DGA of CCleaner
'''

import argparse
from datetime import datetime

def msvcrt_rand(seed):
    new_seed = (0x343fd * seed + 0x269ec3) & ((1 << 32) - 1)
    randval = (new_seed >> 16) & 0x7fff
    return randval, new_seed

def dga(year, month, nr, tlds):

    r1, seed = msvcrt_rand(year * 10000 + month)
    r2, seed = msvcrt_rand(seed)
    r3, seed = msvcrt_rand(seed)
    

    sld = 'ab%x%x' %(r2 * r3, r1)

    domain = sld + '.' + tlds[0]
    print domain

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help="Seconds since January 1, 1970 UTC")
    parser.add_argument("-n", "--nr", help="nr of domains to generate")
    args = parser.parse_args()

    tlds = ['com']
        
    d = datetime.utcfromtimestamp(int(args.time))
    dga(d.year, d.month, int(args.nr), tlds)
