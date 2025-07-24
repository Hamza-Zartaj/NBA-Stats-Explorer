import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def create_basic_visualizations(df_selected_team):
    if df_selected_team.empty:
        st.warning("No data available for visualizations.")
        return

    # Create a copy to avoid SettingWithCopyWarning
    df_selected_team = df_selected_team.copy()

    # 🎯 Scoring Efficiency
    st.header('🎯 Scoring Efficiency Analysis')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df_selected_team, x='FGA', y='PTS', hue='Pos', ax=ax)
    st.pyplot(fig)

    # 🏀 Assist-to-Turnover Ratio
    st.header('🏀 Assist-to-Turnover Ratio Analysis')
    st.write("Assessing playmaking efficiency through the Assist-to-Turnover Ratio (AST/TOV).")
    df_selected_team['AST_to_TOV'] = df_selected_team['AST'] / (df_selected_team['TOV'] + 1e-9)
    top_ast_tov = df_selected_team[['Player', 'AST_to_TOV']].sort_values(by='AST_to_TOV', ascending=False).head(10)
    st.write("Top 10 Players by Assist-to-Turnover Ratio:")
    st.dataframe(top_ast_tov, use_container_width=True)

    # ⚡ Free Throw Efficiency
    st.header('⚡ Free Throw Efficiency Analysis')
    st.write("Comparing Free Throw Percentage (FT%) with Free Throw Attempts (FTA).")
    df_selected_team['FT%'] = pd.to_numeric(df_selected_team['FT%'], errors='coerce')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df_selected_team, x='FTA', y='FT%', hue='Pos', ax=ax)
    ax.set_title("Free Throw Efficiency: FT% vs. FTA")
    ax.set_xlabel("Free Throw Attempts (FTA)")
    ax.set_ylabel("Free Throw Percentage (FT%)")
    st.pyplot(fig)

    # 🧑‍🤝‍🧑 Starters vs Bench
    st.header('🧑‍🤝‍🧑 Starters vs. Bench Players Analysis')
    st.write("Comparing performance metrics between starters and bench players.")
    df_selected_team['Role'] = df_selected_team['GS'].apply(lambda x: 'Starter' if x > 0 else 'Bench')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_selected_team, x='Role', y='PTS', ax=ax)
    ax.set_title("Points Scored: Starters vs. Bench Players")
    st.pyplot(fig)

    # 🤾‍♂️ Shooting Efficiency
    st.header('🤾‍♂️ Shooting Efficiency by Position')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_selected_team, x='Pos', y='FG%', ax=ax)
    ax.set_title("Field Goal Percentage by Position")
    st.pyplot(fig)

    # ⛹️‍♂️ Rebounding by Position
    st.header('⛹️‍♂️ Rebounding Analysis by Position')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_selected_team, x='Pos', y='TRB', ax=ax)
    ax.set_title("Total Rebounds by Position")
    st.pyplot(fig)

    # 🔥 Intercorrelation Matrix
    st.header("🔥 Intercorrelation Matrix Heatmap")
    numeric_df = df_selected_team.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(10, 8))
    with sns.axes_style("white"):
        sns.heatmap(corr, mask=mask, vmax=1, square=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # 🏆 Awards and Performance
    st.header("🏆 Awards and Performance")
    awards_analysis = df_selected_team.groupby('Player')[['PTS', 'Awards']].sum().sort_values(by='PTS', ascending=False)
    st.dataframe(awards_analysis, use_container_width=True)

    # ⛹️‍♀️ Points per Minute
    st.header("⛹️‍♀️ Scoring Efficiency (Points per Minute)")
    df_selected_team['PTS_per_Min'] = df_selected_team['PTS'] / df_selected_team['MP']
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df_selected_team, x='MP', y='PTS', hue='Pos', ax=ax)
    st.pyplot(fig)
