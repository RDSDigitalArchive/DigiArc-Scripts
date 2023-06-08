import os
import sys
import csv
import xml.etree.ElementTree as ET
import re

def extract_data(csv_file, field_value):
    extracted_data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        field_index = 0  # Default field index to column A (index 0)
        if headers[0] == 'Field A':
            field_index = 0  # If the header is Field A, use column A (index 0)
        for row in reader:
            if row[field_index] == field_value:
                extracted_data.append(row)
    return extracted_data

def sanitize_tag(tag):
    # Remove invalid characters and spaces from the tag
    tag = re.sub(r'[^\w.-]', '_', tag)
    tag = re.sub(r'\s+', '_', tag)
    return tag

def create_csv(headers, data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers[0:])
        writer.writerows(data)

def create_xml(data, field_titles, output_file):
    root = ET.Element('data')
    for row in data:
        entry = ET.SubElement(root, 'entry')
        for field_value, field_title in zip(row, field_titles):
            tag = sanitize_tag(field_title)
            field = ET.SubElement(entry, tag)
            field.text = field_value

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python extract_data.py input_csv output_directory")
        sys.exit(1)

    csv_file = sys.argv[1]
    field_value = input("Enter the value (RDS_DO_####): ")
    output_directory = sys.argv[2]

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_csv_file = os.path.join(output_directory, 'content_information.csv')
    output_xml_file = os.path.join(output_directory, 'content_information.xml')

    extracted_data = extract_data(csv_file, field_value)

    # Get the field titles from the second row of the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row
        field_titles = next(reader)

    create_csv(field_titles, extracted_data, output_csv_file)
    create_xml(extracted_data, field_titles, output_xml_file)
