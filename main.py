import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


ruta = "dataset_banco.csv"
data = pd.read_csv(ruta)

print('=====================================================')
print(data.shape)
data.head()

print('=====================================================')
# Vizualizar variables categóricas y las numericas 
data.info()

print('=====================================================')
# Limpieza

#Datos faltantes 
data.dropna(inplace=True)
data.info()

print('=====================================================')
#Columnas irrelevantes 
#(Conteo de los niveles en las diferentes columnas categoricas)
cols_cat = ['job', 'marital', 'education', 'default', 
            'housing', 'loan', 'contact', 'month', 'poutcome', 'y']

for col in cols_cat: 
    print(f'Columna {col}: {data[col].nunique()} subniveles')

data.describe()

