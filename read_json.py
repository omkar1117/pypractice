import json

f = open("test_data.json")
data = json.load(f)
print(data)

f.close()

# Read Str

f = open("test_data_str.json")
d = f.read()
print("Test::", d[1:-1])

data = json.dumps(d)
print(data)

f.close()
