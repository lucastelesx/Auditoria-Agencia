# Auditoria de Agência - Reconciliação Financeira & Detecção de Anomalias

Projeto de análise de dados e auditoria contábil/financeira para reconciliação entre relatórios de conversão de agências de marketing e vendas reais registradas no ERP.

## Objetivo do Projeto
Empresas que contratam agências de marketing e afiliados frequentemente enfrentam discrepâncias entre os valores cobrados por conversões e as vendas efetivamente pagas no sistema interno (ERP). 

Este projeto cruza as duas fontes de dados (ETL) para:
1. **Identificar Pedidos Fantasmas**: Conversões aprovadas pela agência que não constam no ERP.
2. **Divergências de Valor**: Pedidos registrados com valores diferentes entre marketing e faturamento.
3. **Fraudes e Inadimplência**: Pedidos cancelados, estornados ou boletos vencidos que foram indevidamente comissionados.
4. **Cálculo de Reembolso/Chargeback**: Total monetário a ser glosado ou recuperado junto à agência.

## Tecnologias Utilizadas
- **Python 3.12**
- **Pandas**: Limpeza de chaves (`str.replace`), coerção de datas (`pd.to_datetime`), merges relacionais (`left`/`outer`), filtros booleanos e máscaras lógicas.
- **Jupyter Notebook**: Análise exploratória interativa e documentação do fluxo de auditoria.

## Estrutura do Repositório
```text
.
├── dados/
│   ├── erp_vendas.csv           # Dados de faturamento interno do ERP
│   ├── relatorio_marketing.csv  # Relatório de conversões da agência
│   └── relatorio_fraudes.csv    # Saída com as inconsistências identificadas
├── auditoria.ipynb              # Notebook executável com a pipeline de auditoria
├── auditoria.py                 # Script Python estruturado
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação do projeto
```

## Como Executar

1. Clone o repositório:
```bash
git clone git@github.com:lucastelesx/auditoria_agencia.git
cd auditoria_agencia
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o script ou abra o notebook:
```bash
python auditoria.py
# ou
jupyter notebook auditoria.ipynb
```

---
Desenvolvido por [Lucas Telles](https://github.com/lucastelesx).
