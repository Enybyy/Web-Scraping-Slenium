# Verificación de Identidad a través de Web Scraping

Este proyecto tiene como objetivo verificar la identidad de personas utilizando técnicas de web scraping. Incluye scripts para leer datos, extraer información de una página web y comparar resultados para detectar inconsistencias.

## Requerimientos

Para ejecutar este proyecto, necesitarás instalar las siguientes bibliotecas de Python:

- **`pandas`**: Para manipulación y análisis de datos en estructuras de datos tabulares.
- **`selenium`**: Para la automatización de navegadores y extracción de datos dinámicos de páginas web.
- **`requests`**: Para realizar solicitudes HTTP y obtener contenido de páginas web.
- **`beautifulsoup4`**: Para analizar y extraer datos de archivos HTML y XML.

Puedes instalarlas utilizando el siguiente comando:

```bash
pip install pandas selenium requests beautifulsoup4
```

## Scripts

### 1. `01_df_correo.py`

Lee un archivo de texto con pares de nombre e identificación, limpia los datos y los guarda en un archivo CSV.

**Código Destacado**:

``` Leer archivo y crear DataFrame
data_split = open('datos_correo.txt', 'r').read().split('\n')
df_correo = pd.DataFrame([data_split[i:i+2] for i in range(0, len(data_split), 2)], columns=['NAME', 'ID'])
df_correo.to_csv('df_dni_name1.csv', index=False)
```

### 2. `02_xtraer_data_dni.py`

Utiliza Selenium para ingresar números de identidad en una página web, extraer nombres completos y guardarlos en un archivo CSV.

**Código Destacado**:

``` Inicializar el navegador y abrir la página web
driver = webdriver.Chrome()
driver.get("https://el-dni.com/")

def eldnicom(dni):
    ipt_dni = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(('xpath', '//input[@type="number" and @name="dni"]')))
    btn_buscar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(('xpath', '//button[@class="btn btn-primary mb-3"]')))
    ipt_dni.send_keys(dni)
    btn_buscar.click()
```
    
### 3. `03_comparar_data.py`

Compara los datos de dos archivos CSV para identificar y mostrar las diferencias entre ellos.

**Código Destacado**:

``` Comparar datos y mostrar inconsistencias
df_dni_name = pd.read_csv('df_dni_name1.csv')
df_dni_name_01 = pd.read_csv('df_dni_name2.csv')
datos_inconsistentes = pd.merge(df_dni_name, df_dni_name_01, how='outer', indicator=True)
datos_inconsistentes = datos_inconsistentes[datos_inconsistentes['_merge'] != 'both']
datos_inconsistentes.to_csv('datos_inconsistentes.csv', index=False)
```

### 4. `F_verificar_dni_0.1.py`

**Nota**: Este script fue una prueba para acceder a la API y extraer datos de manera más rápida, pero no se completó con éxito. No se incluye código para esta sección.

## Licencia

Este proyecto está bajo la licencia **NMS**.