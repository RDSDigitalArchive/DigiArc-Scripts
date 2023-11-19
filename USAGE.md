## Usage

### batchmd5.py
This script will create an MD5 manifest file for each digital file located within a directory. The default output directory is the current working directory, however there is an option to specify the output directory with the ‘-o’ argument. If the directory doesn’t exist, it will be created.

Usage with option to specify the output directory:

``
batchmd5.py /path/to/input_directory -o /path/to/output_directory
``

### extract_data.py
This script will extract relevant data from the Digital Object Register (CSV file format), pertaining to a specified digital object, and create a content information file in both CSV and XML format, to be included in the appropriate archival information package.

Usage:

``
extract_data.py /path/to/input_csv /path/to/output_directory
``

The command-line will return a prompt to input the digital object number:

``
Enter the digital object number (RDS_DO_####):
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

The command-line will return a prompt for the input directory path followed by the digital object number:

``
Enter the directory path: /path/to/input_directory
``

``
Enter the digital object number: ####
``

### validate.py
This script will validate an MD5 file or directory containing a batch of MD5 files against corresponding file or files. The MD5 input may be in a file or directory form whereas the corresponding file(s) must be in the form of a directory. 

The command-line will display the validation results, indicating whether each MD5 file is valid or invalid. At the end of the batch validation, a summary will be printed showing the total count of files validated.

Usage:

``
validate.py /path/to/input_file /path/to/corresponding_directory
``

``
validate.py /path/to/input_directory /path/to/corresponding_directory
``
