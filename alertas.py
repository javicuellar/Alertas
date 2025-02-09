from Herramientas.variables import USUARIO, PASSWORD, DESTINATARIO
from alerta_MD import Alerta_MD
# from alerta_ficheros import Alerta_Ficheros               # Genera fichero excel
from alerta_ficheros_sheet import Alerta_Ficheros_sheet     # Actualiza hoja de cálculo





#     Analizamos las alertas:

#  Alerta puestos en Madrid Digital
Alerta_MD(USUARIO, PASSWORD, DESTINATARIO)


#  Analizamos ficheros en DIRECTORIO mayores de T_MINIMO 
T_MINIMO = 4 * 1024 * 1024 * 1024      # GB en bytes (1024 bytes x 1024 Mb x 1024 Gb)

# Para Windows añadimos path a librerías python, para añadir librerías mías de Herramientas
import sys, os
if os.name == 'nt':
    sys.path.append(os.path.join(os.path.dirname(__file__), '\\Python'))
    DIRECTORIO = 'D:\\'
else:
    DIRECTORIO = '/video'

Alerta_Ficheros_sheet(DIRECTORIO, T_MINIMO)