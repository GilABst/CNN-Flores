#!/usr/bin/env python
# coding: utf-8

# In[2]:


#IMPORTAMOS LIBRERIAS
import numpy as np
from keras import models
import cv2 as cv


# In[3]:


#CARGAMOS EL MODELO
model = models.load_model("C:\\Users\\gilba\\Desktop\\IA\\ProyectoFinal\\Flores\\flores99.h5py")


# In[4]:


#ASEGURAMOS QUE EL MODELO SE CARGO CORRECTAMENTE, OPCIONAL NO TIENE FUNCIONALIDAD EN EL PROGRAMA
model.summary()


# In[5]:


#ARREGLO DE CLASES PARA CUANDO REALICEMOS LA PREDICCION COINCIDAN
clases_flores = ['Dhalia', 'Marigold', 'Orquidea', 'Rosa']

#DECALRAMOS UN CONTADOR PARA NO DESBORDAR EL CICLO DE BUSQUEDA DE LA PREDICCION, 
#SOBRE TODO PARA QUE SE VEA MAS CLARO, VISUAL
contador = len(clases_flores)


# In[9]:


#TRATAMOS LA IMAGEN Y LA CONVERTIMOS A NUMPY ARRAY 

def tratarImg(im):
    #SE PODRIAN AGREGAR FILTRO DE COLOR Y REDIMENSION PARA TRATAR LA IMAGEN ANTES DE 
    #CONVERTIRLA A UN ARRAY Y REALIZAR LA PREDICCION, ESTO NOS DARIA MAYOR PRESICION
    
    #SE CORRIJE LA GAMA DE LA IMAGEN DE BGR A RGB :)
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)

    #SE CREA EL NUMPY ARRAY
    img_array = np.array(im)
    
    #EXPANDE LA MATRIZ ARRAY PARA EVITAR EL ERROR NONE,50,50,3
    img_array = np.expand_dims(img_array, axis=0)
    
    #RETORNAMOS EL NUMPY ARRAY DE LA IMAGEN
    return img_array


# In[14]:


#LEEMOS LA IMAGEN
#IM LA USAREMOS PARA REALIZAR LA PREDICCION
im = cv.imread("C:\\Users\\gilba\\Desktop\\IA\\ProyectoFinal\\Flores\\Pruebas\\Orquidea8.jpg")

#IM2 LA USAREMOS PARA MOSTRARLA UNICAMENTE
imagen2 = cv.imread("C:\\Users\\gilba\\Desktop\\IA\\ProyectoFinal\\Flores\\Pruebas\\Orquidea8.jpg")

#RESIZE PARA VER EL RESULTADO MAS AMPLIO
imagen2 = cv.resize(imagen2,(600,600))

#SE ENVIA IM AL METODO PARA TRATARLA Y CONVERTIRLA EN ARRAY
img_array = tratarImg(im)

#SE REALIZA LA PREDICCION CON EL MODELO Y LA IMAGEN ARRAY
prediction = model.predict(img_array)

#SE IMPRIME LA PREDICCION
print (prediction)

#RECORREMOS EL ARREGLO Y GUARDAMOS LA PREDICCION PARA AGREGARLA A LA IMAGEN FINAL
for i in range(contador):
    #SI EL VALOR DE LA CASILLA [0][i] ES IGUAL A 1 SACAMOS EL NOMBRE DE ESA MISMA CELDA EN EL ARRAY CLASES 
    if prediction[0][i].all() == 1 :
        #GUARDA LA PREDICCION PARA MOSTRAR DICHO TEXTO EN LA IMAGEN
        mostrar="Predice: "+clases_flores[i]
        #ROMPE EL CICLO SI ENCONTRO UN 1
        break

#PUT TEXT AGREGA EL TEXTO EN LA IMAGEN
#PRIMER PARAMETRO IMAGEN A MOSTRAR
#SEGUNDO PARAMETRO TEXTO A AGREGAR
#TERCER PARAMETRO POSICION
#CUARTO PARAMETRO TIPO DE LETRA
#QUINTO PARAMETRO TAMANIO DE LA LETRA
#SEXTO PARAMETRO COLOR
#SEPTIMO PARAMETRO TRAZO DE LA LETRA, NUMERO DE PIXELES
cv.putText(imagen2, mostrar,(0,50), cv.FONT_HERSHEY_SIMPLEX, 1,(50,255,0),2)

#MUESTRA IMAGEN
cv.imshow("imagen", imagen2)
cv.waitKey(0)
cv.destroyAllWindows()

