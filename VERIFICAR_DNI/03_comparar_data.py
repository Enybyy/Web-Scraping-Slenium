import pandas as pd

df_dni_name = pd.read_csv(
    'C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name1.csv')
df_dni_name_01 = pd.read_csv(
    'C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name2.csv')

# COMPARAR DATOS Y DEVOLVER SOLO LOS DATOS QUE NO COINCIDEN
datos_inconsistentes = pd.merge(
    df_dni_name, df_dni_name_01, how='outer', indicator=True)
datos_inconsistentes = datos_inconsistentes[datos_inconsistentes['_merge'] == 'right_only'].drop(
    '_merge', axis=1)
# REINICIAR INDEX
datos_inconsistentes = datos_inconsistentes.reset_index(drop=True)
print(datos_inconsistentes.to_markdown())
