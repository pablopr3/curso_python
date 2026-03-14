# ==========================================
# PARTE 1: ¿QUÉ ES UNA VARIABLE? Y FORMAS DE IMPRIMIR
# ==========================================
nombre = 'David'
# Forma 1: Separando con comas (La clásica)
#print("El nombre en la caja es:", nombre)
# Forma 2: Usando f-strings (La moderna y recomendada)
# Ponemos una 'f' al principio y metemos la variable entre llaves {}
print(f"El nombre en la caja es: {nombre}")
print(type(nombre))
print("-" * 30)
# ==========================================
# PARTE 2: LOS OTROS TIPOS DE DATOS
# ==========================================
# Integer (Número entero)
edad = 25
print(f"Valor de edad: {edad} | Tipo: {type(edad)}")
# Float (Número decimal)
estatura = 1.75
print(f"Valor de estatura: {estatura} | Tipo: {type(estatura)}")
# Boolean (Verdadero o Falso - Recuerda la mayúscula inicial)
le_gusta_python = True
print(f"Valor de le_gusta_python: {le_gusta_python} | Tipo: {type(le_gusta_python)}")
print("-" * 30)
# ==========================================
# PARTE 3: TIPADO DINÁMICO (El superpoder de Python)
# ==========================================
caja_magica = "Ahora soy un texto"
# Aquí usamos la coma tradicional para ver la diferencia
print("Valor actual:", caja_magica)
print("Tipo actual:", type(caja_magica))
caja_magica = 100
print("Nuevo valor:", caja_magica)
print("Nuevo tipo:", type(caja_magica))
print("-" * 30)
# ==========================================
# PARTE 4: EL MICRÓFONO (INPUT) Y EL CASTING
# ==========================================
# Todo lo que entra por input() es texto (String) por defecto
edad_usuario = float(input("Dime tu edad "))
print(f"tu edad es {edad_usuario}")
print(f"Valor ingresado: {edad_usuario} | Tipo: {type(edad_usuario)}")
print("-" * 30)