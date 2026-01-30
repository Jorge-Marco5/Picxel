"""
Funcion que crea en formato ascii una imagen pixelart
con sus colores correspondientes de cada pixel de imagen
usamos ANSI para cada color personalizado
Mostramos el resultado en la terminal

Parametros:
    image_path: ruta de la imagen en pixelart
"""
import os
from PIL import Image

def create_ascii(image_path):
    #abrimos la imagen
    image = Image.open(image_path)
    
    #convertimos la imagen a RGB
    image = image.convert("RGB")

    #obtenemos el ancho y alto de la terminal
    try:
        ancho, alto = os.get_terminal_size()
    except OSError:
        ancho, alto = 80, 24
        
    #redimensionamos la imagen para que se adapte al tamaño de la terminal
    image = image.resize((ancho, alto), Image.NEAREST)

    #caracter a usar
    caracter = "█"
    
    #recorremos la imagen pixel por pixel
    for y in range(alto):
        for x in range(ancho):
            #obtenemos el valor del pixel (r, g, b)
            r, g, b = image.getpixel((x, y))
            
            #imprimimos el caracter con el color correspondiente
            # Usamos secuencias de escape ANSI para color verdadero (24-bit): \033[38;2;R;G;Bm
            print(f"\033[38;2;{r};{g};{b}m{caracter}\033[0m", end="")
            
        #imprimimos un salto de linea
        print()
        
    #fin de la funcion