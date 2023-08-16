# import xml.etree.ElementTree as ET
#
# # Define namespaces
# namespaces = {
#     'default': 'urn:hl7-org:v3',
#     'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
#     'sdtc': 'urn:hl7-org:sdtc'
# }
#
#
# def extract_section_data(section_name):
#     # Parse the XML file
#     tree = ET.parse('files/CCDA_Williams_Suzanne (3).xml')
#     root = tree.getroot()
#
#     # Search for the section by its title
#     for section in root.findall(".//default:section", namespaces=namespaces):
#         title_element = section.find("default:title", namespaces=namespaces)
#         if title_element is not None and title_element.text == section_name:
#             # Convert the section subtree to a formatted XML string
#             return ET.tostring(section, encoding="unicode", method="xml")
#     return "Section not found"
#
#
# def xml_to_readable(section_xml):
#     # Parse the provided section XML
#     section = ET.fromstring(section_xml)
#
#     # Initialize the readable output
#     output = []
#
#     # Extract section title
#     title_element = section.find("default:title", namespaces=namespaces)
#     if title_element is not None:
#         output.append(title_element.text)
#         output.append('-' * len(title_element.text))
#
#     # Extract table data
#     for table in section.findall(".//default:table", namespaces=namespaces):
#         # Extract table headers
#         headers = [th.text for th in table.findall(".//default:thead/default:tr/default:th", namespaces=namespaces)]
#         output.append(' | '.join(headers))
#         output.append('-' * (sum([len(header) for header in headers]) + len(headers) * 3 - 2))
#
#         # Extract table rows
#         for row in table.findall(".//default:tbody/default:tr", namespaces=namespaces):
#             row_data = [td.text if td.text else ' '.join(td.itertext()) for td in
#                         row.findall(".//default:td", namespaces=namespaces)]
#             output.append(' | '.join(row_data))
#
#         output.append('')
#
#     return '\n'.join(output)
#
#
# # Example usage:
# section_name = "Assessment"
# section_xml = extract_section_data(section_name)
# readable_output = xml_to_readable(section_xml)
# print(readable_output)

# import xml.etree.ElementTree as ET
#
# # Define namespaces
# namespaces = {
#     'default': 'urn:hl7-org:v3',
#     'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
#     'sdtc': 'urn:hl7-org:sdtc'
# }
#
#
# def extract_section_names():
#     # Parse the XML file
#     tree = ET.parse('files/CCDA_Williams_Suzanne (3).xml')
#     root = tree.getroot()
#
#     # Extract section names
#     section_names = []
#     for section in root.findall(".//default:section", namespaces=namespaces):
#         title_element = section.find("default:title", namespaces=namespaces)
#         if title_element is not None:
#             section_names.append(title_element.text)
#     return section_names
#
#
# def extract_section_data(section_name):
#     # Parse the XML file
#     tree = ET.parse('files/CCDA_Williams_Suzanne (3).xml')
#     root = tree.getroot()
#
#     # Search for the section by its title
#     for section in root.findall(".//default:section", namespaces=namespaces):
#         title_element = section.find("default:title", namespaces=namespaces)
#         if title_element is not None and title_element.text == section_name:
#             # Convert the section subtree to a formatted XML string
#             return ET.tostring(section, encoding="unicode", method="xml")
#     return "Section not found"
#
#
# def xml_to_readable(section_xml):
#     section = ET.fromstring(section_xml)
#
#     output = []
#
#     title_element = section.find("default:title", namespaces=namespaces)
#     if title_element is not None:
#         output.append(title_element.text)
#         output.append('-' * len(title_element.text))
#
#     for table in section.findall(".//default:table", namespaces=namespaces):
#         headers = [th.text for th in table.findall(".//default:thead/default:tr/default:th", namespaces=namespaces)]
#         output.append(' | '.join(headers))
#         output.append('-' * (sum([len(header) for header in headers]) + len(headers) * 3 - 2))
#
#         for row in table.findall(".//default:tbody/default:tr", namespaces=namespaces):
#             row_data = [td.text if td.text else ' '.join(td.itertext()) for td in
#                         row.findall(".//default:td", namespaces=namespaces)]
#             output.append(' | '.join(row_data))
#
#         output.append('')
#
#     return '\n'.join(output)
#
#
# # Example usage:
# section_names_list = extract_section_names()
# print("Available section names:")
# for section_name in section_names_list:
#     print("- " + section_name)
#
# chosen_section_name = input("\nEnter a section name to display its data: ")
# chosen_section_xml = extract_section_data(chosen_section_name)
# if chosen_section_xml != "Section not found":
#     readable_output = xml_to_readable(chosen_section_xml)
#     print("\nReadable output for '{}' section:".format(chosen_section_name))
#     print(readable_output)
# else:
#     print("\nChosen section '{}' not found.".format(chosen_section_name))
import os
import xml.etree.ElementTree as ET
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for the app
# Define namespaces
namespaces = {
    'default': 'urn:hl7-org:v3',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'sdtc': 'urn:hl7-org:sdtc'
}

