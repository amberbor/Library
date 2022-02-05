from main import Solution as Lib

# test Create

Lib().create("RR", "Boricej")

# test Update

Lib().update("RR", "Myslym Shyri")

# test GetOneRecord Method

data = Lib().getOneRecord("name")
print(data)

# test delete Method

Lib().delete("RR")

# test batch_insert Method

Lib().batch_insert({'key1': 'value1', 'key2': 'value2'})

# test queryfilters Method

data = Lib().queryFilter(2, 4)
print(data)
