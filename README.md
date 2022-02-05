Library
-----------------------------------
This is a library where you store/retrieve arbitrary data in multiple formats & destinations. 
Destination and file-format are specified in the .env file.
This library supports 2 types of file formats JSON/XML and multiple operations: Add/ Delete/ Update/ Get a Record,
Insert Batch Records & Query records from the file by specifying limit and offset.

Configuration File
.env is the configuration file where you choose where you want to store the records and in which format
DESTINATION_PATH = “example”
FILE FORMAT = “JSON”

How does this work?
-----------------------------------

- Method create(key, value)

  Create Method where you pass two arguments “key”, “value”

  Lib.create(key, value)
---

- Method update(key)
  
  Update Record pass the key of the record you want to update and new_value as arguments
  
  Lib.update(key, new_value)
---
- Method delete(key)
  
  Delete Method where you pass the key of the record you want to delete as argument
  
  Lib.delete(key)
---
- Method getOneRecord(key)

  GetOneRecord where you pass the key of the record as argument

  Lib.getOneRecord
---
- Method batch_insert(list)

  Batch_Insert where you pass “key”:”values” as dictionary as argument 
  Lib.batch_inset( {“key1”:”value1”, “key2”:”value2”})

---
- Method queryFilter(offset = 0, limit =0)

  When we want to get records with offset and limit,
  searches for the records after the offset and limit is set and show in terminal with print(). 

  Lib.queryFilter(offset, limit)

---
Packages installed
-----------------------------------
- Dotenv 

In the .env we set path of file that user uploaded PATH_USER, and the path destination PATH_DESTINATION
 
- Dicttoxml
 
Converts a Python dictionary or other native data type into a valid XML string.
 
- Xmltodict

Converts a XML string to a Python dictionary.

- Json

