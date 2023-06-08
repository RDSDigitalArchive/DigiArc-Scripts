import os
import sys
import csv
import xml.etree.ElementTree as ET

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

def create_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def create_xml(data, output_file):
    root = ET.Element('data')
    for row in data:
        entry = ET.SubElement(root, 'entry')
        for field_value in row:
            field = ET.SubElement(entry, 'Field')
            field.text = field_value

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: extract_data.py input_csv output_directory")
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
    create_csv(extracted_data, output_csv_file)
    create_xml(extracted_data, output_xml_file)
