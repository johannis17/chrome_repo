import logging
import numpy as np
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def func(x:int):
    return x + 1

def ppppp(df:pd.DataFrame):
    logging.info(df.columns)
    
    
def test_answer():
    assert func(3) == 4
    


func(3)

df1= pd.DataFrame({'a':[1,1,1,1,1]})

ppppp(df1)