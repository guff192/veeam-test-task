# Test task for Veeam Software

## Task 1
### Make file executable
```sh
chmod +x task1.py
```
### Usage
```sh
task1/task1.py config_files...
task1/task1.py -d <configs_dir>
```

### Config file format
Examples of config files are in config_examples/
```xml
<!-- <any_file_name>.xml -->
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
