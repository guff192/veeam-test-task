#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET

from utils import get_files_list, process_copies

files = get_files_list(sys.argv[1:])

for config_name in files:
    try:
        tree = ET.parse(config_name)
    except ET.ParseError as e:
        print(f'Invalid xml file format "{config_name}": {e}')
        continue
    except FileNotFoundError as e:
        print(e)
        continue
    else:
        print(f'Config file: "{config_name}"')
        process_copies(tree)
