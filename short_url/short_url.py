import re
import hashlib

x = 'http://www.wepiao.com/'

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

m = hashlib.md5(x).hexdigest()

m = re.findall(r'.{8}', m)

r = []
for v in m:
    l = int(v, 16) & 0x3FFFFFFF   # 30bits
    o = ''
    for i in range(6):
        idx = l & 0x3D           # 0x3D == 61 
        o += s[idx]
        l = l >> 5
    r.append(o)
print r
