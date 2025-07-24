from components.header import show_header
from data.loader import load_data
from components.download import filedownload
from ml.predictor import NBAPlayerPredictor
from ml.ai_insights import NBAInsightsAI
from components.ai_features import add_ai_features_ui
from visualization.charts import create_basic_visualizations

import streamlit as st

def main():
    st.set_page_config(page_title="NBA Stats Explorer", layout="wide")
    show_header()

    st.sidebar.header('User Input Features')
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(1980, 2025))))

    playerstats = load_data(selected_year)

    sorted_unique_team = sorted(playerstats.Team.unique())
    selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team[:4])

    unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
    selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos[:3])

    df_selected_team = playerstats[(playerstats.Team.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

    st.header('📊 Basic Player Stats')
    tab1, tab2 = st.tabs(["Player Stats", "AI Features"])

    with tab1:
        st.dataframe(df_selected_team, use_container_width=True)
        st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
        create_basic_visualizations(df_selected_team)

    with tab2:
        if not df_selected_team.empty:
            add_ai_features_ui(df_selected_team, selected_year)

if __name__ == "__main__":
    main()
