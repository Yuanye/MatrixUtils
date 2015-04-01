# -*- coding: utf-8 -*- 
# 
# From 42qu.com
#
from hashlib import md5
from rfc3987 import parse

chars = [
        "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" ,
        "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" ,
        "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" ,
        "y" , "z" , "0" , "1" , "2" , "3" , "4" , "5" ,
        "6" , "7" , "8" , "9" , "A" , "B" , "C" , "D" ,
        "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" ,
        "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" ,
        "U" , "V" , "W" , "X" , "Y" , "Z"
        ]


def shorten(url, salt='42', offset=0):
    result = []
    s = md5(salt+ url).hexdigest()

    for i in range(0, 4):
        hexint = int(s[i * 8:(i+1) * 8], 16) & 0x3fffffff
        outChars = ""
        for j in range(0,10):
            index = hexint & 0x0000003D
            outChars += chars[index]
            hexint = hexint >> 3
        result.append(outChars)
    return result[offset]

def validate_url(url):
    try:
        p = parse(url, rule='URI_reference')
        r = all((p['scheme'], p['authority'], p['path']))
    except Exception as e:
        print e
        r = False 
    return r

if __name__ == "__main__":
    pass
