
def saludar_usuarios(nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")
        print("Preparando el entorno...")

usuarios = ["Alex", "Maria", "Dani"]
saludar_usuarios(usuarios)