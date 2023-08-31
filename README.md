
# AMLO-GPT

![nanoGPT](assets/amlogpt_banner.jpg)

A simple scripts to train a [nanoGPT](https://github.com/karpathy/nanoGPT) model with extracted from the morning conferences hosted by the mexican president, Andres Manuel Lopez Obrador.
## install

```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```

Dependencies:

- [pytorch](https://pytorch.org)
- [numpy](https://numpy.org/install/)
-  `transformers` for huggingface transformers <3 (to load GPT-2 checkpoints)
-  `opendatasets` for kaggle datasets (if you want to download + preprocess the conferences transcripts)
-  `mananeras` for easy processing of the transcripts
-  `tiktoken` for OpenAI's fast BPE code 
-  `wandb` for optional logging 
-  `tqdm` for progress bars 

## quick start

Download the conferences data from the kaggle, extract only the dialogs from the mexican president and tokenize the dataset.


```
$ python data/amlo/prepare.py
```

This creates a `train.bin` and `val.bin` in that data directory. Now we can train the GPT model. The size of it very much depends on the computational resources of your system:


```
$ python train.py config/train_amlo.py
```

If you are running out of memory try adjusting some parameters in this file like n_layer, n_head, n_embd, block_size or batch_size. Based on the configuration, the model checkpoints are being written into the `--out_dir` directory `out-amlo`. 

## sampling / inference

Once the training finishes we can use the script `sample.py` to sample from a model you trained yourself by pointing the sampling script at the output directory.

```
$ python sample.py --out_dir=out-amlo
```

This generates a few samples, for example:


```
De lo que siempre hemos recomendado, que es una mujer con principios, con ideales, con principios, que eso es lo mejor y también, y no queremos que se inicien estas acciones o que se creó durante un tiempo.
Siempre se habla de conservadores, en México, que han hecho muchas a los conservadores de ahora, mucho tienen sus enjuagues, sus voceros, son muy conservadores, han seguido manteniendo la política posrevolucionaria, entre otras, son muy corruptos y muy hipócritas, pero hay algunos que van a seguir diciendo que hay un cambio en México y que yo defiendo intereses creados, que son muy conservadores, muy corruptos.
Pero el hecho de que la transformación es de que cambia todo. No cambia la mentalidad de un pueblo y que se necesita un cambio, y que se necesita una transformación, no cambia todo en beneficio del pueblo.
Sí hay que convencer, pero hay que verlo, hay que analizarlo.
No, tenemos todos los elementos, pero sí tenemos que ver si hay trabajadores o hay, como no hay trabajadores inscritos en el Seguro Social, no hay servicios, no hay servicios médicos.
Y una cosa que tiene que ver con la familia, que diga si no hay una regidora de oro de la clase media, con la familia que tiene una clínica privada, no tiene una familia en una clínica pobre.
Todos los días están atendiendo esto, o sea, qué pasa con el Reforma y con la profundidad, pero con el racismo, con la discriminación.
Pero que no hablemos de
```

```
También aprovecho para decir que en esta semana se están reuniendo los gobernadores para que se llegue a acuerdo.
Bueno, aprovecho para decir que se está avanzando en el bienestar de la gente, en especial lo de la pensión a los adultos mayores, en el caso de la pensión a niñas, niños con discapacidad, las becas sean a sus hijos y se les está ayudando, tanto, en el campo como en el campo, que se está apoyando a productores, se le está dando preferencia a los más pobres, como nunca se había hecho en este tiempo.
El programa de becas para preescolar, primaria, secundaria, lo que era el Procampo ahora se llama Producción para el Bienestar, y se están entregando a tres millones de estudiantes de familias pobres.
Ya también en comunidades indígenas se está apoyando a los productores, se le está dando trabajo a mucho apoyo de manera directa a los que tienen más apoyo para sembrar.
Ya se fijaron precios de garantía, se les está pidiendo un precio justo a los productores, era un precio muy bajo; ya es un precio justo, pero todavía no se lleva a cabo un precio justo a los productores, a los adultos mayores de 65 años y ya es un precio justo, para que siembren sus familiares, que no tenga que ir a sus comunidades, que no tenga que ir a buscar sus pueblos y que no tengan que irse la vida a otras partes.
Eso ya se está llevando a cabo, acabo de decir que estamos trabajando en varias entidades federativas en
```

```
Y se va a fortalecer el mercado interno, porque de eso depende mucho, o sea, que en vez de tener mercado, que tenga producción, es lo que estamos buscando para sacar adelante al país en lo económico. Tenemos, por ejemplo, el petróleo, que es de la nación y es el que aumentaron los precios de las gasolinas, del diésel, de la luz, que eso es lo que estamos viendo aquí.
Y ya está lo de la ley de la ley.
¿Qué es lo que hacían antes?
‘No se podía quedar sin gas a las empresas, a los bancos, no se puede enfrentar el problema, no se puede enfrentar el problema de la inflación’, no se puede enfrentar la inflación.
¿Qué había?
Luego, privatizaron la industria petrolera y eso es lo que se hicieron durante los 36 años de política neoliberal.
Ayer hablaba yo de cómo íbamos a estar bajando la producción de petróleo y comprábamos las gasolinas en el país, que nos íbamos a caer porque no estamos importando petróleo crudo, estamos rehabilitando las refinerías, estamos proyectando una nueva refinería en Dos Bocas, en Paraíso, Tabasco; y esto nos está permitiendo que no aumente el precio de las gasolinas porque cuesta muchísimo dinero y extraer el combustóleo.
Pero no sólo eso, desde Salinas hasta hace mucho tiempo, desde Salinas hasta hace más de 30 años, toda la nación, hasta Salinas, 40, 50 años,
```

## acknowledgements
[nanoGPT](https://github.com/karpathy/nanoGPT) provides the codebase for train the models.

[Mananeras](https://www.kaggle.com/datasets/ioexception/mananeras) provides and updated and easy to use dataset of the mexican president morning conferences.
