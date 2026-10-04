from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Stock Diario"

#Datos
datos = [
    ["SKU", "Producto", "Stock actual", "Stock minimo", "Precio unitaro"],
    ["BOD-101", "Cajas de Cartón M", 450, 500, 1.20],
    ["BOD-102", "Cinta Adhesiva", 15, 50, 0.80],
    ["BOD-103", "Pallets Madera", 120, 100, 15.50],
    ["BOD-104", "Plastico Burbuja", 8,20,12.00],
    ["BOD-105", "Etiquetas Frágil", 2000, 500, 0.5]
]
for fila in datos:
    ws.append(fila)

wb.save("inventario_bruto.xlsx")
print ("Archivo, 'inventario_bruto.xlsx' generado correctamente.")

