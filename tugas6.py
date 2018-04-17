def sf():
    print("modul dictionary")
    
no_telpon={"nama" : ["Jane Doe", "Jhon Smith", "Bob Stone"],"Telephone Number" : ["+27 555 5367", "+27 555 6254", "+27 555 5689"]}
>>> no_telpon["Telephone Number"][0] = "+27 555 1024"
>>> no_telpon
{'nama': ['Jane Doe', 'Jhon Smith', 'Bob Stone'], 'Telephone Number': ['+27 555 1024', '+27 555 6254', '+27 555 5689']}
>>> no_telpon.update({ "nama": ["Jane Doe", "Jhon Smith", "Bob Stone", "Anna Cooper"], "Telephone Number": ["+27 555 1024", "+27 555 6254", "+27 555 5689", "+27 555 3237"]})
>>> no_telpon
{'nama': ['Jane Doe', 'Jhon Smith', 'Bob Stone', 'Anna Cooper'], 'Telephone Number': ['+27 555 1024', '+27 555 6254', '+27 555 5689', '+27 555 3237']}
>>> no_telpon["Telephone Number"][2]
'+27 555 5689'
>>> no_telpon.keys()
['nama', 'Telephone Number']
>>> no_telpon.values()
[['Jane Doe', 'Jhon Smith', 'Bob Stone', 'Anna Cooper'], ['+27 555 1024', '+27 555 6254', '+27 555 5689', '+27 555 3237']]
>>> 
