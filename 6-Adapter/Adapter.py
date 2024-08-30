"""
    Adapter Design Pattern
    - a structural design pattern that allows objects with incompatible interfaces to collaborate.
"""
# We use the xmltodict library to convert XML data to JSON format.
# Install the library using: pip install xmltodict
import xmltodict


# Application class that generates and sends a request (in this case, an XML file).
class Application:
    def send_request(self):
        # Returns the path to the XML file as the request
        return "6-Adapter/data.xml"


# Analytic class that expects to receive data in JSON format.
class Analytic:
    def recieve_request(self, json):
        # Receives the converted JSON data and returns it
        return json


# Adapter class that acts as a bridge between Application and Analytic classes.
# It converts the XML data from Application to JSON format for Analytic.
class Adapter:
    def convert_xml_to_json(self, file):
        # Opens the XML file and reads its content
        with open(file, "r") as my_file:
            # Converts the XML data to a dictionary (JSON-like structure)
            obj = xmltodict.parse(my_file.read())
            return obj


# Client function that ties everything together using the Adapter pattern.
def client_adapter():
    # Create an Application instance and send a request (get XML file path)
    sender = Application().send_request()

    # Use the Adapter to convert the XML file to JSON format
    converted_data = Adapter().convert_xml_to_json(sender)

    # Create an Analytic instance and pass the converted JSON data
    receiver = Analytic().recieve_request(converted_data)

    # Print the received JSON data
    print(receiver)


# Run the client_adapter function to demonstrate the Adapter Design Pattern.
client_adapter()
# output: {'employees': {'employee': {'name': 'Sorena', 'role': 'Programmer', 'age': '27'}}}
