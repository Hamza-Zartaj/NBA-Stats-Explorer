# NBA Stats Explorer 🏀

A comprehensive NBA player statistics analysis and exploration tool built with Streamlit. This application provides interactive visualizations, player performance analytics, and AI-powered insights for NBA data from 1980 to 2025.

## 🌟 Features

### 📊 Core Analytics
- **Interactive Player Statistics Dashboard**: View and filter NBA player stats by year, team, and position
- **Dynamic Team Analysis**: Compare performance metrics across different teams
- **Position-based Insights**: Analyze statistics by player positions (PG, SG, SF, PF, C)
- **CSV Data Export**: Download filtered datasets for external analysis
- **Real-time Data Loading**: Live scraping from Basketball Reference

### 🤖 AI-Powered Features
- **Player Similarity Analysis**: Find players with similar playing styles using K-Nearest Neighbors algorithm
- **Performance Prediction**: Predict future player performance using Random Forest regression
- **Multi-dimensional Comparisons**: Radar charts for comprehensive player analysis
- **Historical Trend Analysis**: Visualize player performance evolution over multiple seasons

### 📈 Advanced Visualizations
- **🎯 Scoring Efficiency Analysis**: Field goal attempts vs points scored scatter plots
- **🏀 Assist-to-Turnover Ratio**: Playmaking efficiency metrics and rankings
- **⚡ Free Throw Efficiency**: FT% vs FTA correlation analysis
- **🧑‍🤝‍🧑 Starters vs Bench Players**: Role-based performance comparison
- **🤾‍♂️ Shooting Efficiency by Position**: Position-specific field goal percentage analysis
- **⛹️‍♂️ Rebounding Analysis**: Total rebounds distribution by position
- **🔥 Statistical Correlation Heatmaps**: Inter-statistical relationships visualization
- **🏆 Awards and Performance**: Player awards correlation with statistical performance
- **⛹️‍♀️ Points per Minute**: Scoring efficiency metrics

### 📅 Historical Data Coverage
- **Extensive Coverage**: NBA seasons from 1980 to 2025
- **Real-time Updates**: Live data scraping from Basketball Reference
- **Multi-year Analysis**: Historical trend analysis capabilities
- **Data Caching**: Streamlit caching for improved performance

## 🏗️ Project Architecture

### Modular Design
The project follows a clean, modular architecture with separated concerns:

```
NBA-Stats-Explorer/
├── app.py                 # Main application entry point
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
├── components/           # UI components
│   ├── header.py         # Application header and team information
│   ├── download.py       # CSV download functionality
│   └── ai_features.py    # AI-powered features UI
├── data/                 # Data loading and processing
│   └── loader.py         # Data fetching from Basketball Reference
├── ml/                   # Machine learning models
│   ├── ai_insights.py    # Player similarity analysis
│   └── predictor.py      # Performance prediction models
└── visualization/        # Data visualization components
    └── charts.py         # Statistical charts and plots
```

### Core Components

#### 🎯 Main Application (`app.py`)
- **Streamlit Configuration**: Wide layout with custom page title
- **Sidebar Controls**: Year selection, team filtering, position filtering
- **Tabbed Interface**: Separation between basic stats and AI features
- **Data Flow Management**: Coordinates data loading and filtering

#### 📊 Data Layer (`data/loader.py`)
- **Web Scraping**: Real-time data fetching from Basketball Reference
- **Data Cleaning**: Removes invalid entries and handles missing values
- **Caching**: Streamlit cache decorators for performance optimization
- **Historical Data**: Multi-year data aggregation capabilities
- **Error Handling**: Graceful handling of network and parsing errors

#### 🤖 Machine Learning (`ml/`)

**AI Insights (`ai_insights.py`)**:
- **Feature Engineering**: 17 statistical features for similarity analysis
- **Standardization**: StandardScaler for feature normalization
- **K-Nearest Neighbors**: Euclidean distance-based player similarity
- **Similarity Scoring**: Inverse distance similarity calculation

**Performance Predictor (`predictor.py`)**:
- **Random Forest Regression**: Ensemble learning for performance prediction
- **Feature Engineering**: Lag features, averages, and trend analysis
- **Multi-stat Prediction**: Points, assists, and rebounds forecasting
- **Confidence Scoring**: Model performance metrics

#### 📈 Visualization (`visualization/charts.py`)
- **Statistical Analysis**: 9 different visualization types
- **Interactive Plots**: Matplotlib and Seaborn integration
- **Data Transformations**: Custom metrics calculation (AST/TOV ratio, etc.)
- **Warning-free Operations**: DataFrame copy operations to avoid pandas warnings

#### 🎨 UI Components (`components/`)
- **Modular Header**: Team member information and project branding
- **Download Functionality**: Base64 encoded CSV export
- **AI Features UI**: Interactive player selection and visualization

## 🛠️ Technology Stack

### Core Framework
- **Frontend**: Streamlit 1.41.1 - Modern web app framework for data science
- **Backend**: Python 3.8+ - Core programming language

### Data Processing
- **Pandas 2.2.2**: DataFrame operations and data manipulation
- **NumPy 1.26.4**: Numerical computing and array operations
- **lxml 5.2.1**: XML/HTML parsing for web scraping

