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

### rename_dir.py
This script will rename a directory of files, which sum the total of one digital object, according to the RDS Digital Archive's naming convention: RDS_DO_####_#### 

The user will be asked to enter the directory path followed by the digital object number. 

The digital object number is assigned in the Digital Object Register. Please consult the register before running this script.

Usage:

``
rename_dir.py
``

The command-line will return a prompt for the input directory path followed by the first number in the sequence:

``
Enter the directory path: /path/to/input_directory
``

``
Enter the first number in the sequence: ####
``
