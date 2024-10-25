import pandas as pd

# Cargar el archivo de Excel
archivo_excel = 'CPdescarga.xls'

# Crear una lista para almacenar los pares (d_tipo_asenta, c_tipo_asenta)
tipos_asenta = []

# Leer todas las hojas del archivo
xls = pd.ExcelFile(archivo_excel)
for hoja in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=hoja)

    # Asegurarse de que las columnas existen
    if 'd_tipo_asenta' in df.columns and 'c_tipo_asenta' in df.columns:
        # Filtrar filas no nulas y agregar los pares a la lista
        for _, row in df[['d_tipo_asenta', 'c_tipo_asenta']].dropna().iterrows():
            tipos_asenta.append((row['d_tipo_asenta'], row['c_tipo_asenta']))

# Convertir a un conjunto para eliminar duplicados
tipos_asenta_unicos = set(tipos_asenta)

# Mostrar resultados
print("Valores únicos de d_tipo_asenta y c_tipo_asenta:")
for d, c in tipos_asenta_unicos:
    print(f"d_tipo_asenta: {d}, c_tipo_asenta: {c}")
