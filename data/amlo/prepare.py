import os
import requests
import mananeras
import numpy as np
import pandas as pd
import opendatasets as od
from unidecode import unidecode
import tiktoken

path = "data/amlo/input/mananeras"
od.download("https://www.kaggle.com/datasets/ioexception/mananeras", path)
conferencias = mananeras.lee_todas(path)

dialogos_speakers = []
for conferencia in conferencias:
    for participación in conferencia.participaciones:
        participante = unidecode(participación.hablante).lower()
        label = None
        if "andres manuel" in participante:
            label = "amlo"
        
        if label:
            dialogos_speakers.extend(
                [(label, dialogo, len(dialogo)) for dialogo in participación.dialogos]
            )

dialogos_df = pd.DataFrame(dialogos_speakers, columns=["speaker", "dialog", "length"])
data = dialogos_df["dialog"].str.cat(sep="\n")

n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
