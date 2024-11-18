#  Recuperamos los puestos que hay en la web de Madrid Digital, si los hay.
# --------------------------------------------------------------------------
#       Url Madrid Digital
URL_MD = "https://www.comunidad.madrid/servicios/empleo/procesos-selectivos-agencia-administracion-digital"
#
#  Se recupera la tabla de puestos que hay en la web.

from Herramientas.scraping import Recuperar_tablas
from Herramientas.mail import Envio_mail



def Alerta_MD(variables): 
    #  Recuperamos la tabla con los puestos
    tablas = Recuperar_tablas(URL_MD)

    #  Comprobamos si hay puestos, y si los hay se envía alerta
    puestos = tablas[0].iloc[:, :2]
    
    if puestos.iloc[0].nunique() == 1:    # Si no hay puestos, todos los valores son los mismos
        print('No se encontrado puestos en Madrid Digital')
        alerta = 'Puestos Madrid Digital - NO HAY NINGUNO'
        mensaje = f"{puestos.iloc[0,1]}\nVisita la pagina web\n{URL_MD}"
        Envio_mail(variables.usuario, variables.password , alerta, mensaje, variables.destinatario)
    else:
        alerta = 'ALERTA - Puestos Madrid Digital'
        mensaje = f"Han salido los siguientes puestos en Madrid Digital.\n\n{puestos.to_string(index=False)}\n\n Visita la pagina web\n{URL_MD}"
        print(mensaje)
        Envio_mail(variables.usuario, variables.password , alerta, mensaje, variables.destinatario)
