import os

dir_path = input("Enter the directory path: ")
first_num = input("Enter the first number in the sequence: ")

# get a list of all files in the directory
file_list = os.listdir(dir_path)

# filter out any subdirectories
file_list = [filename for filename in file_list if os.path.isfile(os.path.join(dir_path, filename))]

# iterate over the files and rename them
for i, filename in enumerate(file_list):
    # get the file extension
    file_ext = os.path.splitext(filename)[1]
    # construct the new filename using the naming convention
    new_filename = f"RDS_DO_{first_num.zfill(4)}_{str(i+1).zfill(4)}{file_ext}"
    # rename the file
    os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
