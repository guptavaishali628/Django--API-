import json

py_data={
    'active1':True,
    'active2':False,
    'active3':None,
}
# converting it into json data

jsn_data=json.dumps(py_data)
print(jsn_data)
print(type(jsn_data))   # datatype--> string


# converting it into python data
j_data='''{
    "active1":true,
    "active2":false,
    "active3":null
}'''

p_data=json.loads(j_data)
print(p_data)
print(type(p_data))