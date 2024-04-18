from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def eldnicom(dni):
    wait = WebDriverWait(driver, 5)
    try:
        # XPATH CASILLA INGRESAR DNI
        ipt_dni = wait.until(
            EC.visibility_of_element_located(('xpath', '//input[@type="number" and @name="dni"]')))
        # XPATH BOTN BUSCAR
        btn_buscar = wait.until(
            EC.visibility_of_element_located(('xpath', '//button[@class="btn btn-primary mb-3"]')))

        if ipt_dni and btn_buscar:
            ipt_dni.send_keys(dni)
            time.sleep(0.1)
            btn_buscar.click()
            lista_dni.append(dni)
            time.sleep(1)
            try:
                nombres = driver.find_elements(
                    by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[2]/td[2]')
                apellido = driver.find_elements(
                    by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[3]/td[2]')
                apellido01 = driver.find_elements(
                    by='xpath', value='//table[@class="table-bordered table"]/tbody/tr[4]/td[2]')

                # LISTA PARA GUARDAR ELEMENTOS
                apellido_nombres = []

                for nombre_element in apellido:
                    apellido_nombres.append(nombre_element.text.strip())

                for apellido_element in apellido01:
                    apellido_nombres.append(apellido_element.text.strip())

                for apellido01_element in nombres:
                    apellido_nombres.append(apellido01_element.text.strip())
                # GUARDAR APELLIDOS Y NOMRBES E DF
                df_apellido_nombres = ' '.join(apellido_nombres)
                lista_fullname.append(df_apellido_nombres)

                ipt_dni.clear()

            except Exception as e:
                print("Error:", e)
        else:
            if not ipt_dni:
                print("No se encontró el campo 'DNI'")
            if not ipt_dni:
                print("No se encontró el botón 'BUSCAR'")

    except Exception as e:
        print("Error:", e)

    time.sleep(0.5)


df_dni_name1 = pd.read_csv(
    "C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name1.csv")

driver = webdriver.Chrome()
print("CONECTANDOSE A LA PAGINA WEB...")
driver.get("https://el-dni.com/")

dni01 = df_dni_name1['ID']

# LISTAS:
lista_dni = []
lista_fullname = []

for dni02 in dni01:
    eldnicom(dni02)

df_dni_name2 = pd.DataFrame(
    {'NAME': lista_fullname, 'ID': lista_dni})

df_dni_name2.to_csv(
    "C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/CORREO/DATAFRAME/df_dni_name2.csv", index=False)
