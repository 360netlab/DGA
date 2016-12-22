'''
    DGA of vidro
'''

import argparse

def rand(seed):
    seed = (seed * 0x41c64e6d  + 0x3039) & 0xffffffff
    return seed, (seed >> 0xa)

def dga(epoch, nr):
    tlds = ['dyndns.org', 'com', 'net']
    seed_init = 0x1e240 * \
           (((epoch-0x4BEFB280)<<32)/(0x93a80<<32)+0x3ed)

    for i in range(nr):
        seed = i % 100 + seed_init
        seed, r = rand(seed)
        sld_len =  r % 6 + 7

        domain = ''
        for _ in range(sld_len):
            seed, r = rand(seed)
            domain += chr(r % 26 + ord('a'))

        domain += '.' + tlds[i % 3]
        print domain

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help="Seconds since January 1, 1970 UTC")
    parser.add_argument("-n", "--nr", help="nr of domains to generate")
    args = parser.parse_args()
    
    dga(int(args.time), int(args.nr))
