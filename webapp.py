import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# CONFIGURAÇÃO DO APP
# =====================================================
st.set_page_config(
    page_title="Distribuição dos recursos do FUNDEB",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# BARRA LATERAL DE NAVEGAÇÃO
# =====================================================
st.sidebar.title("📚 Seções")
menu = st.sidebar.radio(
    "Navegação",
    [
        "Início",
        "Panorama FUNDEB",
        "Ranking de Municípios",
        "Evolução Temporal",
        "Comparador",
        "Metodologia & Fontes"
    ]
)

# =====================================================
# ESTILO CUSTOMIZADO
# =====================================================
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
# CONTEÚDO DAS SEÇÕES
# =====================================================
if menu == "Início":
    st.title("📊 Distribuição dos recursos do FUNDEB")
    st.markdown("<p class='big-font'>Por: Débora Resende Maranhão</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.header("🎯 Objetivo do App")
    st.info("""
    Este aplicativo tem como objetivo **consultar e visualizar** informações sobre a distribuição do **FUNDEB** no Brasil.  

    O **FUNDEB** é o principal fundo de financiamento da educação básica, e o **MEC** publica portarias trimestrais que detalham:
    - Recursos recebidos por estado/município/rede de ensino;
    - Complementações da União (VAAF, VAAT e VAAR);
    - Matrículas ponderadas por município;
    - Distribuição consolidada final.  

    Este app é um **protótipo interativo** para mostrar como essas informações podem ser apresentadas de forma visual e acessível.
    """)

elif menu == "Panorama FUNDEB":
    st.header("📊 Distribuição de Recursos (Exemplo)")

    dados = {
        "ANO": ["2022", "2022", "2022", "2022"],
        "Estado": ["ES", "MG", "BA", "SP"],
        "Matrículas ponderadas": [82000, 145000, 132000, 210000],
        "Complementação VAAF(R$ mi)": [2000, 45000, 13000, 2100],
        "Complementação VAAR(R$ mi)": [0, 5000, 12000, 360000],
        "Valor FUNDEB (R$ mi)": [84000, 195000, 157000, 7200]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)

elif menu == "Ranking de Municípios":
    st.header("🏆 Ranking de Municípios (Em Desenvolvimento)")
    st.warning("Esta seção está em construção. Futuramente mostrará o ranking de municípios com base nos repasses do FUNDEB.")

elif menu == "Evolução Temporal":
    st.header("📈 Evolução Temporal dos Recursos (Fictícios)")

    df_demo = pd.DataFrame([
        {"Município": "Fortaleza", "Ano": 2022, "Valor": 2350000},
        {"Município": "Fortaleza", "Ano": 2023, "Valor": 2450000},
        {"Município": "Fortaleza", "Ano": 2024, "Valor": 2550000},
        {"Município": "São Paulo", "Ano": 2022, "Valor": 9400000},
        {"Município": "São Paulo", "Ano": 2023, "Valor": 9800000},
        {"Município": "São Paulo", "Ano": 2024, "Valor": 10200000},
    ])
    fig = px.line(df_demo, x="Ano", y="Valor", color="Município",
                  title="Evolução Fictícia dos Recursos FUNDEB (2022–2024)",
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Comparador":
    st.header("⚖️ Comparador de Municípios")
    municipio1 = st.selectbox("Município 1", ["Fortaleza", "São Paulo", "Salvador", "Belo Horizonte"])
    municipio2 = st.selectbox("Município 2", ["Fortaleza", "São Paulo", "Salvador", "Belo Horizonte"])
    ano = st.selectbox("Ano", [2022, 2023, 2024])
    st.info(f"Comparando {municipio1} e {municipio2} no ano de {ano} (dados fictícios).")

elif menu == "Metodologia & Fontes":
    st.header("📘 Metodologia & Fontes")
    st.markdown("""
    **Fontes dos Dados:**
    - Portarias do MEC/FNDE sobre o FUNDEB;
    - Censo Escolar (INEP);
    - Dados simulados para prototipagem.

    **Metodologia:**
    - Limpeza e padronização em Python (pandas);
    - Visualização interativa (Plotly e Streamlit);
    - Estrutura modular com sidebar para navegação.
    """)

st.sidebar.markdown("---")
st.sidebar.info("💡 Desenvolvido como protótipo educacional em Streamlit.")
