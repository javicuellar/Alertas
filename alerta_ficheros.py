#  Análisis de los ficheros del directorio enviando alerta mail con los ficheros mayores de x bytes.
# ---------------------------------------------------------------------------------------------------
#       Lectura del DIRECTORIO:
DIRECTORIO = 'D:\\'
#
#       Tamaño mínimo de ficheros a alertar
TAMANO_MINIMO = 5 * 1024 * 1024 * 1024      # 5 GB en bytes
TAMANO_MINIMO = 5 * 1024 * 1024             # para pruebas en D:


from Herramientas.mail import Envio_mail_adjunto


import os
import pandas as pd





# Función para buscar archivos mayores a t_minimo
def buscar_archivos_grandes(directorio, t_minimo):
    archivos_grandes = []
    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)
            if os.path.getsize(ruta_archivo) > t_minimo:
                archivos_grandes.append((archivo, ruta_archivo, os.path.getsize(ruta_archivo)))
    return archivos_grandes


#  Alerta de Ficheros mayores de T_MINIMO
def Alerta_Ficheros(variables, directorio, t_minimo):
    archivos_grandes = buscar_archivos_grandes(directorio, t_minimo)
    
    if archivos_grandes:
        # Crear DataFrame y guardar en Excel
        df = pd.DataFrame(archivos_grandes, columns=['Nombre', 'Ruta', 'Tamaño (bytes)'])        
        archivo_excel = 'archivos_grandes.xlsx'
        df.to_excel(archivo_excel, index=False)

        tamano = round(t_minimo / (1024 * 1024 * 1024), 2)
        alerta = f'ALERTA - {len(archivos_grandes)} archivos de más de {tamano} Gb. detectados en {directorio}'
        mensaje = f"Se han encontrado {len(archivos_grandes)} archivos mayores de {tamano} Gb."
        print(mensaje)
        Envio_mail_adjunto(variables.usuario, variables.password , alerta, mensaje, variables.destinatario, archivo_excel)
    else:
        print(f'No se encontraron archivos mayores de {tamano} Gb.')
