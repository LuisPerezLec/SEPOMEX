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
            sql = f"INSERT INTO asentamiento (nombre_asentamiento, codigo_asentamiento, zona, tipo_asentamiento, c_mnpio, c_estado, cve_ciudad) VALUES ('{d_asenta}', '{d_codigo}', '{d_zona}', '{c_tipo_asenta}', '{c_mnpio}', '{c_estado}', '{c_cve_ciudad}');"
            sql = f"INSERT INTO asentamiento (descripción_asentamiento, id_codigo, zona, tipo_asentamiento, c_mnpio, c_estado, cve_ciudad) VALUES ('{d_asenta}', (
                        SELECT id_codigo FROM codigo_postale WHERE id_municipio = (
                            SELECT id_municipio
                            FROM municipio
                            WHERE id_estado = (
                                SELECT id_estado
                                FROM estado
                                WHERE codigo_estado = '{c_estado}'
                            ) AND codigo_municipio = '{c_mnpio}'
                        ) AND codigo_codigo = '{d_codigo}'
                    ), '{d_zona}', '{c_tipo_asenta}', '{c_mnpio}', '{c_estado}', '{c_cve_ciudad}');"
            #INSERT INTO asentamiento (nombre_asentamiento, codigo_asentamiento, zona, tipo_asentamiento, c_mnpio, c_estado, cve_ciudad) VALUES ('Paseos de Santa Mónica', '20286', 'Urbano', '10', '1', '1', '1.0');
        else:
            sql = f"INSERT INTO asentamiento (nombre_asentamiento, codigo_asentamiento, zona, tipo_asentamiento, c_mnpio, c_estado, cve_ciudad) VALUES ('{d_asenta}', '{d_codigo}', '{d_zona}', '{c_tipo_asenta}', '{c_mnpio}', '{c_estado}', NULL);"
        
        file.write(sql + '\n')

print("Instrucciones de inserción generadas en 'inserciones_asentamientos.sql'")
