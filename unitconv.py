parts = ('convert 35 m/s to mi/h').split(' ')
num = int(parts[1])
unit_from = parts[2]
unit_to = parts[4]
temp = ['c','f','k']
dist = ['m','km','cm','in','ft','yd','mi']
speed = ['m/s','km/h','mi/h']

if unit_to in temp:  
    if unit_from == 'k':
        num = num - 273.15
    if unit_from == 'f':
        num  = (num - 32)*(5/9)
        
    if unit_to == 'f':
        num = (num * (9/5))+32
    if unit_to == 'k':
        num += 273.15
        
if unit_to in dist:
    if unit_from == 'km':
        num *= 1000
    elif unit_from == 'cm':
        num /= 100
    elif unit_from == 'in':
        num /= 39.37
    elif unit_from == 'ft':
        num /=  3.281
    elif unit_from == 'yd':
        num /=  1.094
    elif unit_from == 'mi':
        num *= 1609

    if unit_to == 'km':
        num /= 1000
    elif unit_to == 'cm':
        num *= 100
    elif unit_to == 'in':
        num *= 39.37
    elif unit_to == 'ft':
        num *=  3.281
    elif unit_to == 'yd':
        num *=  1.094
    elif unit_to == 'mi':
        num /= 1609

if unit_to in speed:
    if unit_from == 'km/h':
        num /= 3.6
    elif unit_from == 'mi/h':
        num /=  2.237
    
    if unit_to == 'km/h':
        num *= 3.6
    elif unit_to == 'mi/h':
        num *=  2.237
    
print(num)