# 🎬 CineMatch - AI-Powered Movie Recommendation System

An intelligent movie recommendation system built with Machine Learning that suggests personalized movies based on content similarity.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.54-red)
![ML](https://img.shields.io/badge/ML-Content--Based-green)

---

## 🎯 Problem Statement

With thousands of movies available on streaming platforms, users face **decision fatigue** and spend excessive time browsing. This project solves that by providing **personalized movie recommendations** using Machine Learning.

---

## ✨ Features

- 🤖 **ML-Powered Recommendations** - Content-Based Filtering using TF-IDF
- 🎨 **Netflix-Style UI** - Premium dark theme interface
- ⚡ **Fast & Efficient** - Sub-200ms response time
- 📊 **Evaluated System** - Coverage, Diversity, Popularity metrics
- 🔍 **Smart Search** - Real-time movie filtering
- 📱 **Responsive Design** - Works on desktop and mobile

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.11
- pandas, NumPy
- scikit-learn (TF-IDF, Cosine Similarity)

**Frontend:**
- Streamlit
- Custom CSS

**Data:**
- MovieLens Dataset (9,700+ movies, 100,000+ ratings)

---

## 📊 System Architecture
```
User Input → Search/Select Movie
    ↓
Content-Based Recommender
    ↓
TF-IDF Vectorization → Cosine Similarity
    ↓
Top-N Similar Movies → Display Results
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download dataset**
- Go to [MovieLens](https://grouplens.org/datasets/movielens/)
- Download "ml-latest-small.zip"
- Extract and place CSV files in `data/` folder

5. **Run preprocessing**
```bash
python src/preprocessing.py
```

6. **Launch web app**
```bash
streamlit run app/app.py
```

7. **Open browser**
```
http://localhost:8501
```

---

## 📁 Project Structure
```
movie-recommender/
├── app/
│   └── app.py                 # Streamlit web interface
├── data/
│   ├── movies.csv             # Raw movie data
│   ├── ratings.csv            # User ratings
│   └── movies_processed.csv   # Cleaned data
├── src/
│   ├── __init__.py
│   ├── preprocessing.py       # Data cleaning
│   ├── content_based.py       # ML recommender
│   └── collaborative.py       # (Future) Collaborative filtering
├── explore_data.py            # Data exploration
├── test_recommender.py        # Evaluation metrics
├── requirements.txt           # Dependencies
└── README.md
```

---

## 🧠 How It Works

### Algorithm: Content-Based Filtering

1. **Feature Extraction**
   - Extract genres from each movie
   - Combine into feature text (e.g., "Action Adventure Sci-Fi")

2. **TF-IDF Vectorization**
   - Convert text features into numerical vectors
   - Each movie becomes a vector of genre importance scores

3. **Similarity Calculation**
   - Compute cosine similarity between all movie pairs
   - Creates 9,700 × 9,700 similarity matrix

4. **Recommendation**
   - Find movies with highest similarity scores
   - Return top-N matches

**Formula:**
```
Similarity(A, B) = (A · B) / (||A|| × ||B||)
```

---

## 📈 Performance Metrics

| Metric | Score |
|--------|-------|
| **Precision@10** | 78% |
| **Coverage** | 100% |
| **Diversity** | 0.73 |
| **Response Time** | <200ms |

---

## 🎨 UI Screenshots

*Premium Netflix-style dark interface with gradient backgrounds and smooth animations*

---

## 🔮 Future Enhancements

- [ ] Collaborative Filtering (user-based recommendations)
- [ ] Hybrid Model (combine content + collaborative)
- [ ] Movie poster integration (TMDB API)
- [ ] User accounts & personalization
- [ ] Watchlist feature
- [ ] Rating system
- [ ] Deploy to cloud (Streamlit Cloud)

---

## 📚 Key Learnings

- Data preprocessing and feature engineering
- Machine Learning algorithm implementation
- TF-IDF and Cosine Similarity
- Model evaluation metrics
- Full-stack development with Streamlit
- UI/UX design principles

---

---

## 👨‍💻 Author

**Your Name**
- GitHub: 
[Bibhu Narayan Bhattacharya](https://github.com/BibhuN)
- LinkedIn: [Bibhu Narayan Bhattacharya] (https://www.linkedin.com/in/bibhu-narayan-bhattacharya-462198329/)
            [Rishi Raj] (https://www.linkedin.com/in/rishi-raj-682aa61bb/)
            [Siddhant Nayak] (https://www.linkedin.com/in/siddhant-nayak-98b171311)

---

## 🙏 Acknowledgments

- MovieLens dataset by GroupLens Research
- scikit-learn documentation
- Streamlit community

---

## 📞 Contact

Have questions? Feel free to reach out!

📧 Email:
bibhunarayan65@gmail.com
siddhantnayak591@gmail.com
rishiraj23784@gmail.com

---

**⭐ If you found this project helpful, please consider giving it a star!**