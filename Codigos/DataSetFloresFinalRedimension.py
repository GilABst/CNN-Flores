#!/usr/bin/env python
# coding: utf-8

# In[4]:

#IMPORTACIONES NECESARIAS
import cv2 as cv
import numpy as np
import math


# In[8]:

#FUNCION GUARDAR IMAGEN LLEGAN LOS PARAMETROS DE LA MASCARA, EL FRAME, IMAGEN EN ESCALA HSV, NUMERO DE IMAGEN
def guardar (mask1, frame, hsv, num_img):    
    #BITWISE_AND BUSCA UN PUNTO DE INTERSECCION ENTRE DOS IMAGENES, SI AMBAS SON DE LA MISMA INTENSIDAD APLICA LA MISMA INTENSIDAD AL PIXEL
    #PRIMER PARAMETRO PRIMERA IMAGEN
    #SEGUNDO PARAMETRO SEGUNDA IMAGEN EN ESTE CASO ES LA MISMA
    #TERCER PARAMETRO LA MASCARA DE COLOR QUE SE LA APLICARA
    res=cv.bitwise_and(frame, frame, mask=mask1)
    #RESIZE, REDIMENSIONAR EL TAMANIO DE LA IMAGEN
    #PRIMER PARAMETRO IMAGEN A REDIMENSIONAR
    #SEGUNDO PARAMETRO TAMANIO DE REDIMENSION
    #TERCER PARAMETRO TIPO DE INTERPOLACION, INTERPOLACION CUBICA GENERA UN PROMEDIO DEL PIXEL PARA SUSTITUIRLO CON UNO NUEVO
    new_img = cv.resize(res, dsize=(50, 50), interpolation=cv.INTER_CUBIC)
    name='C:\\Users\\gilba\\Desktop\\IA\\DataSetFlores\\Marigold\\img_'+str(num_img)+'.jpg'
    cv.imwrite(name,new_img)


# In[9]:


video=cv.VideoCapture("C:\\Users\\gilba\\Desktop\\IA\\DataSetFlores\\Marigolds.mp4")

#CONTADOR, NOMBRE UNICO DE IMAGEN
num_img = 108
while (video.isOpened()):
    #SACAMOS CADA FRAME DEL VIDEO
    ret, frame = video.read()
    if ret == False:
        break
    
    #CONVIERTE DE RGB A HSV PARA RESALTAR EL COLOR Y PODER USAR LOS PARAMETROS DE LA "HSV COLOR TABLE"
    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #MASCARA DE COLOR MARIGOLD AMARILLO Y ROJO
    
    YellowBajo1 = np.array([0,60,60])
    YellowAlto1 = np.array([32,255,255])
    redBajo2 = np.array([170,50,50])
    redAlto2 = np.array([180,255,255])
    
    maskRed1 = cv.inRange(hsv, YellowBajo1, YellowAlto1)
    maskRed2 = cv.inRange(hsv, redBajo2, redAlto2)
    #JUNTAMOS MASCARAS PARA GENERAR UNA ADECUADA PARA EXTRAER EL COLOR NECESARIO
    mask1 = cv.add(maskRed1, maskRed2)
    
    
    
    #MASCARA DE COLOR DHALIA MORADA
    
    #WhiteBajo1 = np.array([0,0,0])
    #WhiteAlto1 = np.array([0,0,255])
    #PurpleBajo2 = np.array([135,0,0])
    #PurpleAlto2 = np.array([165,255,255])
    
    #maskRed1 = cv.inRange(hsv, WhiteBajo1, WhiteAlto1)
    #maskRed2 = cv.inRange(hsv, PurpleBajo2, PurpleAlto2)
    #mask1 = cv.add(maskRed1, maskRed2)
    
    
    #MASCARA DE COLOR ORQUIDEA BLANCO
    
    #WhiteBajo1 = np.array([0,0,168])
    #WhiteAlto1 = np.array([150,111,255])
    #mask1 = cv.inRange(hsv, WhiteBajo1, WhiteAlto1)
    
    
    
    
    #MASCARA DE COLOR ROSA ROJO
    
    #redBajo1 = np.array([0,50,50])
    #redAlto1 = np.array([10,255,255])
    #redBajo2 = np.array([170,50,50])
    #redAlto2 = np.array([180,255,255])
    
    #maskRed1 = cv.inRange(hsv, redBajo1, redAlto1)
    #maskRed2 = cv.inRange(hsv, redBajo2, redAlto2)
    #mask1 = cv.add(maskRed1, maskRed2)
    
    #FUNCION GUARDAR       
    guardar(mask1 , frame, hsv, num_img)
    
    #AUMENTAMOS EL CONTADOR PARA TENER UN NOMBRE UNICO POR IMAGEN
    num_img += 1
    
