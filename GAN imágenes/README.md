

## Instalación
    $ git clone https://github.com/eriklindernoren/PyTorch-GAN
    $ cd PyTorch-GAN/
    $ sudo pip3 install -r requirements.txt

## Implementación 

### StarGAN
_StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation_

#### Autores
Yunjey Choi, Minje Choi, Munyoung Kim, Jung-Woo Ha, Sunghun Kim, Jaegul Choo

#### Abstracto
Estudios recientes han mostrado un éxito notable en la traducción de imagen a imagen para dos dominios. Sin embargo, los enfoques existentes tienen una escalabilidad y robustez limitadas para manejar más de dos dominios, ya que se deben construir modelos independientes para cada par de dominios de imagen. Para abordar esta limitación, proponemos StarGAN, un enfoque novedoso y escalable que puede realizar traducciones de imagen a imagen para múltiples dominios utilizando solo un modelo. La arquitectura de modelo unificado de StarGAN permite el entrenamiento simultáneo de múltiples conjuntos de datos con diferentes dominios dentro de una sola red. Esto conduce a la calidad superior de las imágenes traducidas de StarGAN en comparación con los modelos existentes, así como a la capacidad novedosa de traducir de manera flexible una imagen de entrada a cualquier dominio de destino deseado. Demostramos empíricamente la efectividad de nuestro enfoque en la transferencia de atributos faciales y en la síntesis de expresiones faciales.


(https://arxiv.org/abs/1711.09020) [[Code]](implementations/stargan/stargan.py)

#### Ejecutar
```
$ cd implementations/stargan/
$ python3 stargan.py
El dataset puede ser descargado desde: https://www.dropbox.com/sh/8oqt9vytwxb3s4r/AADIKlz8PR9zr6Y20qbkunrba/Img/img_align_celeba.zip?dl=0
Y las anotaciones: https://www.dropbox.com/sh/8oqt9vytwxb3s4r/AAA8YmAHNNU6BEfWMPMfM6r9a/Anno?dl=0&preview=list_attr_celeba.txt
Instrucciones para ejecutar el script:
1. Descargar dataset y anotaciones de los enlaces dados
2. Copair 'list_attr_celeba.txt' en carpeta 'img_align_celeba'
2. Guardar 'img_align_celeba' en '../../data/'
4. Ejecutar usando 'python3 stargan.py'
```


