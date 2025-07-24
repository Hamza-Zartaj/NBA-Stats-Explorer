import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from data.loader import load_historical_data

class NBAPlayerPredictor:
    def __init__(self):
        self.historical_data = {}
        self.scaler = StandardScaler()
        self.feature_cols = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
                             '3PA', '3P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']

    def load_historical_data(self, years_range):
        self.historical_data = load_historical_data(years_range)
        for col in self.feature_cols:
            if col in self.historical_data.columns:
                self.historical_data[col] = pd.to_numeric(self.historical_data[col], errors='coerce')

    def get_player_history(self, player_name):
        return self.historical_data[self.historical_data['Player'] == player_name].sort_values('Year')

    def prepare_prediction_features(self, player_history):
        if len(player_history) < 2:
            return None
        recent_seasons = player_history.sort_values('Year').tail(3)
        features = {}
        for col in self.feature_cols:
            features[f'{col}_last'] = recent_seasons[col].iloc[-1]
            features[f'{col}_avg'] = recent_seasons[col].mean()
            features[f'{col}_trend'] = recent_seasons[col].diff().mean()
        features['seasons_played'] = len(player_history)
        features['age'] = recent_seasons['Age'].iloc[-1]
        return pd.DataFrame([features])

    def predict_future_performance(self, player_name):
        player_history = self.get_player_history(player_name)
        if len(player_history) < 2:
            return None, "Insufficient historical data for prediction"
        X = self.prepare_prediction_features(player_history)
        if X is None:
            return None, "Could not prepare prediction features"

        predictions = {}
        confidence_scores = {}

        for stat in ['PTS', 'AST', 'TRB']:
            all_features, all_targets = [], []
            for player in self.historical_data['Player'].unique():
                ph = self.get_player_history(player)
                if len(ph) >= 3:
                    features = self.prepare_prediction_features(ph.iloc[:-1])
                    if features is not None:
                        all_features.append(features)
                        all_targets.append(ph[stat].iloc[-1])
            if all_features:
                X_train = pd.concat(all_features, ignore_index=True)
                y_train = np.array(all_targets)
                model = RandomForestRegressor(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)
                pred = model.predict(X)[0]
                predictions[stat] = pred
                confidence_scores[stat] = model.score(X_train, y_train)

        return {
            'predictions': predictions,
            'confidence_scores': confidence_scores,
            'current_stats': {stat: player_history[stat].iloc[-1] for stat in ['PTS', 'AST', 'TRB']},
            'historical_trend': {stat: player_history[stat].tolist() for stat in ['PTS', 'AST', 'TRB']}
        }
