# case de cancelamento

# PYTHON INSIGHTS

# importação de base de dados
# visualização da base de dados

import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")
display(tabela)

# resolução da base de dados
# tratamento de valores vazio
# linha -. axil = 0
# linha -> axil = 1

tabela = tabela.dropna()
tabela = tabela.drop("CustomerID", axis=1)

# analisar a base de dados (cancelamento)

display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

display(tabela.groupby("duracao_contrato").mean())
display(tabela.groupby("assinatura").mean())
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]

# show so funiciona no grafico

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

# se aprofundar nas informação de dados

tabela = tabela[tabela["ligacoes_callcenter"] < 5]
tabela = tabela[tabela["dias_atraso"] < 20]
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
# forma de pagamento - mensal
# dias de atraso > 20
# ligacoes do call center ›= 5
# se aprofundar nas informação de dados
