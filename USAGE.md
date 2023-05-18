## Usage

### batchmd5.py
This script will create an MD5 manifest file for each digital file located within a directory. The default output directory is the current working directory, however there is an option to specify the output directory with the ‘-o’ argument. If the directory doesn’t exist, it will be created.

Usage with option to specify the output directory:

``
batchmd5.py /path/to/input_directory -o /path/to/output_directory
``

### md5.py
This script will create an MD5 manifest file for a digital file. The default output directory is the current working directory, however there is an option to specify the output directory with the ‘-o’ argument.

Usage with option to specify the output directory:

``
md5.py /path/to/input_file -o /path/to/output_directory
``
