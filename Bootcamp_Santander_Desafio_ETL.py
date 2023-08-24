# Site do banco de dados: https://dadosabertos.bcb.gov.br/dataset/7384-vendas-de-veiculos-pelas-concessionarias---automoveis
# URL de Download da BD (Renomear para teste2.csv): https://api.bcb.gov.br/dados/serie/bcdata.sgs.7384/dados?formato=csv
# BD = Série temporal mensal das vendas de veículos pelas concessionárias - Automóveis

# importação da Lib Pandas
import pandas as pd


# EXTRACT
# LEITURA DO ARQUIVO CSV (COLOCÁ-LO NA MESMA PASTA DESTE ARQUIVO)
tabela = pd.read_csv("teste2.csv", sep=";")


# TRANSFORMATION
# TRANSFORMAÇÃO EM DATAFRAME
tabela_df = pd.DataFrame(tabela)

# TRANSFORMA A COLUNA 'Data' DE FORMATO 'Str' PARA 'Datetime'
tabela_df['data'] = pd.to_datetime(tabela_df['data'])

# SEPARAÇÃO DA COLUNA 'data' EM ANO
tabela_df['year'] = tabela_df['data'].dt.year

# SOMATÓRIA DA QUANTIDADE DAS VENDAS DE VEÍCULOS
tabela_df_vendas_ano = tabela_df.groupby(
    'year', as_index=False).sum('valor')

# EXIBIÇÃO DO RESULTADO
print('Quantidade de veículos vendidos, no Brasil, por ano')
print(tabela_df_vendas_ano)


# LOAD (CARREGAMENTO)
tabela_df_vendas_ano.to_csv(
    'vendas_veiculos_por_ano.csv', sep=',', index=False)
