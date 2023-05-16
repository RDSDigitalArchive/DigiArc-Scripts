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
    parser.add_argument('filepath', help='Path of the file to generate the MD5 hash for')
    parser.add_argument('-o', '--output_dir', default=os.getcwd(), help='Path of the directory to save the MD5 file to')
    args = parser.parse_args()

    md5_hash = generate_md5(args.filepath)
    filename = os.path.basename(args.filepath)
    md5_filename = filename + ".md5"
    md5_filepath = os.path.join(args.output_dir, md5_filename)

    with open(md5_filepath, 'w') as f:
        f.write(md5_hash)
    print(f"MD5 hash generated successfully for {filename}.md5 and saved at {md5_filepath}")
