import numpy as np
import pandas as pd

def alimentos_gr(des2, p_gr):
    des2["Energia(kcal)"] = des2["Energia(kcal)"] * p_gr
    des2["Grasas"] = des2["Grasas"] * p_gr
    des2["Proteina"] = des2["Proteina"] * p_gr
    des2["Carbohidratos"] = des2["Carbohidratos"] * p_gr
    return des2

def concatenar(comida, desayuno, cena, otros):
    a_concatenar = []
    for i in [comida, desayuno, cena, otros]:
        if isinstance(i, pd.DataFrame):
            a_concatenar.append(i)
    alimentos_dia = pd.concat(a_concatenar)
    return alimentos_dia