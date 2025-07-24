import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from ml.predictor import NBAPlayerPredictor
from ml.ai_insights import NBAInsightsAI

def add_ai_features_ui(df, selected_year):
    st.header("🤖 AI-Powered Insights")
    ai_tab1, ai_tab2 = st.tabs(["Player Similarity", "Performance Prediction"])

    try:
        nba_ai = NBAInsightsAI(df)
    except Exception as e:
        st.error("Error initializing AI models. Please check the data or try again later.")
        return

    with ai_tab1:
        st.subheader("Find Similar Players")
        selected_player = st.selectbox("Select a player:", df['Player'].unique())
        if selected_player:
            similar_players = nba_ai.find_similar_players(selected_player)
            if not similar_players.empty:
                fig = px.bar(similar_players,
                             x='Player',
                             y='Similarity Score',
                             color='Position',
                             title=f"Players Similar to {selected_player}")
                st.plotly_chart(fig)
                st.dataframe(similar_players)

    with ai_tab2:
        st.subheader("Performance Prediction")
        pred_player = st.selectbox("Select player for prediction:", df['Player'].unique(), key='pred_player')

        predictor = NBAPlayerPredictor()
        try:
            predictor.load_historical_data(range(selected_year-3, selected_year+1))
        except Exception as e:
            st.error(f"Error loading historical data: {e}")
            return
        if pred_player:
            results = predictor.predict_future_performance(pred_player)
            if isinstance(results, tuple):
                st.warning(results[1])
            elif results:
                categories = ['Points', 'Assists', 'Rebounds']
                current_stats = [results['current_stats']['PTS'], results['current_stats']['AST'], results['current_stats']['TRB']]
                predicted_stats = [results['predictions']['PTS'], results['predictions']['AST'], results['predictions']['TRB']]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=current_stats, theta=categories, fill='toself', name='Current Stats'))
                fig.add_trace(go.Scatterpolar(r=predicted_stats, theta=categories, fill='toself', name='Predicted Stats'))

                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, max(max(current_stats), max(predicted_stats))])),
                    showlegend=True,
                    title=f"Performance Prediction for {pred_player}"
                )
                st.plotly_chart(fig)

