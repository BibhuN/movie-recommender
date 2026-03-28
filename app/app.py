import sys
import os
import streamlit as st

# PATH SETUP
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.content_based import ContentBasedRecommender

# PAGE CONFIG
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide", initial_sidebar_state="collapsed")

# PREMIUM NETFLIX-STYLE CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {font-family: 'Inter', sans-serif;}

#MainMenu, footer, header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f2e 100%);
    color: #fff;
}

/* HEADER */
.header {
    text-align: center;
    padding: 40px 0 20px 0;
    background: linear-gradient(180deg, rgba(0,0,0,0.4) 0%, transparent 100%);
}

.logo {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

.tagline {
    color: #94a3b8;
    font-size: 1rem;
    font-weight: 300;
}

/* SEARCH BAR */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: white !important;
    padding: 14px 20px !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
}

/* SLIDER */
.stSlider > div > div > div {
    background: #667eea !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
}

/* MOVIE CARD */
.movie-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px;
    margin: 12px 0;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}

.movie-card::before {
    content: '';
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.movie-card:hover::before {
    opacity: 1;
}

.movie-card:hover {
    transform: translateY(-5px) scale(1.02);
    border-color: rgba(102, 126, 234, 0.3);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
}

.movie-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 8px;
    color: #fff;
}

.movie-genres {
    color: #94a3b8;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.match-badge {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.95rem;
    font-weight: 600;
    display: inline-block;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.top-row {
    display: flex;
    align-items: center;
    gap: 12px;
}

.rank-badge {
    background: transparent;
    color: #fbbf24;
    font-weight: 600;
    font-size: 1rem;
    border: 2px solid #fbbf24;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
}

/* SECTION TITLE */
.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 40px 0 25px 0;
    text-align: center;
    background: linear-gradient(135deg, #fff 0%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 40px 0 20px 0;
    color: #64748b;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 60px;
}

/* LOADING SPINNER */
.stSpinner > div {
    border-color: #667eea transparent transparent transparent !important;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #0a0e1a;
}

::-webkit-scrollbar-thumb {
    background: #667eea;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #764ba2;
}
</style>
""", unsafe_allow_html=True)

# LOAD MODEL
def load_model():
    model = ContentBasedRecommender()
    model.build_model()
    return model

with st.spinner("Loading recommendation engine..."):
    recommender = load_model()

# HEADER
st.markdown('<div class="header"><div class="logo">Movie Recommendation System</div><div class="tagline">Personalized Recommendations using Content-Based Filtering</div></div>', unsafe_allow_html=True)

# SEARCH SECTION
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    movie_titles = recommender.movies['clean_title'].sort_values().unique()
    
    search_query = st.text_input("", placeholder="Search for a movie...", label_visibility="collapsed")
    
    if search_query:
        filtered_movies = [m for m in movie_titles if search_query.lower() in m.lower()]
    else:
       filtered_movies = movie_titles  # ✅ show ALL movies
    
    selected_movie = st.selectbox("", filtered_movies, label_visibility="collapsed")
    
    num_recs = st.slider("Number of recommendations", 3, 10, 5, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Discover Similar Movies"):
        with st.spinner("Finding your perfect matches..."):
            try:
                recs = recommender.get_recommendations(selected_movie, n=num_recs)
                
                if recs:
                    st.markdown(f'<div class="section-title">Top Picks for You</div>', unsafe_allow_html=True)
                    
                    for i, movie in enumerate(recs, 1):
                        match_score = int(movie.get('similarity', 0) * 100)
                        
                        st.markdown(f"""
                    <div class="movie-card">
                        <div class="top-row">
                            <div class="rank-badge">{i}</div>
                            <div class="movie-title">{movie['title']}</div>
                        </div>
                        <div class="movie-genres">{movie['genres']}</div>
                        <div class="match-badge">{match_score}% Match</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(" No recommendations found. Try another movie!")
                    
            except Exception as e:
                st.error(" Something went wrong. Please try again.")

# FOOTER
st.markdown("""
<div class="footer">
    <div style="margin-bottom: 10px;">
        <span style="font-size: 1.2rem;">🎬</span>
    </div>
    <div>Powered by Machine Learning • Content-Based Filtering • TF-IDF + Cosine Similarity</div>
    <div style="margin-top: 8px; color: #475569;">Built with Python & Streamlit</div>
</div>
""", unsafe_allow_html=True)