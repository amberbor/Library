import os
from itertools import islice

import xmltodict as xmltodict
from dicttoxml import dicttoxml
from dotenv import load_dotenv
import json

# Load .env PATH
load_dotenv()
PATH_DESTINATION = os.getenv(r"PATH_DESTINATION")

class Solution:
    def __init__(self):
        self.file_format = os.getenv("FILE_FORMAT")
        self.path = PATH_DESTINATION
        # self.destination =  os.getenv('PATH_DESTINATION')
        self.parse_destination()

    def parse_destination(self):
        #Check if the destination file is JSON or XML
        #Parse files from Json
        if self.path.endswith(".json"):
            with open(self.path) as json_file:
                #print(self.destination)
                data_destination = json.load(json_file)
                return data_destination

        # Parse file from XML
        elif self.path.endswith(".xml"):
            with open(self.path, 'r') as xml_file:
                x = xml_file.read()
                data = xmltodict.parse(x, xml_attribs=True)
                data_destination = data['root']
                return data_destination
        else:
            raise ValueError("The file is not json nor xml or wrong destination")

    #Method to Create one record {"key" : "value"}
    def create(self, key, value):
        data = self.parse_destination()

        if key not in data:
            data[key] = value
        else:
            raise KeyError("You have one key with key name", key)

        # Save our changes to file
        Solution.saveFile(self, data)

    #Method to Insert list of record {"key1" : "value1", "key2" : "value2"}
    def batch_insert(self, data_list):
        data = self.parse_destination()
        for key, value in data_list.items():
            if key not in data:
                data.update({key: value})
        Solution.saveFile(self, data)

    #Method to get one record searching by Key from the destination
    def getOneRecord(self, key):
        data = self.parse_destination()
        if key in data:
            return data.get(key)
        else:
            raise KeyError("You dont have a record with name", key)

    #Method to update the record in destination
    def update(self, key, value):
        data = self.parse_destination()
        if key in data:
            data.update({key: value})
        else:
            raise KeyError("The key its not found in file")
        Solution.saveFile(self, data)

    #Method to delete one record through key
    def delete(self, key):
        data = self.parse_destination()
        if key in data:
            data.pop(key)
        else:
            raise KeyError("You dont have a key with name", key)

        Solution.saveFile(self, data)

    #Filter by offset
    def queryFilter(self, offset=None, limit = None):
        data = self.parse_destination()
        return dict(list(islice(islice(data.items(), offset, None), limit)))

    #Method to save file into the destination
    def saveFile(self, data):
        if self.file_format == "JSON":
            file_path_save = self.path
            jsonFile = open(file_path_save, "w")
            jsonFile.write(json.dumps(data))
            jsonFile.close()
        elif self.file_format == "XML":
            xml_data = dicttoxml(data)
            file_path_save = self.path
            xmlFile = open(file_path_save, "w+")
            xmlFile.write(xml_data.decode())
            xmlFile.close()
        else:
            print('Please enter destination file_format')


if __name__ == '__main__':

    db = Solution()
    # db.create("home", "12")