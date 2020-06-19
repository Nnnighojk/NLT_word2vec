l = []
a = []
analogy_list = ['king', 'man', 'queen', 'woman',
                 'bird','wing','tiger', 'feet',
                  'sun', 'tree', 'meat', 'lion',
                  'dog', 'nose', 'eagle','eye',
                   'foot', 'run', 'eye' , 'see',
                    'sword', 'attack','shield', 'defend',
                    'good', 'bad', 'up', 'down',
                    'good', 'bad', 'left', 'right',
                    'up', 'down', 'good', 'bad',
                    'good', 'bad', 'right', 'wrong',
                    'many', 'little', 'wet', 'dry',
                    'many', 'little', 'hot', 'cold',
                    'heavy', 'light', 'high', 'short',
                    'high', 'short','long' , 'short',
                    'big', 'small', 'clever', 'fool',
                    'strong', 'weak', 'advantage', 'disavantage',
                    'strong', 'weak', 'fast', 'slow',
                    'weapon', 'damage', 'medicine', 'heal',
                    'old', 'young', 'destroy', 'create'

                ]
for k in analogy_list:
    a.append(k)

#print (len(a))

with open('analogy_data_set.rtf', 'r') as fh:
    word = fh.readlines()
    for i in word:
        element = i.split()
        stuff = (element[3].split('\\'))
        element [3] = stuff[0]
        for j in element:
            l.append(j)
print (len(l))

final_list = a + l
#print(final_list[1000])
#str1 = ''.join(final_list)
print (len(final_list))

#writing into a file
#with open("file.txt", "w") as output:
#    output.write(str(final_list))