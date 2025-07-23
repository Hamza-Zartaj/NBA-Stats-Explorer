# NBA Stats Explorer 🏀

A comprehensive NBA player statistics analysis and exploration tool built with Streamlit. This application provides interactive visualizations, player performance analytics, and AI-powered insights for NBA data.

## Features

### 📊 Core Analytics
- **Player Statistics Dashboard**: View and filter NBA player stats by year, team, and position
- **Team Analysis**: Compare performance across different teams
- **Position-based Insights**: Analyze statistics by player positions (PG, SG, SF, PF, C)
- **Data Export**: Download filtered data as CSV files

### 🤖 AI-Powered Features
- **Player Similarity Analysis**: Find players with similar playing styles using machine learning
- **Performance Prediction**: Predict future player performance based on historical data
- **Trend Analysis**: Visualize player performance trends over multiple seasons

### 📈 Advanced Visualizations
- **Scoring Efficiency Analysis**: Field goal attempts vs points scored
- **Assist-to-Turnover Ratio**: Playmaking efficiency metrics
- **Free Throw Efficiency**: FT% vs FTA analysis
- **Starters vs Bench Players**: Role-based performance comparison
- **Shooting Efficiency by Position**: FG% across different positions
- **Rebounding Analysis**: Total rebounds by position
- **Correlation Heatmaps**: Inter-statistical relationships
- **Radar Charts**: Multi-dimensional player comparisons

### 📅 Historical Data
- NBA seasons from 1980 to 2025
- Real-time data scraping from Basketball Reference
- Multi-year trend analysis capabilities

## Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn (RandomForest, KNN, StandardScaler)
- **Data Source**: Basketball Reference (web scraping)

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Running in a Virtual Environment (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hamza-Zartaj/sport-stat-explorer.git
   cd sport-stat-explorer
   ```

2. **Create a virtual environment**:
   ```bash
   # On Windows
   python -m venv venv
   
   # On macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   streamlit run index.py
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://localhost:8501`

### Deactivating the Virtual Environment
When you're done using the application, deactivate the virtual environment:
```bash
deactivate
```

## Usage

1. **Select Analysis Parameters**:
   - Choose a year (1980-2025)
   - Select teams to analyze
   - Filter by player positions

2. **Explore Basic Stats**:
   - View player statistics in the main dashboard
   - Download filtered data as CSV

3. **Use AI Features**:
   - Find similar players using machine learning algorithms
   - Predict future player performance
   - Analyze multi-year trends

4. **Analyze Visualizations**:
   - Explore various statistical relationships
   - Compare players and teams across different metrics

## Data Source

This application scrapes real-time NBA statistics from [Basketball Reference](https://www.basketball-reference.com/), ensuring up-to-date and accurate player data.

## Project Team

- **Muhammad Hamza** - Registration: F1F22UBSCS064
- **Muhammad Abdullah** - Registration: F1F22UBSCS082  
- **Syed Qasim Raza** - Registration: F1F22UBSCS092

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Troubleshooting

- **Data Loading Issues**: Ensure you have a stable internet connection for web scraping
- **Package Conflicts**: Use a virtual environment to avoid dependency issues
- **Performance Issues**: Large datasets may take time to load; consider filtering data for better performance

---

*Built with ❤️ for NBA analytics enthusiasts*

