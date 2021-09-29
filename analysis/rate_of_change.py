import pandas as pd
import numpy as np

def rate_of_change(dict):
    s = pd.Series(dict)
    result = s.pct_change().replace([np.inf, -np.inf, np.nan], 0).to_dict()
    print(result)
    return result
