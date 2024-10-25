import pandas as pd

# Cargar el archivo de Excel
archivo_excel = 'CPdescarga.xls'

# Crear una lista para almacenar los resultados
ciudades = []

# Leer todas las hojas del archivo
xls = pd.ExcelFile(archivo_excel)
for hoja in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=hoja)

    # Asegurarse de que las columnas existen
    if 'd_ciudad' in df.columns and 'c_cve_ciudad' in df.columns and 'c_estado' in df.columns:
        # Filtrar filas no nulas y agregar los pares a la lista
        for _, row in df[['d_ciudad', 'c_cve_ciudad', 'c_estado']].dropna().iterrows():
            valor_ciudad = (row['d_ciudad'], row['c_cve_ciudad'], row['c_estado'])
            if valor_ciudad not in ciudades:
                ciudades.append(valor_ciudad)

# Ordenar la lista por c_estado y luego por c_cve_ciudad
ciudades_ordenadas = sorted(ciudades, key=lambda x: (x[2], x[1]))

# Escribir en un archivo .sql
with open('inserciones_ciudades.sql', 'w') as file:
    for d_ciudad, c_cve_ciudad, c_estado in ciudades_ordenadas:
        # Generar la instrucción SQL
        sql = f"INSERT INTO ciudad (codigo_cve_ciudad, descripcion_ciudad, id_estado) VALUES ('{c_cve_ciudad}', '{d_ciudad}', (SELECT id_estado FROM estado WHERE codigo_estado = '{c_estado}'));"
        file.write(sql + '\n')

print("Instrucciones de inserción generadas en 'inserciones_ciudades.sql'")
