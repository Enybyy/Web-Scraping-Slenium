## Código Destacado

Aquí se presentan algunas secciones clave del código para entender mejor cómo funciona el proyecto.

### 01_df_correo.py

```python
# Leer el archivo de texto y dividir los datos en líneas
with open('../ARCHIVOS_LOCALES/CORREO/datos_correo.txt', 'r', encoding='utf-8') as archivo:
    data_correo = archivo.read()
data_split = data_correo.split('\n')

# Crear un DataFrame a partir de los datos
df_correo = pd.DataFrame(
    [data_split[i:i+2] for i in range(0, len(data_split), 2)], columns=['NAME', 'ID'])
```

**Explicación**: Este fragmento lee un archivo de texto, lo divide en líneas y organiza los datos en un DataFrame con columnas 'NAME' e 'ID'.

### 02_xtraer_data_dni.py

```python
# Buscar elementos en la página web utilizando Selenium
ipt_dni = wait.until(
    EC.visibility_of_element_located(('xpath', '//input[@type="number" and @name="dni"]')))
btn_buscar = wait.until(
    EC.visibility_of_element_located(('xpath', '//button[@class="btn btn-primary mb-3"]')))
```

**Explicación**: Aquí se utilizan `Selenium` y `WebDriverWait` para esperar a que aparezcan los campos de entrada y el botón en la página web antes de interactuar con ellos.

```python
# Extraer nombres y apellidos de la página
nombres = driver.find_elements(by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[2]/td[2]')
apellido = driver.find_elements(by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[3]/td[2]')
```

**Explicación**: Este código extrae nombres y apellidos de la página web utilizando `find_elements` con `Selenium`.

### 03_comparar_data.py

```python
# Comparar los datos y devolver solo los datos que no coinciden
datos_inconsistentes = pd.merge(
    df_dni_name, df_dni_name_01, how='outer', indicator=True)
datos_inconsistentes = datos_inconsistentes[datos_inconsistentes['_merge'] == 'right_only'].drop('_merge', axis=1)
```

**Explicación**: Utiliza `pandas` para comparar los DataFrames y encontrar datos que están presentes solo en el archivo más reciente, indicando posibles discrepancias.

### F_verificar_dni_0.1.py (Prueba)

```python
# Intentar conectar con la página web y obtener el HTML
response = requests.get(url, headers=headers)
```

**Explicación**: Este fragmento usa `requests` para realizar una solicitud HTTP y obtener el HTML de la página web para análisis.

```python
# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html_pagina_web, 'html.parser')
input_dni = soup.find('input', {'id': 'dni'})
```

**Explicación**: Usa `BeautifulSoup` para analizar el HTML y buscar elementos específicos en la página web.
