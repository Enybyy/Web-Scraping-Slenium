Verificación Automatizada de DNIs

Descripción:
Este proyecto consiste en un script en Python que automatiza el proceso de verificación de DNIs en una página web utilizando una base de datos previamente obtenida. La herramienta recorre los DNIs de la base de datos, los ingresa en el formulario de verificación en línea, y compara la información obtenida con la de la base de datos. Se genera un nuevo DataFrame con los DNIs que no coinciden, lo que permite un proceso eficiente de identificación de discrepancias.

Funcionamiento
El script utiliza las siguientes tecnologías y herramientas:

Python: Lenguaje de programación utilizado para desarrollar el script.
Selenium: Librería de automatización de navegadores web, utilizada para interactuar con la página web de verificación de DNIs.
Pandas: Librería de manipulación y análisis de datos, utilizada para trabajar con la base de datos de DNIs.
Otros paquetes de Python: Se pueden utilizar otros paquetes según sea necesario para el procesamiento de datos y la manipulación del DataFrame resultante.
El flujo de trabajo del script es el siguiente:

Lee la base de datos de DNIs previamente obtenida.
Utiliza Selenium para abrir un navegador web y acceder a la página de verificación de DNIs.
Ingresa cada DNI en el formulario de verificación en línea.
Obtiene la información correspondiente al DNI verificado.
Compara la información obtenida con la de la base de datos.
Si hay discrepancias, agrega el DNI a un nuevo DataFrame.
Guarda el nuevo DataFrame en un archivo CSV para su posterior análisis.

Autor
Este proyecto fue desarrollado por Tu Eliud RM.
