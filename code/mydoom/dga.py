'''
    DGA of Mydoom
'''

import argparse
from datetime import datetime 

def dga(date, seed, nr, tlds):
    _sld = ['e', 'v', 'l', 'k', 'r', 'd', 'o', 'h', 'l', 'p']
    magic = 'nj'
    len_sld = len(_sld)
    for i in range(len_sld):
        for j in range(len(magic)):
            _sld[i] = chr(ord(_sld[i]) ^ ((ord(magic[j]) + i * j) & 0xff))

    _seed = seed + date.year + date.month + date.day

    for i in range(nr):
        if i == nr - 1:
            _seed = seed

        _seed = ((_seed * 0x19660d) + 0x3c6ef35f) & 0xffffffff

        sld = ''
        tld = ''
        m = _seed
        for j in range(len_sld):
            idx = m % len_sld
            sld += _sld[idx]
            if j == 0:
                if idx < 7:
                    tld = tlds[idx]
                else:
                    tld = tlds[-1]

            m = m / len_sld

        print sld + '.' + tld

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help="Seconds since January 1, 1970 UTC")
    parser.add_argument("-n", "--nr", help="nr of domains", type=int, default=51)
    parser.add_argument("-s", "--seed", help="RAND_MAX", default="0xfa8")
    parser.add_argument("-T", "--tlds", help="TLD", default="com-biz-us-net-org-ws-info-in")

    args = parser.parse_args()

    d = datetime.utcfromtimestamp(int(args.time))
    tlds = args.tlds.split('-')
    dga(d, int(args.seed, 16), args.nr, tlds)
