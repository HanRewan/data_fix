import pandas as pd

data=[]
delta=[]

def get_data(name):
    data.append(name)

def getdelta():
    for i in range(len(data)//4):
        j=(i)*4
        if(data[j + 0] != '' and data[j + 1] != ''):
            delta.append(float(data[j + 0]) - float(data[j + 1]))
        #else: delta.append('')
        if (data[j + 2] != '' and data[j + 3] != ''):
            delta.append(float(data[j + 2]) - float(data[j + 3]))
        # else: delta.append('')

df = pd.read_csv('data/cgo_20_2021-06-13.csv', converters={'Діоксид сірки':get_data})

getdelta()

print(data)
print(delta)