### Visualization Libraries
- **Matplotlib 3.8.4**: Static plotting and chart generation
- **Seaborn 0.13.2**: Statistical data visualization
- **Plotly 5.24.1**: Interactive plots and radar charts

### Machine Learning
- **Scikit-learn 1.4.2**: ML algorithms and preprocessing
  - RandomForestRegressor: Performance prediction
  - KNearestNeighbors: Player similarity analysis
  - StandardScaler: Feature normalization

### Data Source
- **Basketball Reference**: Comprehensive NBA statistics database
- **Web Scraping**: Real-time data extraction using pandas.read_html()

## 🚀 Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection for data scraping

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hamza-Zartaj/NBA-Stats-Explorer.git
   cd NBA-Stats-Explorer
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## 📋 Usage Guide

### Basic Operations

1. **Data Selection**:
   - Select year from dropdown (1980-2025)
   - Choose teams using multi-select widget
   - Filter by player positions (PG, SG, SF, PF, C)

2. **Data Exploration**:
   - View filtered statistics in interactive table
   - Download data as CSV for external analysis
   - Explore 9 different visualization types

3. **AI Features**:
   - **Player Similarity**: Select a player to find similar players based on statistical profile
   - **Performance Prediction**: Choose a player for future performance forecasting
   - **Radar Charts**: Compare current vs predicted statistics

### Visualization Types

1. **🎯 Scoring Efficiency**: FGA vs PTS by position
2. **🏀 AST/TOV Ratio**: Top 10 playmakers ranking
3. **⚡ Free Throw Efficiency**: FT% vs FTA scatter plot
4. **🧑‍🤝‍🧑 Role Analysis**: Starters vs bench performance
5. **🤾‍♂️ Position Shooting**: FG% distribution by position
6. **⛹️‍♂️ Rebounding**: Total rebounds by position
7. **🔥 Correlation Matrix**: Statistical relationships heatmap
8. **🏆 Awards Analysis**: Performance vs recognition
9. **⛹️‍♀️ Efficiency Metrics**: Points per minute analysis

## 🔧 Technical Implementation

### Data Flow
1. **User Input**: Year, team, and position selection
2. **Data Fetching**: Real-time scraping from Basketball Reference
3. **Data Filtering**: Apply user-selected filters
4. **Visualization**: Generate statistical charts and plots
5. **AI Analysis**: ML-powered insights and predictions

### Performance Optimizations
- **Streamlit Caching**: `@st.cache_data` decorators for data loading
- **DataFrame Operations**: Efficient pandas operations with proper copying
- **Error Handling**: Graceful degradation for network issues
- **Memory Management**: Proper cleanup of matplotlib figures

### Security Features
- **Input Validation**: Safe handling of user inputs
- **Data Sanitization**: Proper cleaning of scraped data
- **Error Boundaries**: Exception handling for all critical operations

## 🎓 Educational Value

This project demonstrates:
- **Full-stack Development**: From data acquisition to user interface
- **Machine Learning Pipeline**: Feature engineering, model training, and prediction
- **Data Visualization**: Multiple chart types and interactive elements
- **Web Scraping**: Real-time data extraction and processing
- **Software Engineering**: Modular design and separation of concerns

## 👥 Project Team

- **Muhammad Hamza** - Registration: F1F22UBSCS064
  - Project Lead, Backend Development, ML Implementation
- **Muhammad Abdullah** - Registration: F1F22UBSCS082  
  - Frontend Development, UI/UX Design, Data Visualization
- **Syed Qasim Raza** - Registration: F1F22UBSCS092
  - Data Engineering, Testing, Documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling for external dependencies
- Test with multiple data scenarios

## 🐛 Troubleshooting

### Common Issues

**Data Loading Issues**:
- Ensure stable internet connection for web scraping
- Check Basketball Reference website availability
- Verify year parameter is within valid range (1980-2024)

**Package Conflicts**:
- Use virtual environment to isolate dependencies
- Update packages if compatibility issues arise
- Check Python version compatibility (3.8+)

**Performance Issues**:
- Large datasets may take time to load
- Use data filtering to improve performance
- Clear Streamlit cache if needed: `streamlit cache clear`

**Memory Issues**:
- Close matplotlib figures properly
- Limit data range for better performance
- Monitor RAM usage with large datasets

### Error Resolution
- Check terminal output for specific error messages
- Verify all dependencies are installed correctly
- Ensure proper virtual environment activation
- Check file permissions and paths

## 📈 Future Enhancements

- **Database Integration**: PostgreSQL/MongoDB for data persistence
- **Real-time Updates**: Live game statistics integration
- **Advanced ML Models**: Deep learning for more sophisticated predictions
- **Mobile Responsiveness**: Optimized mobile interface
- **User Authentication**: Personalized dashboards and preferences
- **Advanced Analytics**: Team chemistry analysis, injury prediction
- **Export Options**: PDF reports, PowerPoint presentations

## 📄 License

This project is developed for educational purposes as part of university coursework.

## 🙏 Acknowledgments

- **Basketball Reference**: For providing comprehensive NBA statistics
- **Streamlit Community**: For excellent documentation and support
- **Scikit-learn Team**: For robust machine learning libraries
- **University Faculty**: For guidance and project requirements

---

*Built with ❤️ for NBA analytics enthusiasts and data science education*

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

