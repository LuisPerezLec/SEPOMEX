import pandas as pd

# Cargar el archivo de Excel
archivo_excel = 'CPdescarga.xls'

# Crear una lista para almacenar los resultados
codigos = []

# Leer todas las hojas del archivo
xls = pd.ExcelFile(archivo_excel)
for hoja in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=hoja)

    # Asegurarse de que las columnas existen
    if 'd_codigo' in df.columns and 'c_estado' in df.columns and 'c_mnpio' in df.columns:
        # Filtrar filas no nulas y agregar los pares a la lista
        for _, row in df[['d_codigo', 'c_estado', 'c_mnpio']].dropna().iterrows():
            valor_codigo = (row['d_codigo'], row['c_estado'], row['c_mnpio'])
            if valor_codigo not in codigos:
                codigos.append(valor_codigo)

# Ordenar la lista por d_codigo
codigos_ordenados = sorted(codigos, key=lambda x: x[0])

# Escribir en un archivo .sql
with open('inserciones_codigos.sql', 'w') as file:
    for d_codigo, c_estado, c_mnpio in codigos_ordenados:
        # Generar la instrucción SQL
        sql = f"INSERT INTO codigo_postal (codigo_codigo, id_municipio) VALUES ('{d_codigo}', (SELECT id_municipio FROM municipio WHERE codigo_municipio = '{c_mnpio}' AND id_estado = (SELECT id_estado FROM estado WHERE codigo_estado = '{c_estado}')));"
        file.write(sql + '\n')

print("Instrucciones de inserción generadas en 'inserciones_codigos.sql'")
