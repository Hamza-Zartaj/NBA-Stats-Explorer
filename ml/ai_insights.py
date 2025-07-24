import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

class NBAInsightsAI:
    def __init__(self, df):
        self.df = df
        self.feature_cols = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
                             '3PA', '3P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']
        self.scaler = StandardScaler()
        self.scaler.fit(df[self.feature_cols])

    def prepare_features(self, data):
        return self.scaler.transform(data[self.feature_cols])

    def find_similar_players(self, player_name, n_neighbors=5):
        X = self.prepare_features(self.df)
        X = pd.DataFrame(X).reset_index(drop=True)
        aligned_df = self.df.reset_index(drop=True)
        if player_name not in aligned_df['Player'].values:
            raise ValueError(f"Player '{player_name}' not found in the dataset.")
        nbrs = NearestNeighbors(n_neighbors=n_neighbors+1, metric='euclidean')
        nbrs.fit(X)
        idx = aligned_df[aligned_df['Player'] == player_name].index[0]
        distances, indices = nbrs.kneighbors(X.iloc[idx].values.reshape(1, -1))
        similar_players = aligned_df.iloc[indices[0][1:]]
        similarity_scores = 1 / (1 + distances[0][1:])
        return pd.DataFrame({
            'Player': similar_players['Player'].values,
            'Similarity Score': similarity_scores,
            'Position': similar_players['Pos'].values
        })
