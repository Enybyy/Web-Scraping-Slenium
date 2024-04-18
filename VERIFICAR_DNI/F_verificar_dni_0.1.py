import requests
from bs4 import BeautifulSoup

# –––––––– FAIL - TRAYING TO ACCESS YOUR SOURCE –––––––– #


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


# URL de la página web a la que nos conectaremos
url_pagina_web = "https://el-dni.com/"

# Conectarse a la página web y obtener el HTML
html_pagina_web = conectar_a_pagina_web(url_pagina_web)

# Verificar si se pudo conectar y obtener el HTML correctamente
if html_pagina_web:
    print("Conexión exitosa a la página web.")

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_pagina_web, 'html.parser')

    # Encontrar el elemento de entrada del DNI
    input_dni = soup.find('input', {'id': 'dni'})

    # Verificar si se encontró el elemento de entrada del DNI
    if input_dni:
        print("Se encontró la casilla de ingreso del DNI:")
        # Modificar el valor del atributo 'value' para ingresar el número de DNI
        # Aquí puedes poner el número de DNI que desees ingresar
        input_dni['value'] = '76173899'

        # Encontrar el botón de búsqueda
        boton_buscar = soup.find('button', {'class': 'btn btn-primary mb-3'})

        # Verificar si se encontró el botón de búsqueda
        if boton_buscar:
            print("Se encontró el botón de búsqueda.")

            # Simular hacer clic en el botón de búsqueda
            # Aquí pondremos el código para hacer clic en el botón

        else:
            print("No se encontró el botón de búsqueda.")
    else:
        print("No se encontró la casilla de ingreso del DNI.")
else:
    print("No se pudo conectar a la página web.")
