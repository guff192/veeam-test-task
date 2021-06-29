#!/usr/bin/env python
import hashlib
import os
import sys

hashfuncs = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256}


def usage():
    pass


def file_hash_sum(filepath, algorithm):
    file_hash = hashfuncs[algorithm]()
    with open(filepath, 'rb') as f:
        while block := f.read(4096):
            file_hash.update(block)
    return file_hash.hexdigest()


args = sys.argv[1:]
input_file_path = args[0]
dir_path = args[1]

if not (os.path.isfile(input_file_path) and os.path.isdir(dir_path)):
    usage()
    exit(1)

with open(input_file_path, 'r') as file:
    data = file.readlines()
for line in data:
    file_info = line.split()
    if len(file_info) != 3:
        continue

    name, alg, test_sum = file_info
    full_name = os.path.join(dir_path, name)

    if not os.path.isfile(full_name):
        print(name, 'NOT FOUND')
        continue

    real_sum = file_hash_sum(full_name, alg)
    print(name, end=' ')
    if real_sum == test_sum:
        print('OK')
    else:
        print('FAIL')

