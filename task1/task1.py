import os
import shutil
import xml.etree.ElementTree as ET


def check_attributes_errors(src: str, dst: str, name: str) -> (str, str):
    if src is None or dst is None or name is None:
        return f'Please provide "source_path", "destination_path" and "file_name" attributes!', ''

    full_source_path = os.path.join(source_path, name)
    if not os.path.isfile(full_source_path):
        return f'There is no file named "{name}" in {source_path} directory!', ''

    if not os.path.isdir(destination_path):
        os.makedirs(destination_path)

    return '', full_source_path


tree = ET.parse('config.xml')
root = tree.getroot()

for el in root:
    if el.tag != 'file':
        print(f'Wrong tag name "{el.tag}"!')
        continue

    source_path = el.attrib.get('source_path')
    destination_path = el.attrib.get('destination_path')
    file_name = el.attrib.get('file_name')

    error, full_source_path = check_attributes_errors(source_path, destination_path, file_name)
    if error:
        print(error)  # or we can log here
        continue

    print(source_path, destination_path, file_name)
    shutil.copy2(full_source_path, destination_path)
