# XML_JSON_converter

This Python script is designed to efficiently convert XML files into JSON format, making it easier to work with data in applications that prefer JSON. It is particularly useful for developers dealing with data interchange between systems or applications that produce XML output but require data in JSON format for further processing or API consumption.

Key Features:
Dynamic Handling of Elements: Automatically processes all elements within an XML document, converting them into equivalent JSON structures.
Attribute Awareness: Pays special attention to attributes like size and type within XML elements, using them to inform the structure and data types in the JSON output. This ensures that elements marked with a size attribute are appropriately converted into arrays or objects, reflecting their intended structure, and that data types are preserved according to the type attribute, ensuring numeric values are correctly represented in JSON.
Error Handling: Includes robust error handling to gracefully manage any issues encountered during the conversion process, such as improperly formatted XML or unsupported data types, ensuring the script's reliability across a wide range of XML documents.
Ease of Use: Designed with simplicity in mind, requiring minimal configuration to convert an XML file to JSON. Users can easily integrate this script into larger workflows or systems that require XML to JSON conversion.