import pandas as pd
import numpy as np
import random as rd

dik = pd.read_csv('diksi_rep.csv')
pd.set_option('display.max_rows', 207)
dik.replace('None', np.nan, inplace=True)
dik.dropna(how="any", inplace=True)

def carib(text):
    try:   
        output = dik[dik['bind'].str.match(text)].values
        if text != output[-1][0]:
            return f"'{text}' kurang spesifik"
        else:
            return f"{output[-1][1]}"
    except:
        if IndexError:
            try:
                textr = text[0:3]
                output = dik[dik['bind'].str.match(textr)].values[rd.choice([0,-1])][0]
            except:
                if IndexError:
                    return "kata tidak ditemukan!"
            nanni = [f"Mungkin maksud anda {output}",f"Mungkin maksud anda {output}","Maaf kata tidak ditemukan"]
            return rd.choice(nanni)