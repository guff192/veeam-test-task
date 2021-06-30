# Test task for Veeam Software

1) <a href="#task-1">Task 1</a>
2) <a href="#task-2">Task 2</a>

## Task 1
<hr>

Simple command-line utility for copying files according to XML configs.  
Also supports selecting directory, containing configs.

### Make file executable
```shell
chmod +x task1/task1.py
```

### Usage
```shell
task1/task1.py config_files...
task1/task1.py -d <configs_dir>
```

### Config file format
Examples of config files are in config_examples/
```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
    <file
            source_path="path_to_file"
            destination_path="path_to_copy_file"
            file_name="file_to_copy"
    />
    <file
            source_path="path_to_file2"
            destination_path="path_to_copy_file2"
            file_name="file_to_copy2"
    />
    <!-- ........... -->
</config>

```


## Task 2
<hr>

Command-line utility to check file hash sums in directory according to input file.

###Make file executable
```shell
chmod +x task2/task2.py
```

### Usage
```shell
task2/task2.py input_file directory_with_files
```

### Input file format
Input file example: "test_input_file"
```shell
# file_name hash_algorithm sum_to_check
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709
```

