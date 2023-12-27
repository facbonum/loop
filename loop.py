'''
i = 0

while i < 5:
    print(i)
    i += 1
'''
'''
i = 0

while i < 5: # is 0 less than 5?
    i += 1   # ok, increment by 1
    if i == 3: # but is i equal to 3?
        continue # re-run while script from the top
    
    print(i)  # if i is not equal to 3, print i
    # 5 will be printed because i is incremented before printing
'''
'''
usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']


for usuario in usuarios:
    print(usuario)
'''
'''
Chanchito feliz
felipe
roberto
nicolas
'''

'''
usuario = 'Chanchito Feliz'

for c in usuario:
    print(c)
'''
'''
Saldrá en forma vertical como tal:
C
h
a
n
c
h
i
t
o
 
F
e
l
i
z
'''
'''usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']


for usuario in usuarios:
    if usuario == 'roberto':
        continue # continue skips condition, and continues iteration
    print(usuario)

'''

""" for x in range(1,28,5): # most basic range loop: range(min, max, # to skip)
    x+=2
    print(x)
else:
    print('Hemos terminado!')
 """

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']
edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)