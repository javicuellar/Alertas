#  -- Para uso en PC añadir --
import sys, os

# Añadimos path a librerías python, para añadir librerías mías de Herramientas
sys.path.append(os.path.join(os.path.dirname(__file__), '\Python'))
#  -- Fin uso en PC --

from Herramientas.variables import Variables
from alerta_MD import Alerta_MD
from alerta_ficheros import Alerta_Ficheros





var = Variables() 

#     Analizamos las alertas:

#  Alerta puestos en Madrid Digital
Alerta_MD(var)

#  Analizamos ficheros en DIRECTORIO mayores de T_MINIMO 
DIRECTORIO = 'D:\\'
T_MINIMO = 2 * 1024 * 1024 * 1024      # 5 GB en bytes
Alerta_Ficheros(var, DIRECTORIO, T_MINIMO)