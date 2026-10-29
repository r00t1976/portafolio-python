""" genera codogo para ganar el kino
con esto  me  ganare el cielo
""" 

import random

# debe generar numeros entre el 1 al 25

def generar_numeros_ganadores():
    return sorted(random.sample(range(1, 26),14))
    
numeros_ganadores = generar_numeros_ganadores()
print("Números ganadores:", numeros_ganadores)
