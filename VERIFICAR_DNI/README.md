# Verificación Automatizada de Identidades

Este proyecto automatiza la verificación de identidades mediante un sistema de web scraping, utilizando Python y varias bibliotecas. A continuación, se detalla cada componente del sistema y su función.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes componentes:

- **Python 3.x**: Asegúrate de tener Python 3.x instalado en tu sistema.
- **Bibliotecas de Python**: Este proyecto utiliza varias bibliotecas de Python. Puedes instalarlas utilizando `pip`. Aquí está el archivo `requirements.txt` que incluye todas las dependencias necesarias:

  ```plaintext
  pandas
  selenium
  requests
  beautifulsoup4
  ```

  Para instalar las bibliotecas, ejecuta:

  ```bash
  pip install -r requirements.txt
  ```

- **Driver de Selenium**: Necesitas el driver adecuado para el navegador que vas a usar con Selenium (por ejemplo, ChromeDriver para Google Chrome). Descárgalo y colócalo en una ubicación accesible en tu PATH.

- **Archivo de Datos**: Asegúrate de tener el archivo `datos_correo.txt` con los datos necesarios en la ruta especificada en el script `01_df_correo.py`.

## Descripción

El sistema consta de cuatro scripts que trabajan en conjunto para verificar identidades mediante números de identidad:

### 1. Extracción y Formateo de Datos

**Script: `01_df_correo.py`**

Este script procesa un archivo de texto con datos de nombres e IDs y los convierte en un DataFrame de pandas. Los datos se leen, se dividen en líneas, se organizan en un DataFrame y se guardan en un archivo CSV. Aquí está un fragmento clave del código que crea el DataFrame:

```python
df_correo = pd.DataFrame(
    [data_split[i:i+2] for i in range(0, len(data_split), 2)], columns=['NAME', 'ID'])
```

### 2. Extracción de Datos de la Web

**Script: `02_xtraer_data_dni.py`**

Este script utiliza Selenium para extraer nombres y apellidos asociados a números de identidad desde una página web. Se conecta a la web, ingresa la identidad en un formulario, y recoge la información resultante. Aquí hay un fragmento relevante que busca y llena el campo de identidad y hace clic en el botón de búsqueda:

```python
def eldnicom(dni):
    wait = WebDriverWait(driver, 5)
    ipt_dni = wait.until(
        EC.visibility_of_element_located(('xpath', '//input[@type="number" and @name="dni"]')))
    btn_buscar = wait.until(
        EC.visibility_of_element_located(('xpath', '//button[@class="btn btn-primary mb-3"]')))
    if ipt_dni and btn_buscar:
        ipt_dni.send_keys(dni)
        time.sleep(0.1)
        btn_buscar.click()
        # Código para extraer los nombres y apellidos
```
    
### 3. Comparación de Datos

**Script: `03_comparar_data.py`**

Este script compara los datos obtenidos con los datos originales para identificar inconsistencias. Utiliza pandas para realizar una comparación y genera un DataFrame con las discrepancias. Aquí está un fragmento clave que muestra cómo se realiza la comparación:

```python
datos_inconsistentes = pd.merge(
    df_dni_name, df_dni_name_01, how='outer', indicator=True)
datos_inconsistentes = datos_inconsistentes[datos_inconsistentes['_merge'] == 'right_only'].drop(
    '_merge', axis=1)
```

### 4. Verificación de Acceso a la Web (Prueba)

**Script: `F_verificar_dni_0.1.py`**

Este script es una prueba para conectar y extraer datos de una página web utilizando requests y BeautifulSoup. Aunque no se pudo concretar la automatización completa, el script muestra cómo se podría intentar acceder a los elementos de la página. Aquí un ejemplo de cómo se realiza una solicitud HTTP:

```python
def conectar_a_pagina_web(url):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print("Error al conectar con la página web:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None
```

## Licencia

Este proyecto está bajo la Licencia NMS (No Modificar y Compartir). No puedes usar, modificar, distribuir, ni compartir este código sin mi consentimiento previo. Si necesitas permisos para usar el código, por favor contacta al autor.

---

Para más detalles, consulta la documentación completa en [GitHub](https://github.com/tu_usuario/tu_repositorio).
