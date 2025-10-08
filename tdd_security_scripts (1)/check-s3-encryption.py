#!/usr/bin/env python3
import subprocess, json, sys

buckets = json.loads(subprocess.check_output([
    "aws","s3api","list-buckets","--query","Buckets[].Name","--output","json"
]))

non_enc = []
for b in buckets:
    try:
        subprocess.check_output(["aws","s3api","get-bucket-encryption","--bucket",b])
    except subprocess.CalledProcessError:
        non_enc.append(b)

if non_enc:
    print("RED: Buckets sin cifrado:", non_enc)
    sys.exit(1)
else:
    print("GREEN: Todos los buckets cifrados")
    sys.exit(0)
