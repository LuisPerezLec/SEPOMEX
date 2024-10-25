import pandas as pd

# Cargar el archivo de Excel
archivo_excel = 'CPdescarga.xls'

# Crear una lista para almacenar los resultados
municipios = []

# Leer todas las hojas del archivo
xls = pd.ExcelFile(archivo_excel)
for hoja in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=hoja)

    # Asegurarse de que las columnas existen
    if 'D_mnpio' in df.columns and 'c_mnpio' in df.columns and 'c_estado' in df.columns:
        # Filtrar filas no nulas y agregar los pares a la lista
        for _, row in df[['D_mnpio', 'c_mnpio', 'c_estado']].dropna().iterrows():
            valor_municipio = (row['D_mnpio'], row['c_mnpio'], row['c_estado'])
            if valor_municipio not in municipios:
                municipios.append(valor_municipio)

# Ordenar la lista primero por c_estado y luego por c_mnpio
municipios_ordenados = sorted(municipios, key=lambda x: (x[2], x[1]))

# Escribir en un archivo .sql
with open('inserciones_municipios.sql', 'w') as file:
    for d_mpio, c_mnpio, c_estado in municipios_ordenados:
        # Generar la instrucción SQL
        sql = f"INSERT INTO municipio (codigo_municipio, descripcion_municipio, id_estado) VALUES ('{c_mnpio}', '{d_mpio}', (SELECT id_estado FROM estado WHERE codigo_estado = '{c_estado}'));"
        file.write(sql + '\n')

print("Instrucciones de inserción generadas en 'inserciones_municipios.sql'")
