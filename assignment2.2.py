d={}
def convert(x):
    y=x
    x=chr(x)
    d[x]=y  #adding keys n vales to empty dic


for i in range(97,123):
    convert(i)
print(d)  
