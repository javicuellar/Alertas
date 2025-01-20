import sys, os

# Para Windows añadimos path a librerías python, para añadir librerías mías de Herramientas
if os.name == 'nt':
    sys.path.append(os.path.join(os.path.dirname(__file__), '\\Python'))
    DIRECTORIO = 'D:\\'
else:
    DIRECTORIO = '/video'



from Herramientas.variables import Variables
from alerta_MD import Alerta_MD
# from alerta_ficheros import Alerta_Ficheros       # Genera fichero excel
from alerta_ficheros_sheet import Alerta_Ficheros   # Actualiza hoja de cálculo





var = Variables() 


#     Analizamos las alertas:

#  Alerta puestos en Madrid Digital
Alerta_MD(var)

#  Analizamos ficheros en DIRECTORIO mayores de T_MINIMO 
T_MINIMO = 2 * 1024 * 1024 * 1024      # 2 GB en bytes
Alerta_Ficheros(var, DIRECTORIO, T_MINIMO)