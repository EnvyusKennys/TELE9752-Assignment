import json
import xmltodict

with open("sandbox-iosxr-1.cisco.com.xml") as xml_file:

    json_data = json.dumps(xmltodict.parse(xml_file.read()))

    with open("sandbox-iosxr-1.cisco.com.json", "w") as json_file:
        json_file.write(json_data)
