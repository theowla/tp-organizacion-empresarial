import csv #terminar el grafico ig
import matplotlib.pyplot as plt
import os

ventas_totales = 0
productos = {}
ventas_mes = {}

with open("datos/dataset.csv", "r") as archivo:
  reader = csv.DictReader(archivo)

  for fila in reader:
    producto = fila["Product Name"]
    cantidad = int(fila["Units Sold"])
    precio = float(fila["Unit Price"])
    fecha = fila["Date"]

    venta = cantidad * precio
    ventas_totales += venta

    if producto in productos:
      productos[producto] += cantidad
    else:
      productos[producto] = cantidad

    mes = fecha[:7]

    if mes in ventas_mes:
      ventas_mes[mes] += venta
    else:
      ventas_mes[mes] = venta

producto_mas_vendido = max(productos, key=productos.get)

#resultados
print(f"Ventas totales: ${ventas_totales:.2f}")
print(f"Producto mas vendido: {producto_mas_vendido}")
print("Ventas por mes:")

for mes in ventas_mes:
  print(f"{mes}: ${ventas_mes[mes]:.2f}")

#grafico

meses = list(ventas_mes.keys())
ventas = list(ventas_mes.values())

plt.figure(figsize=(10, 5))
plt.plot(meses, ventas, marker='o', color='purple')
plt.title("Evolucion Mensual de Ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar obligatoriamente en la carpeta resultados antes de mostrarlo
os.makedirs("resultados", exist_ok=True)
plt.savefig("resultados/evolucion_ventas.png")
plt.close()
print("Grafico exportado exitosamente en: resultados/evolucion_ventas.png")
