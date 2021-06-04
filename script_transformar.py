import pandas as pd

data = pd.read_csv("inicial.csv")

grupo_si_no = ['s101p11','s101p12a','s101p12b','s101p12c','s101p12d','s101p12e', 's101p61', 's101p62', 's101p63', 's101p64',
               's101p65', 's101p66', 's101p67', 's101p68', 's101p71', 's101p72', 's101p73', 's101p74', 's101p75', 's101p76',
               's101p77', 's101p121', 's101p122', 's101p123', 's101p124', 's101p125', 's101p126', 's101p141', 's101p142', 
               's101p143', 's101p144']
grupo_cantidad = ['s101p3a', 's101p3b', 's101p4a', 's101p4b', 's101p4b1']
grupo_likert = ['s101p13', 's101p171', 's101p172', 's101p173', 's101p174', 's101p175', 's101p176', 's101p181', 's101p182', 
                's101p183']
grupo_likert_inversa = ['s101p176', 's101p181']
grupo_desecho_residuos = ['s101p2a','s101p2b', 's101p2c', 's101p2d', 's101p2e', 's101p2f', 's101p5a','s101p5b', 's101p5c', 
                          's101p5d', 's101p5e', 's101p5f','s101p5g']

max_i = len(data['area'])
table = {}

# Mientras menor sea el valor de una variable mas contribuye al medio ambiente

for columna in data:

    table[columna] = []

    for i in range(max_i):

        if(columna in grupo_si_no):
            if(int(data[columna][i]) == 2):
                table[columna].append(1) # No
            elif(int(data[columna][i]) == 3): # Casos no aplica
                table[columna].append(0.5) # Punto medio, no se sabe nada
            else:
                table[columna].append(0) # Si

        elif(columna in grupo_cantidad):
            if(columna == 's101p3a' or columna == 's101p4a'):
                table[columna].append(int(data[columna][i]))
            elif(columna == 's101p3b'):
                table[columna].append(int(data['s101p3a'][i]) - int(data[columna][i])) # Diferencia entre pilas y pilas recargables
            elif(columna == 's101p4b'):
                table[columna].append(int(data['s101p4a'][i]) - int(data[columna][i])) # Diferencia entre focos y focos ahorradores
            elif(columna == 's101p4b1'):
                table[columna].append(int(data['s101p4b'][i]) - int(data[columna][i])) # Diferencia entre focos ahorradores simples y focos ahorradores LED¨

        elif(columna in grupo_likert):
            if(int(data[columna][i]) == 99): # Casos no responde / no sabe
                table[columna].append(3) # Se le pone ni en acuerdo ni en desacuerdo
            else:
                if(columna not in grupo_likert_inversa): # Invertir escala de Likert
                    if(int(data[columna][i]) == 1):
                        table[columna].append(5)
                    elif(int(data[columna][i]) == 2):
                        table[columna].append(4)
                    elif(int(data[columna][i]) == 3):
                        table[columna].append(3)
                    elif(int(data[columna][i]) == 4):
                        table[columna].append(2)
                    else:  
                        table[columna].append(1)
                else: # Escala de Likert ya invertida
                    table[columna].append(int(data[columna][i]))
                
        elif(columna in grupo_desecho_residuos): # Escala de practicas de desechos de resiudos
            if(int(data[columna][i]) == 1):
                table[columna].append(3)
            elif(int(data[columna][i]) == 2):
                table[columna].append(4)
            elif(int(data[columna][i]) == 3):
                table[columna].append(6)
            elif(int(data[columna][i]) == 4):
                table[columna].append(7)
            elif(int(data[columna][i]) == 6):
                table[columna].append(2)
            elif(int(data[columna][i]) == 7):
                table[columna].append(5)
            else: 
                table[columna].append(1)

        else:
            table[columna].append(str(data[columna][i]))   

table = pd.DataFrame(table)
table.to_csv('transformada2.csv', header=True, index=True)
