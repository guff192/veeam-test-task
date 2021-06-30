import hashlib
import os


def usage():
    print('./task2.py path_to_the_input_file path_to_the_directory_containing_files')
    exit(1)


def get_args(argv):
    if len(argv) != 2:
        usage()
    input_file_path = argv[0]
    dir_path = argv[1]
    if not (os.path.isfile(input_file_path) and os.path.isdir(dir_path)):
        usage()
    return input_file_path, dir_path


hashfuncs = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256}


def file_hash_sum(filepath, algorithm):
    file_hash = hashfuncs[algorithm]()
    with open(filepath, 'rb') as f:
        while block := f.read(4096):
            file_hash.update(block)
    return file_hash.hexdigest()


def check_sums(input_file_path, dir_path):
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
        if alg not in hashfuncs.keys():
            print(name)

        real_sum = file_hash_sum(full_name, alg)
        if real_sum == test_sum:
            print(name, 'OK')
        else:
            print(name, 'FAIL')

