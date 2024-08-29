# Verificación Automatizada de DNIs

Este proyecto automatiza la verificación de identidades a través de un sistema de web scraping, utilizando Python y diversas bibliotecas. A continuación, se describe en detalle cada componente del sistema y su función.

## Descripción

El sistema consta de cuatro scripts que trabajan en conjunto para verificar identidades mediante números de DNI:

1. **Extracción y Formateo de Datos**
2. **Recuperación de Información desde la Web**
3. **Comparación de Datos**
4. **Intento de Verificación Alternativa**

### 1. Extracción y Formateo de Datos

**Script: `01_df_correo.py`**

Este script procesa un archivo de texto con datos de nombres e IDs y los convierte en un DataFrame de pandas. Las operaciones clave incluyen:

- **Creación del DataFrame**: Convierte los pares de datos en un DataFrame, aplicando `strip()` para limpiar los datos.

  ```
  df_correo = pd.DataFrame(
      [data_split[i:i+2] for i in range(0, len(data_split), 2)], columns=['NAME', 'ID'])
  df_correo = df_correo.applymap(lambda x: x.strip() if isinstance(x, str) else x)
  ```

- **Exportación a CSV**: Guarda el DataFrame limpio en un archivo CSV para su posterior uso.

  ```
  df_correo.to_csv("C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name1.csv", index=False, sep=',')
  ```

### 2. Recuperación de Información desde la Web

**Script: `02_xtraer_data_dni.py`**

Este script utiliza Selenium para automatizar la interacción con la página web de verificación de DNI. Las partes destacadas son:

- **Interacción con la Web**: Ingresa el DNI en un campo de texto y hace clic en el botón de búsqueda.

  ```
  ipt_dni.send_keys(dni)
  btn_buscar.click()
  ```

- **Extracción de Datos**: Recoge los nombres y apellidos desde la página web, asegurando que se manejen adecuadamente los elementos web.

  ```
  nombres = driver.find_elements(by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[2]/td[2]')
  apellido = driver.find_elements(by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[3]/td[2]')
  apellido01 = driver.find_elements(by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[4]/td[2]')
  
  apellido_nombres = []
  for nombre_element in apellido:
      apellido_nombres.append(nombre_element.text.strip())
  for apellido_element in apellido01:
      apellido_nombres.append(apellido_element.text.strip())
  for apellido01_element in nombres:
      apellido_nombres.append(apellido01_element.text.strip())
  
  df_apellido_nombres = ' '.join(apellido_nombres)
  lista_fullname.append(df_apellido_nombres)
  ipt_dni.clear()
  ```

- **Guardar Resultados**: Exporta los datos recuperados en un nuevo archivo CSV.

  ```
  df_dni_name2 = pd.DataFrame({'NAME': lista_fullname, 'ID': lista_dni})
  df_dni_name2.to_csv("C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name2.csv", index=False)
  ```

### 3. Comparación de Datos

**Script: `03_comparar_data.py`**

Este script compara los datos originales con los datos recuperados para identificar cualquier discrepancia. Los pasos esenciales son:

- **Comparación de Datos**: Usa una unión externa para encontrar las diferencias entre los dos conjuntos de datos.

  ```
  datos_inconsistentes = pd.merge(df_dni_name, df_dni_name_01, how='outer', indicator=True)
  datos_inconsistentes = datos_inconsistentes[datos_inconsistentes['_merge'] == 'right_only'].drop('_merge', axis=1)
  ```

- **Mostrar Resultados**: Imprime las discrepancias en un formato legible.

  ```
  print(datos_inconsistentes.to_markdown())
  ```

### 4. Intento de Verificación Alternativa

**Script: `F_verificar_dni_0.1.py`**

Este script fue una prueba para interactuar con la página web utilizando BeautifulSoup para el análisis del HTML. Aunque no se concretó, sirvió como base para la integración de la verificación alternativa.

- **Conexión a la Página Web**: Intenta conectarse a la página web para analizar el HTML.

  ```
  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
  }
  response = requests.get(url, headers=headers)
  ```

## Licencia

Este proyecto está bajo la **Licencia NMS (No Modificar y Compartir)**. Esto significa que el código no puede ser utilizado, modificado ni compartido sin mi consentimiento expreso. Cualquier uso del código sin autorización está prohibido.
