import getopt
import os
import shutil
import xml.etree.ElementTree


def get_files_list(argv):
    try:
        options, args = getopt.getopt(argv, '-d:')
        options = dict(options)
        assert len(args) > 0 or options.get('-d')
    except Exception as e:
        print(e)
        print('Usage:\n./task1.py config_files...\n./task1.py -d <configs_dir>')
        exit()

    if len(args) == 0:
        return map(
            lambda s: os.path.join(options['-d'], s),
            os.listdir(options['-d'])
        )

    return args


def check_attributes_errors(src: str, dst: str, name: str) -> str:
    if not (src and dst and name):
        return f'Please provide "source_path", "destination_path" and "file_name" attributes!'

    file_path = os.path.join(src, name)
    if not os.path.isfile(file_path):
        return f'There is no file named "{name}" in {src} directory!'

    if not os.path.isdir(dst):
        os.makedirs(dst)

    return ''


def get_full_path(src: str, dst: str, name: str):
    error = check_attributes_errors(src, dst, name)
    if error:
        print(error)
        return ''

    return os.path.join(src, name)


def process_copies(tree: xml.etree.ElementTree.ElementTree):
    root = tree.getroot()
    for el in root:
        if el.tag != 'file':
            print(f'Wrong tag <{el.tag}>!')
            continue

        source_path = el.attrib.get('source_path')
        destination_path = el.attrib.get('destination_path')
        file_name = el.attrib.get('file_name')

        full_source_path = get_full_path(source_path, destination_path, file_name)
        if not full_source_path:
            continue

        shutil.copy2(full_source_path, destination_path)
