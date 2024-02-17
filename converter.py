import xml.etree.ElementTree as ET
import json

def process_value(element, rows, cols):
    """Processes values' elements to handle numeric and non-numeric values accordingly."""
    # Flatten all text within the element to capture all values
    all_text = ''.join(element.itertext()).split()
    
    # Convert values according to their type (numeric or string)
    values = [convert_value(val) for val in all_text]
    
    if cols > 1:
        # Organize values into a 2D list (matrix) for multi-dimensional data
        return [values[i:i + cols] for i in range(0, len(values), cols)]
    else:
        # Return as a single list if effectively a 1D array
        return values

def convert_value(value):
    """Converts value to int/float if numeric, otherwise returns the original string."""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value  # Return original string if conversion fails

def process_element(element):
    """Processes each element."""
    if 'size' in element.attrib:
        size = element.attrib['size']
        if size == "0":  # Handle empty elements when 'size' is '0'
            return None  
        
        rows, cols = map(int, size.split())
        if rows == 0 or cols == 0:
            return None  
        
        return process_value(element, rows, max(1, cols))  # Ensure cols is at least 1
    elif list(element):  # If the element has children, recursively process each child
        return {child.tag: process_element(child) for child in element}
    else:
        # Handle leaf elements without children by converting their text content
        return element.text.strip() if element.text else ''

def convert_xml_to_json(xml_root):
    """Converts the XML structure to JSON format."""
    return {element.tag: process_element(element) for element in xml_root}

# Load the XML file
xml_file_path = 'test_equate.xml'  
tree = ET.parse(xml_file_path)
root = tree.getroot()

conversion_result = convert_xml_to_json(root)

# Save the conversion result to a JSON file
json_file_path = 'test_equate.json' 
with open(json_file_path, 'w') as json_file:
    json.dump(conversion_result, json_file, indent=4)
