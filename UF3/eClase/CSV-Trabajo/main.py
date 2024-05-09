import pandas as pd

CSV = 'data.csv'

# Declaramos data set
#  Indicamos el indice que utilizamos
#   numero de columna o
#   ["nombre"]
df = pd.read_csv(CSV, index_col=0)

# Printamos las n primeras lineas
#print(df.head())

dict = df.to_dict()

# Printar columnas
for col in dict:
    print(col, end=' ')
print()

# Obtener edad media
a = 0
for i in dict['edad']:
    a += dict['edad'][i]
m = a / df.shape[0]
print(m)

# Simplificado
print(df['edad'].mean())

# Obtener aceptados de cada carrera
d = {}
for i in dict['acepta']:
    if dict['acepta'][i] == 'Si':
        if dict['carrera'][i] not in d:
            d[dict['carrera'][i]] = 1
        else:
            d[dict['carrera'][i]] += 1
print(d)

"""
# 3. Calcular el total de ventas
df['Total'] = df['Cantidad'] * df['Precio_unitario']
total_ventas = df['Total'].sum()
print("Total de ventas:", total_ventas)

# 4. Encontrar el producto más vendido
producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum().idxmax()
print("Producto más vendido:", producto_mas_vendido)
"""