doors = ['close']*100
for i in range(1,101):
    for item in range(i-1,100,i):
        if doors[item] == 'close':
            doors[item] = 'open'
        else:
            doors[item] = 'close'
open_doors = []
for item in range(0,100):
    if doors[item] =="open":
        open_doors.append(item+1)
print('The following doors are open: ', open_doors)