video.release()
cv.waitKey(0)
cv.destroyAllWindows()


# In[10]:

#ROTACION DE IMAGENES Y TRANSLACION PARA GENERAR MAYOR CANTIDAD DE IMAGENES EN NUESTRO DATA SET
def Imagenes(ejex, ejey):
    
    #ESTABLECEMOS RUTA DE IMAGEN Y SE LEVANTA
    img1 = cv.imread('C:\\Users\\gilba\\Desktop\\IA\\DataSetFlores\\Marigold4.jpg')

    ancho = img1.shape[0]
    alto = img1.shape[1]
    
    #GENERAMOS LA MATRIZ DE TRANSFORMACION DE LA IMAGEN, PARA TRANSLADARLA
    M= np.float32([[1,0,ejex], [0,1,ejey]])
    #WARPAFFINE TRANSLACION DE IMAGEN AFIN POR MEDIO DE OPERACIONES MATRICIALES
    #PROMER PARAMETRO LA IMAGEN A MODIFICARDE
    #SEGUNDO PARAMETRO LA MATRIZ TRANSFORMADA
    #TERCER PARAMETRO ANCHO Y ALTO DE IMAGEN
    img = cv.warpAffine(img1, M, (ancho, alto))
    
    #DATOS DE IMAGEN
    h,w = img.shape[:2]       #DEFINE LARGO Y ANCHO
    imgz = np.zeros((h*2, w*2), dtype = 'uint8') #CREA MATRIZ DE 0, IMAGEN A 8 BITS
    
    
    ##CONTADOR DE GUARDADO Y INDENTIFICADOR UNICO DE IMAGEN GENERADA
    num_img = -180

    
    ## GIRAMOS LA IMAGEN
    ## GIRA LA LETRA - GIRO A MANECILLAS DEL RELOJ
    ##              + GIRO EN CONTRA DE MANECILLAS
    while(num_img != 181):
        #GIRAMOS LA IMAGEN CON LA FUNCION GETROTATION
        #PRIMER PARAMETRO NOS SIRVE PARA CENTRAR LA IMAGEN
        #SEGUNDO PARAMETRO GRADO DE GIRO
        #TERCER PARAMETRO FACTOR ESCALA
        mw = cv.getRotationMatrix2D( (h//2, w//2), num_img, 1 )
        #DEFINIMOS IMAGEN DE SALIDA, AFINAMOS CON WARPAFFINE
        #PRIMER PARAMETRO IMAGEN A MODIFICAR
        #SEGUNDO PARAMETRO LA MATRIZ TRANSFORMADA
        #TERCER PARAMETRO TAMANIO DE LA IMAGEN DE SALIDA
        imgz = cv.warpAffine(img,mw,(h,w))
        ruta = 'C:\\Users\\gilba\\Desktop\\IA\\DataSetFlores\\Marigold\\Marigold (('+str(ejex)+'_'+str(ejey)+'_'+ str(num_img)+').jpg'
        cv.imwrite(ruta, imgz)
        num_img += 1
    


# In[11]:


#MATRIZ DE TRANSLACION DE IMAGEN DESDE (-1,-1) HASTA (1,1) 
lados = [[1,-1,1,-1],[1,1,-1,-1]]

#INICIALIZACION UNICAMENTE PARA PODER CONTINUAR
x = 1
y = 1

#CICLO, RECORREMOS EL ARREGLO DE RUTA GENERAL Y RUTA DE LA IMAGEN PARA LOGRAR LA AUTOMATIZACION DEL PROCESO
size = len(General)
for h in range(size):
    for i in range(4):
        for j in range(10):
            #CALCULAMOS LA TRANSLACION QUE LE DARA A LA IMAGEN POR CICLO
            #SE MULTIPLICA POR J PARA DARLE UNA TRANSLACION DE HASTA 10 PIXELES DE IZQUIERDA A DERECHA, ARRIBA A ABAJO
            #PRIMERO EN LA TRANSLACION EJE X
            x = lados [0][i] * (j)
            #SEGUNDO TRANSLACION EJE Y
            y = lados [1][i] * (j)
            Imagenes(Img[h], General[h],x,y)
    
##FINALIZAR
print ("PROCESO FINALIZADO")

