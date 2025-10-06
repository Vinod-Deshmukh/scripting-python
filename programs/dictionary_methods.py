#Dictionary Methods in Python.
data={'a':1,'b':2,'c':3,'d':4}
#get() safely get value
print(data.get('b'))
print(data.get('x'))
#keys() get all keys
dict_keys=data.keys()
print(dict_keys)
#values() get all values
dict_vlaues=data.values()
print(dict_vlaues)
#items() get key value pair
dict_items=data.items()
print(dict_items)
#update() merge another dictionary
data.update({'e':5})
print(data)
#pop() remove by key
data.pop('b')
print(data)
#popitem() remove last inserted pair
data.popitem()
print(data)
#clear() remove all the items
# data.clear()
# print(data)
# setdefalut() get values or set if not present
data.setdefault('f',0)
#adds 'f':0 if not present
print(data)
#fromkeys() create dictionary from keys
data_new=dict.fromkeys(['x','y'],0)
print(data_new)