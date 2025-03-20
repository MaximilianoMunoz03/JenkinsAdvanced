import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print("Resolviendo un sistema de ecuaciones lineales... ")

    # Definimos la matriz de coeficientes y un vector de términos independientes
    A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
    b = np.array([4, 1, 1])

    # Resolver el sistema Ax = b
    try:
        x = np.linalg.solve(A, b)
        print("La solución del sistema es: ")
        for i, valor in enumerate(x, start=1):
            print(f"x{i} = {valor:.4f}")
        return x
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución o tiene infinitas soluciones.")
        return None

def graficar_soluciones(soluciones):
    if soluciones is not None:
        print ("Generando Graficos de soluciones")

        # Crear un grafico de barras para visualizar las soluciones
        etiquetas = [f"x{i}" for i in range(1, len(soluciones) + 1)]
        plt.bar(etiquetas, soluciones, color= ['blue', 'green', 'red'] )
        plt.title("Soluciones del sistema de ecuaciones")
        plt.xlabel("Variables")
        plt.ylabel("Valores")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        # Guardar el grafico en un archivo
        plt.savefig("soluciones.png")
        plt.close()
        print("Grafico guardado en soluciones.png")
    else:
        print("No se pueden graficar las soluciones porque no hay solución.")

def guardar_soluciones_csv(soluciones):
    if soluciones is not None:
        print("Guardando las soluciones en un archivo CSV...")
        # Crear un archivo CSV y escribir las soluciones
        with open("soluciones.csv", mode="w", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(["Variable", "Valor"])
            for i, valor in enumerate(soluciones, start=1):
                escritor.writerow([f"x{i}", valor])
        print("Soluciones guardadas en soluciones.csv")
    else:
        print("No se pueden guardar las soluciones porque no hay solución.")

def main():
    print("=== Sistema de ecuaciones lineales ===")

    # Resolver el sistema de ecuaciones
    soluciones = resolver_sistema()
    # Graficar las soluciones
    graficar_soluciones(soluciones)
    # Guardar las soluciones en un archivo CSV
    guardar_soluciones_csv(soluciones)

if __name__ == "__main__":
    main()
