#!/usr/bin/env python
import sys

from utils import get_args, check_sums

input_file_path, dir_path = get_args(sys.argv[1:])

check_sums(input_file_path, dir_path)
