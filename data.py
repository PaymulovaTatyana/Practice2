rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},'job': ['dev', 'mgr'],'age': 25}
print(rec['name'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('anitor')
print(rec)