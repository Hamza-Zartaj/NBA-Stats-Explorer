import pandas as pd
import streamlit as st

@st.cache_data
def load_data(year):
    try:
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
        df = pd.read_html(url, header=0)[0]
        df = df[df['Age'] != 'Age'].fillna(0)
        df.drop(['Rk'], axis=1, inplace=True, errors='ignore')
        df['Awards'] = df['Awards'].astype(str)
        return df[df['Team'] != 0]
    except Exception as e:
        st.error(f"Error loading data for year {year}: {e}")
        return pd.DataFrame()

@st.cache_data
def load_historical_data(years_range):
    all_data = []
    for year in years_range:
        try:
            url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
            df = pd.read_html(url, header=0)[0]
            df = df[df['Age'] != 'Age'].fillna(0)
            df['Year'] = year
            all_data.append(df)
        except Exception as e:
            st.warning(f"Could not load data for year {year}: {e}")
            continue

    if not all_data:
        return pd.DataFrame()

    return pd.concat(all_data, ignore_index=True)
