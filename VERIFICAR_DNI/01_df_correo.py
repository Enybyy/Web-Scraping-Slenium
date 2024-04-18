import pandas as pd

# ABRIR EL Y LEER ARCHIVO .txt
with open('../ARCHIVOS_LOCALES/CORREO/datos_correo.txt', 'r', encoding='utf-8') as archivo:
    data_correo = archivo.read()

data_correo.strip()

# DIVIR DATOS CADA QUE HACE UN SALTO DE LINEA
data_split = data_correo.split('\n')

# CREAR DATAFRAME
df_correo = pd.DataFrame(
    [data_split[i:i+2] for i in range(0, len(data_split), 2)], columns=['NAME', 'ID'])

# APLICAR strip() A LAS COLUMNAS 'NAME' e 'ID'
df_correo = df_correo.applymap(
    lambda x: x.strip() if isinstance(x, str) else x)

df_correo.to_csv(
    "C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name1.csv", index=False, sep=',')
print(df_correo)
