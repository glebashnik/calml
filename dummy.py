import numpy as np
import pandas as pd

class Dummies:
    def __init__(self):
        self.col_vals = {}
        
    def fit(self, df, cols):
        for col in cols:
            self.col_vals[col] = np.sort(df[col].unique())
            
        return self.col_vals
        
    def replace(self, df):
        for col in self.col_vals.keys():
            dummies = pd.get_dummies(df[col], prefix=col, drop_first=False)
            df = pd.concat([df, dummies], axis=1)
            
        df.drop(self.col_vals.keys(), axis=1)
        
        for col, vals in self.col_vals.items():
            for val in vals:
                col_val =  col + '_' + str(val)
                
                if col_val not in df.columns:
                    df[col_val] = 0
                
        return df.drop(self.col_vals.keys(), axis=1)