# Importamos todos los modulos de pygame
import pygame,sys
from pygame.locals import *

# Inicializamos todos los modulos de pygame
pygame.init()

# Variable para las ventanas 
ANCHO = 800 
LARGO = 600
ventana = pygame.display.set_mode((ANCHO, LARGO))

#Colocar el titulo a la ventana
pygame.display.set_caption("MegaScooter")

# class Piso():
#     def __init__(self):
#         self.x=0        #inicializacion en 0
#         self.y=100

# class Nivel():
#     def __init__(self):
#         self.velocidad=-6

# velocidad=Nivel()
# pisoNuevo=Piso()
# def dibujarPiso():
#     piso = pygame.image.load("Imagenes/piso1.jpg").convert()   #cargamos la imagen en variable fondo
#     ventana.blit(piso, (pisoNuevo.x, 500))

# def logicaPiso():
    
#     if(pisoNuevo.x<-800):  #-- -900 Si no llega a -800 resta 2px al costado la imagen
#         pisoNuevo.x=800  # -- 100+ANCHO
#     else:
#         pisoNuevo.x+=velocidad.velocidad

class Variables_CargaImagenes():

    def __init__(self):
         self.xPiso=0       
         self.xFondo=0



FPS =300 #creamos la variable para la cantidad de pixeles
reloj=pygame.time.Clock() # hacemos el reloj para determinar cada cuanto se actualiza
variables=Variables_CargaImagenes()
xPiso=0 
def cargar_fondo():
    #-----------------------------Fondo----------------------------------------------
    fondo= pygame.image.load("Imagenes/fondo2.jpg").convert()
    x_rel_Fondo= variables.xFondo % fondo.get_rect().width

    ventana.blit(fondo, (x_rel_Fondo-fondo.get_rect().width, 0))
    if(x_rel_Fondo<ANCHO):
        ventana.blit(fondo,(x_rel_Fondo,0))
    variables.xFondo-=2
    #----------------------------Fin Fondo-------------------------------------------

# Bucle principal
while True:
    #logicaPiso()
    #dibujarPiso()
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    cargar_fondo()

    #-------------------------------Piso-------------------------------------------
    piso = pygame.image.load("Imagenes/piso1.jpg").convert()   #cargamos la imagen en variable piso
    x_rel_Piso= xPiso % piso.get_rect().width  #despues del % el comando obtiene el ancho
    #de la foto siendo el divisor de xPiso devuelve el resto

    ventana.blit(piso, (x_rel_Piso-piso.get_rect().width, 500))
    if(x_rel_Piso<ANCHO):
        ventana.blit(piso,(x_rel_Piso,500)) #Mostramos la imagen
    xPiso-=5   #Calcula la velocidad mientras el numero sea mas alto mas rapido ira el movimiento de la imagen
    # xPiso es la cantidad de pixeles por segundo
    #-----------------------------FinPiso-------------------------------------------
    
    pygame.display.update()
    reloj.tick(FPS)