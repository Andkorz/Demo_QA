data1 = ['Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General']
data2 = ['angular', 'veu', 'office', 'public', 'private', 'classified', 'general']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(data2)

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()

assert data1 == data2