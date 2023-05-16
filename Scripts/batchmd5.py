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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate an MD5 hash for a file and save it to a specified directory')
    parser.add_argument('input_dir', help='Path of the directory containing the files to generate MD5 hashes for')
    parser.add_argument('-o', '--output_dir', default=os.getcwd(), help='Path of the directory to save the MD5 files to')
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"{args.input_dir} is not a directory")
        exit()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    for filename in os.listdir(args.input_dir):
        filepath = os.path.join(args.input_dir, filename)
        if os.path.isfile(filepath):
            md5_hash = generate_md5(filepath)
            md5_filename = filename + ".md5"
            md5_filepath = os.path.join(args.output_dir, md5_filename)

            with open(md5_filepath, 'w') as f:
                f.write(md5_hash)
            print(f"MD5 hash generated successfully for {filename} and saved at {md5_filepath}")
