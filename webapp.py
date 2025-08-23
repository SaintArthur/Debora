import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Distribuição do FUNDEB/FUNDEPE",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Distribuição do FUNDEB/FUNDEPE")
st.markdown("#### Por: **Debora**")
st.markdown("---")

st.header("🎯 Objetivo do App")
st.write("""
O presente aplicativo tem como objetivo **consultar e visualizar** 
informações sobre a distribuição do **FUNDEB/FUNDEPE** no Brasil.  

O **FUNDEB** é o principal fundo de financiamento da educação básica, 
e o **MEC** publica **portarias trimestrais** que detalham:
- Recursos recebidos por estado;
- Complementações da União;
- Matrículas por município;
- Distribuição consolidada final.  

Este app servirá de protótipo para explorar esses dados de forma 
simples, interativa e acessível.
""")

st.markdown("---")

st.header("📌 Estrutura do App")

with st.expander("🔍 Consulta por Município e Ano"):
    st.write("Permite selecionar o município e o ano para visualizar os dados de matrículas e valores recebidos.")

with st.expander("📈 Visualização dos Dados"):
    st.write("Gráficos interativos para comparar a distribuição dos recursos entre municípios e estados.")

with st.expander("📂 Relatórios"):
    st.write("Geração futura de relatórios exportáveis (PDF/CSV/XLSX) com base na consulta realizada.")

st.markdown("---")

st.header("📚 Bases de Dados Previstas")
st.write("""
As principais fontes de dados serão:
- **Portarias do MEC sobre FUNDEB/FUNDEPE** (publicadas anualmente e atualizadas a cada 3 meses);
- **Anexos das Portarias**:  
   - Anexo I: Valores repassados por Estado;  
   - Anexo II: Complementações da União;  
   - Anexo III: Matrículas por Município;  
   - Anexo IV: Distribuição consolidada final.  
""")

st.markdown("---")

st.header("🖥️ Demonstração (com dados fictícios)")

col1, col2 = st.columns(2)
with col1:
    municipio = st.selectbox("Selecione o Município:", ["Fortaleza", "São Paulo", "Salvador", "Belo Horizonte"])
with col2:
    ano = st.selectbox("Selecione o Ano:", [2022, 2023, 2024])

dados_demo = {
    ("Fortaleza", 2023): {"matriculas": 350000, "valor": 2_450_000_000},
    ("São Paulo", 2023): {"matriculas": 1200000, "valor": 9_800_000_000},
    ("Salvador", 2023): {"matriculas": 420000, "valor": 2_950_000_000},
    ("Belo Horizonte", 2023): {"matriculas": 310000, "valor": 2_100_000_000},
}

resultado = dados_demo.get((municipio, ano), {"matriculas": "N/D", "valor": "N/D"})

st.subheader(f"📌 Dados simulados para {municipio} em {ano}:")

# ✅ Correção para evitar erro de formatação
matriculas = resultado["matriculas"]
valor = resultado["valor"]

if isinstance(matriculas, int):
    matriculas_fmt = f"{matriculas:,}".replace(",", ".")
else:
    matriculas_fmt = matriculas

if isinstance(valor, int):
    valor_fmt = f"R$ {valor:,}".replace(",", ".")
else:
    valor_fmt = valor

st.metric("Número de Matrículas", matriculas_fmt)
st.metric("Valor FUNDEB/FUNDEPE Recebido", valor_fmt)

st.info("⚠️ Obs: Estes valores são **simulações fictícias**. Futuramente serão substituídos pelos dados oficiais do MEC.")

st.markdown("---")

st.header("✅ Conclusão")
st.write("""
Este app é um **protótipo inicial**.  
As próximas etapas de desenvolvimento incluirão:
- Carregamento dos dados reais a partir das portarias do MEC;
- Criação de gráficos interativos (barras, linhas, mapas);
- Exportação de relatórios em PDF e Excel.

Com isso, será possível **facilitar a análise** da distribuição dos recursos 
e apoiar a gestão
