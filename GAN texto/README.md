
## Requisitos

- **PyTorch >= 1.1.0**
- Python 3.6
- Numpy 1.14.5
- CUDA 7.5+ (For GPU)
- nltk 3.4
- tqdm 4.32.1
- KenLM (https://github.com/kpu/kenlm)

Para instalarlos ejecutar `pip install -r requirements.txt`. En caso de problemas con CUDA, consultar(https://pytorch.org/get-started/locally/).

## KenLM Installation

- Descargar versión estable y descomprimir: http://kheafield.com/code/kenlm.tar.gz

- Necesita Boost >= 1.42.0 y bjam

  - Ubuntu: `sudo apt-get install libboost-all-dev`
  - Mac: `brew install boost; brew install bjam`

- Ejecutar *within* directorio kenlm:

  ```bash
  mkdir -p build
  cd build
  cmake ..
  make -j 4
  ```

- `pip install https://github.com/kpu/kenlm/archive/master.zip`/

## Implemented Models and Original Papers

### General Text Generation

- **SeqGAN** - [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](https://arxiv.org/abs/1609.05473)
- **LeakGAN** - [Long Text Generation via Adversarial Training with Leaked Information](https://arxiv.org/abs/1709.08624)
- **MaliGAN** - [Maximum-Likelihood Augmented Discrete Generative Adversarial Networks](https://arxiv.org/abs/1702.07983)
- **JSDGAN** - [Adversarial Discrete Sequence Generation without Explicit Neural Networks as Discriminators](http://proceedings.mlr.press/v89/li19g.html)
- **RelGAN** - [RelGAN: Relational Generative Adversarial Networks for Text Generation](https://openreview.net/forum?id=rJedV3R5tm)
- **DPGAN** - [DP-GAN: Diversity-Promoting Generative Adversarial Network for Generating Informative and Diversified Text](https://arxiv.org/abs/1802.01345)
- **DGSAN** - [DGSAN: Discrete Generative Self-Adversarial Network](https://arxiv.org/abs/1908.09127)
- **CoT** - [CoT: Cooperative Training for Generative Modeling of Discrete Data](https://arxiv.org/abs/1804.03782)

### Category Text Generation

- **SentiGAN** - [SentiGAN: Generating Sentimental Texts via Mixture Adversarial Networks](https://www.ijcai.org/proceedings/2018/618)
- **CatGAN** (ours) - [CatGAN: Category-aware Generative Adversarial Networks with Hierarchical Evolutionary Learning for Category Text Generation](https://arxiv.org/abs/1911.06641)

## Get Started

- Get Started

```bash

```

- Para más experimentos (`Image COCO`, `EMNLP NEWs`, `Movie Review`, `Amazon Review`) can be downloaded from [here](https://drive.google.com/drive/folders/1XvT3GqbK1wh3XhTgqBLWUtH_mLzGnKZP?usp=sharing). 
- Ejecutar solo con un modelo

```bash
cd run
python3 run_leakgan.py 0 0	# El primer 0 es job_id, el segundo 0 es gpu_id

# Por ejemplo
python3 run_seqgan.py 0 0
```

## Features

1. **Instructor**

Para cada modelo, todo el proceso de ejecución se define en instructor/oracle_data/leakgan_instructor.py. ( Algunas funciones básicas como init_model() y optimize() se definen en la clase base BasicInstructor en instructor.py. Si deseas agregar un nuevo modelo de generación de texto basado en GAN, por favor crea un nuevo instructor en instructor/oracle_data y define el proceso de entrenamiento para el modelo.

2. **Visualización**
   
   Usar `utils/visualization.py` para visualizar el archivo de logs, incluye métricas de pérdidas y modelos. 
   

  
### LeakGAN

- Ejecutar archivo: run_leakgan.py (run/run_leakgan.py)

- Instructores: oracle_data(instructor/oracle_data/leakgan_instructor.py), real_data(instructor/real_data/leakgan_instructor.py)

- Modelos: generator(models/LeakGAN_G.py), discriminator(models/LeakGAN_D.py)



  

## Licence

**MIT lincense**

