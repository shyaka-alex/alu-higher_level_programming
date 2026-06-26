#!/usr/bin/python3
for i in range(26):
    c = chr(ord('z') - i)
    if i % 2 == 0:
        print("{}".format(c), end="")
    else:
        print("{}".format(c.upper()), end="")
