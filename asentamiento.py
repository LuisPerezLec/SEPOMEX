import pandas as pd

# Cargar el archivo de Excel
archivo_excel = 'CPdescarga.xls'

# Crear una lista para almacenar los resultados
asentamientos = []

# Leer todas las hojas del archivo
xls = pd.ExcelFile(archivo_excel)
for hoja in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=hoja)

    # Asegurarse de que las columnas existen
    if all(col in df.columns for col in ['d_asenta', 'd_codigo', 'd_zona', 'c_tipo_asenta', 'c_mnpio', 'c_estado', 'c_cve_ciudad']):
        # Filtrar filas no nulas y agregar los pares a la lista
        for _, row in df[['d_asenta', 'd_codigo', 'd_zona', 'c_tipo_asenta', 'c_mnpio', 'c_estado', 'c_cve_ciudad']].dropna().iterrows():
            valor_asentamiento = (
                row['d_asenta'], 
                row['d_codigo'], 
                row['d_zona'], 
                row['c_tipo_asenta'], 
                row['c_mnpio'], 
                row['c_estado'], 
                row.get('c_cve_ciudad', None)  # Usar None si c_cve_ciudad no está
            )
            asentamientos.append(valor_asentamiento)

# Escribir en un archivo .sql
with open('inserciones_asentamientos.sql', 'w') as file:
    for d_asenta, d_codigo, d_zona, c_tipo_asenta, c_mnpio, c_estado, c_cve_ciudad in asentamientos:
        # Generar la instrucción SQL
        if c_cve_ciudad:
            sql = f"""INSERT INTO asentamiento (descripcion_asentamiento, id_codigo, id_zona, id_tipo_asenta, id_ciudad) VALUES ('{d_asenta}', (
                        SELECT id_codigo FROM codigo_postal WHERE codigo_codigo = '{d_codigo}'
                    ),
                    (
                        SELECT id_zona FROM zona WHERE descripcion_zona = '{d_zona}'
                    ),
                    (
                        SELECT id_tipo_asenta FROM tipo_asentamiento WHERE codigo_tipo_asenta = '{c_tipo_asenta}'
                    ),
                    (
                        SELECT id_ciudad FROM ciudad WHERE codigo_cve_ciudad = '{c_cve_ciudad}' AND id_estado = (SELECT id_estado FROM estado WHERE codigo_estado = '{c_estado}')
                    ));"""
        else:
            sql = f"""INSERT INTO asentamiento (descripcion_asentamiento, id_codigo, id_zona, id_tipo_asentamiento) VALUES ('{d_asenta}', (
                        SELECT id_codigo FROM codigo_postal WHERE codigo_codigo = '{d_codigo}'
                    ), 
                    (
                        SELECT id_zona FROM zona WHERE descripcion_zona = '{d_zona}'
                    ), (
                        SELECT id_tipo_asentamiento FROM tipo_asentamiento WHERE codigo_tipo_asenta = '{c_tipo_asenta}'
                    ));"""
        file.write(sql + '\n')

print("Instrucciones de inserción generadas en 'inserciones_asentamientos.sql'")
