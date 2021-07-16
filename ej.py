import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = r'C:\Users\Mateo Sceia\Documents\Facultad Mateo\2do Año\1er Cuatri\Fundamentos de Informatica\datasets\Datos.csv'
datos = pd.read_csv(path)
print(datos)


print(datos.isnull().sum())
print(datos.dropna(inplace=True))

print(datos.fillna(datos['Sueldo'].mean(), inplace=True)) 
print(datos.fillna(datos['Altura'].mean(), inplace=True))


print(datos['Sueldo'].mean())
print(datos['Sueldo'].mode())
print(datos['Sueldo'].median())

print(datos['Altura'].median())
print(datos['Altura'].mean())
print(datos['Altura'].mode())

df2 = datos.sort_values(by = ["Sueldo"], ascending = False, ignore_index = True).head(10)
print(df2)

df3 = datos.sort_values(by = ["Altura"], ascending = False, ignore_index = True).head(10)
print(df3)
 
print(datos.drop_duplicates(inplace=True))

f = sns.histplot(data = datos, x = "Sueldo", binwidth=0.25, kde = True, color= 'orange')
print(f)
plt.show()