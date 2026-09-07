# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] editable=true slideshow={"slide_type": ""}
# # Relatórios de cliques e vendas

# %%
import pandas as pd

path_erp_vendas = "./dados/erp_vendas.csv"
path_relatorio_marketing = "./dados/relatorio_marketing.csv"
df_erp_vendas = pd.read_csv(path_erp_vendas)
df_relatorio_marketing = pd.read_csv(path_relatorio_marketing)

# %%
df_erp_vendas.head(7)

# %%
df_erp_vendas.info()

# %%
df_relatorio_marketing.head(7)

# %%
df_relatorio_marketing.info()

# %% [markdown]
# # Ajuste dType Column "data"

# %%
#df_erp_vendas['data_venda'] = df_erp_vendas['data_venda'].astype('datetime64[ns]')
df_erp_vendas['data_venda'] = pd.to_datetime(df_erp_vendas['data_venda'], errors='coerce')

#df_relatorio_marketing['data'] = df_relatorio_marketing['data'].astype('datetime64[ns]')
df_relatorio_marketing['data'] = pd.to_datetime(df_relatorio_marketing['data'], errors='coerce')


# %%
df_erp_vendas.info()

# %%
df_relatorio_marketing.info()

# %% [markdown]
# # Fixing key before merge

# %%
df_relatorio_marketing['id_transacao'] = df_relatorio_marketing['id_transacao'].str.replace('TRX-','').astype('int64')
df_relatorio_marketing.info()

# %% [markdown]
# # Merging dfs

# %%
df_erp_vendas.head(7)

# %%
df_relatorio_marketing.head(7)

# %%
#df_erp_vendas['data_venda'] = df_erp_vendas['data_venda'].astype('datetime64[ns]')
df_erp_vendas['data_venda'] = pd.to_datetime(df_erp_vendas['data_venda'], errors='coerce')

#df_relatorio_marketing['data'] = df_relatorio_marketing['data'].astype('datetime64[ns]')
df_relatorio_marketing['data'] = pd.to_datetime(df_relatorio_marketing['data'], errors='coerce')


# %%
df_compare_erp_relatorio = pd.merge(
    df_erp_vendas, 
    df_relatorio_marketing, 
    left_on='id_pedido', 
    right_on='id_transacao', 
    how='outer', 
    suffixes=("_erp", "_mkt")
)
 
df_compare_erp_relatorio

# %%
df_compare_erp_relatorio.drop(columns='produto_mkt', inplace=True)

# %% [markdown]
# # Checking Empty IDs

# %%
df_id_pedido_nas = df_compare_erp_relatorio[df_compare_erp_relatorio["id_pedido"].isna()]
df_id_pedido_nas

# %%
df_id_transacao_nas = df_compare_erp_relatorio[df_compare_erp_relatorio["id_transacao"].isna()]
df_id_transacao_nas

# %% [markdown]
# # Checking Payment Issue

# %%
df_status_pagamento_not_Pago = df_compare_erp_relatorio["status_pagamento"] != "Pago"
df_status_pagamento_payment_issue = df_compare_erp_relatorio[df_status_pagamento_not_Pago]
df_status_pagamento_payment_issue

# %% [markdown]
# # Checking Price Issue

# %%
s_valor_real = df_compare_erp_relatorio["valor_real"]
s_valor_conversao = df_compare_erp_relatorio["valor_conversao"]
df_compare_s_valor_conversao = s_valor_real.compare( s_valor_conversao, result_names=("valor","conversao") )
df_compare_s_valor_conversao

# %% [markdown]
# # Shortening price comparison

# %%
df_price_comparison = s_valor_real != s_valor_conversao

# %%
df_overview_issues = df_compare_erp_relatorio[ 
    (df_status_pagamento_not_Pago) 
    | 
    (s_valor_real != s_valor_conversao) 
]
df_overview_issues

# %%
df_overview_issues.to_csv("./dados/relatorio_fraudes.csv")

# %%
