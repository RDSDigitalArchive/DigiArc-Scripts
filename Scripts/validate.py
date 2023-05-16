import argparse
import hashlib
import os

def generate_md5(filepath):
    with open(filepath, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def validate_md5_file(md5_filepath, file_dir):
    with open(md5_filepath, 'r') as f:
        md5_hash = f.read().strip()
        filename = os.path.splitext(os.path.basename(md5_filepath))[0]
        original_filepath = os.path.join(file_dir, filename)

        if not os.path.exists(original_filepath):
            print(f"Error: File not found: {filename}")
            return False

        generated_hash = generate_md5(original_filepath)

        if generated_hash == md5_hash:
            print(f"{filename} is valid.")
            return True
        else:
            print(f"Error: {filename} is invalid.")
            return False

def validate_md5_batch(md5_dir, file_dir):
    valid_count = 0
    invalid_count = 0

    for filename in os.listdir(md5_dir):
        md5_filepath = os.path.join(md5_dir, filename)

        if os.path.isfile(md5_filepath) and filename.endswith('.md5'):
            if validate_md5_file(md5_filepath, file_dir):
                valid_count += 1
            else:
                invalid_count += 1

    print(f"\nBatch validation completed.")
    print(f"Valid MD5 files: {valid_count}")
    print(f"Invalid MD5 files: {invalid_count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate MD5 hash files against corresponding files')
    parser.add_argument('md5_input', help='Path to the MD5 file or directory to perform validation on')
    parser.add_argument('file_input', help='Path to the directory containing the corresponding files')
    args = parser.parse_args()

    if os.path.isfile(args.md5_input) and os.path.isdir(args.file_input):
        validate_md5_file(args.md5_input, args.file_input)
    elif os.path.isdir(args.md5_input) and os.path.isdir(args.file_input):
        validate_md5_batch(args.md5_input, args.file_input)
    else:
        print("Error: Invalid input. The first argument should be an MD5 file or directory, and the second argument should be a directory.")
