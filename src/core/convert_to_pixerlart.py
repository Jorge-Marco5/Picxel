
from PIL import Image

def convert_to_pixelart(image_path, size_pixel, guardar_path):
    print("Convirtiendo a pixelart...")
    imagen = Image.open(image_path)
    
    #calculo del tamaño reducido de la imagen
    ancho, alto = imagen.size
    nuevo_ancho = int(ancho / size_pixel)
    nuevo_alto = int(alto / size_pixel)
    
    #reducir la resolucion de la imagen
    image_reduced = imagen.resize((nuevo_ancho, nuevo_alto), resample = Image.BILINEAR)

    #escalar imagen al tamaño original
    image_reescalada = image_reduced.resize((ancho, alto), resample = Image.NEAREST)

    #guardar la imagen resultante
    image_reescalada.save(guardar_path)
    return image_reescalada