def extract_section_names(xml_path):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract section names
    section_names = []
    for section in root.findall(".//default:section", namespaces=namespaces):
        title_element = section.find("default:title", namespaces=namespaces)
        if title_element is not None:
            section_names.append(title_element.text)
    return section_names

def extract_section_data(xml_path, section_name):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Search for the section by its title
    for section in root.findall(".//default:section", namespaces=namespaces):
        title_element = section.find("default:title", namespaces=namespaces)
        if title_element is not None and title_element.text == section_name:
            # Convert the section subtree to a formatted XML string
            return ET.tostring(section, encoding="unicode", method="xml")
    return "Section not found"

def xml_to_readable(section_xml):
    section = ET.fromstring(section_xml)

    output = []

    title_element = section.find("default:title", namespaces=namespaces)
    if title_element is not None:
        output.append(title_element.text)
        output.append('-' * len(title_element.text))

    for table in section.findall(".//default:table", namespaces=namespaces):
        headers = [th.text for th in table.findall(".//default:thead/default:tr/default:th", namespaces=namespaces)]
        output.append(' | '.join(headers))
        output.append('-' * (sum([len(header) for header in headers]) + len(headers) * 3 - 2))

        for row in table.findall(".//default:tbody/default:tr", namespaces=namespaces):
            row_data = [td.text if td.text else ' '.join(td.itertext()) for td in
                        row.findall(".//default:td", namespaces=namespaces)]
            output.append(' | '.join(row_data))

        output.append('')

    return '\n'.join(output)

@app.route("/", methods=['GET'])
def hello():
    return jsonify("Hello World")

@app.route("/upload", methods=["POST"])
def index():
    if request.method == "POST":
        print("Inside upload method")
        xml_file = request.files["xml_file"]
        xml_path = os.path.join("files", xml_file.filename)
        xml_file.save(xml_path)
        print("Inside upload method file saved")

        return jsonify("XML file uploaded successfully!"), 200


@app.route("/get_section_names", methods=["GET"])
def get_section_names():
    xml_path = os.path.join("files", "CCDA_Williams_Suzanne (3).xml")  # Provide the correct file path
    section_names_list = extract_section_names(xml_path)
    return jsonify({"section_names": section_names_list})

@app.route("/get_section_data/<section_name>", methods=["GET"])
def get_section_data(section_name):
    xml_path = os.path.join("files", "CCDA_Williams_Suzanne (3).xml")  # Provide the correct file path
    chosen_section_xml = extract_section_data(xml_path, section_name)
    if chosen_section_xml != "Section not found":
        readable_output = xml_to_readable(chosen_section_xml)
        return jsonify({"section_data": readable_output})
    else:
        return jsonify({"message": f"Section '{section_name}' not found."})

if __name__ == "__main__":
    app.run(debug=True)
