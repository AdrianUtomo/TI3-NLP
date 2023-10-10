import json

f = json.load(open('saltik_200.json'))

for i in f :
    print(f[i])
    break