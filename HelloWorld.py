import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Pokemon.csv')


#vamos analisar as informações do nosso arquivo
 

print()
print(df.info())
print()

print(df.head())
print()
print(df.tail())


print()
print(f'Quantidades de valores presentes {df.shape}')
print()


#alterar as colunas para facilitar a nossa vida 
df.columns = ['#','Nome','Tipo 1','Tipo 2', 'Total', 'HP', 'Ataque', 'Defesa', 'Sp.Ata', 'Sp.Def','Velocidade', 'Geracao', 'Lendario']
print(df.head(n=2))
#agora vamos ver quais são os melhores e piores 
print()


stats = ['Ataque','Defesa','Sp.Ata']

def max_stats(df, col_list):
    
    saida =''
    for col in col_list:
        stat = df[col].max()
        name = df[df[col]==df[col].max()]['Nome'].values[0]
        saida += name + ' possui o/a maior '+col+ ' com '+ str(stat)+'.\n'
    return saida
    

print(max_stats(df,stats))

def min_stats(df,col_list):
    saida = ''
    for col in col_list:
        stat = df[col].min()
        name = df[df[col]==df[col].min()]['Nome'].values[0]
        saida += name + ' possui o/a menor '+col+ ' com '+ str(stat)+'.\n'
    return saida

print(min_stats(df,stats))








types = df["Tipo 1"].unique()

def barh_stats():
    plt.figure(figsize=(15,5))
    plt.suptitle('Statistics', fontsize=15)

    for t in types:

        #Plotting Mean
        plt.subplot(121)
        plt.title('Mean')
        df[df['Tipo 1']==t].mean().plot(kind='barh')

        #Plotting Standard Deviation
        plt.subplot(122)
        plt.title('Standard Deviation')
        df[df['Tipo 1']==t].std().plot(kind='barh')


barh_stats()