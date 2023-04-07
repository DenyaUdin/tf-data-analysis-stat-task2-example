import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 706552449 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = 2*(x-0.077).mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 0.077 + loc + 2*scale * norm.ppf(alpha)/np.sqrt(len(x)), \
           0.077 + loc + 2*scale * norm.ppf(1 -alpha)/np.sqrt(len(x))
