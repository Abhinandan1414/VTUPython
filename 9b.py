# import pandas lib as pd
import pandas as pd
from pandas import DataFrame

df1 = pd.read_excel('Book1.xlsx')

print(df1)

#df2 = pd.DataFrame({"5":[6, "GH", 33, "EC", 45],"6":[7, "IJ", 37, "CS", 90]})

df2 = pd.DataFrame({"SI. NO":[ 6, 7],
                    "Name":["GH","IJ"],
                    "Age" : [33,37],
                    "Stream": ["EC","CS"],
                    "Percentage":[45,90]})


df_concat = pd.concat([df1, df2], ignore_index=True,axis=0)

df_concat.to_excel("Book2.xlsx")

dataframe4 = pd.read_excel("Book2.xlsx")

print(dataframe4)
