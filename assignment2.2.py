#1
def last (n):
    return n[-1]
def sort_list_last(tuples):
    return sorted(tuples, key=last)
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))
#or
tuple_list =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list_1 = []

new_list = [5,2,4,3,1]
for i in range(len(tuple_list)):
  list_1.append(list(tuple_list[i]))
  new_list.append(list_1[i][1])

new_list.sort()
new_list_output = []

for i in range(len(list_1)):
  for j in range(len(list_1)):
    if(new_list[i]==list_1[j][1]):
      new_list_output.append(list_1[j])

final_output = []
for i in range(len(new_list_output)):
  final_output.append(tuple(new_list_output[i]))

print(final_output)

#2q
d={}
def convert(x):
    y=x
    x=chr(x)
    d[x]=y  #adding keys n vales to empty dic


for i in range(97,123):
    convert(i)
print(d)  
