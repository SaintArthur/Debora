import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# CONFIGURAÇÃO DO APP
# =====================================================
st.set_page_config(
    page_title="Distribuição do FUNDEB/FUNDEPE",
    page_icon="📊",
    layout="wide"
)

# Estilo customizado para deixar o app moderno
st.markdown("""
<style>
    .big-font {
        font-size:28px !important;
        font-weight: bold;
        color: #2E86C1;
    }
    .metric-container {
        background-color: #F8F9F9;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================
# CABEÇALHO
# =====================================================
st.title("📊 Distribuição do FUNDEB/FUNDEPE")
st.markdown("<p class='big-font'>Por: Débora</p>", unsafe_allow_html=True)
st.markdown("---")

# =====================================================
# OBJETIVO
# =====================================================
st.header("🎯 Objetivo do App")
st.info("""
O presente aplicativo tem como objetivo **consultar e visualizar** informações sobre a distribuição do **FUNDEB/FUNDEPE** no Brasil.  

O **FUNDEB** é o principal fundo de financiamento da educação básica, e o **MEC** publica portarias trimestrais que detalham:
- Recursos recebidos por estado;
- Complementações da União;
- Matrículas por município;
- Distribuição consolidada final.  

Este app é um **protótipo interativo** para simular como essas informações podem ser apresentadas de forma visual e acessível.
""")

st.markdown("---")

# =====================================================
# DEMONSTRAÇÃO COM DADOS FICTÍCIOS
# =====================================================
st.header("🖥️ Demonstração Interativa")

col1, col2 = st.columns(2)
with col1:
    municipio = st.selectbox("🏙️ Selecione o Município:", ["Fortaleza", "São Paulo", "Salvador", "Belo Horizonte"])
with col2:
    ano = st.selectbox("📅 Selecione o Ano:", [2022, 2023, 2024])

dados_demo = {
    ("Fortaleza", 2023): {"matriculas": 350000, "valor": 2450000000},
    ("São Paulo", 2023): {"matriculas": 1200000, "valor": 9800000000},
    ("Salvador", 2023): {"matriculas": 420000, "valor": 2950000000},
    ("Belo Horizonte", 2023): {"matriculas": 310000, "valor": 2100000000},
}

resultado = dados_demo.get((municipio, ano), {"matriculas": "N/D", "valor": "N/D"})

# Exibir métricas em cards estilizados
colA, colB = st.columns(2)
with colA:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    matriculas_fmt = f"{resultado['matriculas']:,}".replace(",", ".") if isinstance(resultado['matriculas'], int) else resultado['matriculas']
    st.metric("Número de Matrículas", matriculas_fmt)
    st.markdown("</div>", unsafe_allow_html=True)

with colB:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    valor_fmt = f"R$ {resultado['valor']:,}".replace(",", ".") if isinstance(resultado['valor'], int) else resultado['valor']
    st.metric("Valor Recebido", valor_fmt)
    st.markdown("</div>", unsafe_allow_html=True)

st.info("⚠️ Obs: Estes valores são **simulações fictícias**. Futuramente serão substituídos pelos dados oficiais do MEC.")

# =====================================================
# VISUALIZAÇÃO GRÁFICA
# =====================================================
st.header("📈 Visualização dos Dados (Fictícios)")

df_demo = pd.DataFrame([
    {"Município": "Fortaleza", "Ano": 2023, "Matrículas": 350000, "Valor": 2450000000},
    {"Município": "São Paulo", "Ano": 2023, "Matrículas": 1200000, "Valor": 9800000000},
    {"Município": "Salvador", "Ano": 2023, "Matrículas": 420000, "Valor": 2950000000},
    {"Município": "Belo Horizonte", "Ano": 2023, "Matrículas": 310000, "Valor": 2100000000},
])

fig = px.bar(df_demo, x="Município", y="Valor", color="Município",
             labels={"Valor": "Valor Recebido (R$)", "Município": "Cidade"},
             title="Distribuição Fictícia de Recursos FUNDEB 2023")

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# CONCLUSÃO
# =====================================================
st.header("✅ Conclusão")
st.success("""
Este app é um **protótipo inicial** que já mostra:
- Layout moderno e interativo;
- Seleção dinâmica de município e ano;
- Indicadores em destaque (cards);
- Gráfico interativo com Plotly.

As próximas etapas incluirão:
- Integração com dados reais do MEC;
- Mapas interativos (geolocalização);
- Exportação de relatórios em PDF/Excel.

Dessa forma, será possível **facilitar a análise da distribuição dos recursos** e apoiar a gestão educacional em estados e municípios.
""")
