import streamlit as st
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Islamic styling based on the image
def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
        
        :root {
            --dark-blue: #0a1931;
            --gold: #d4af37;
            --light-gold: #f0d174;
            --mosque: #ffc94b;
            --white: #ffffff;
            --light-blue: #4a6e8a;
        }
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        
        .main {
            background-color: var(--dark-blue);
            background-image: 
                radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
            background-size: 30px 30px;
        }
        
        .main .block-container {
            max-width: 1140px;
            padding: 2rem;
            margin: 0 auto;
            position: relative;
        }
        
        /* Reset some Streamlit defaults */
        .css-18e3th9 {
            padding-top: 0;
            padding-bottom: 0;
        }
        
        .css-1d391kg {
            padding-left: 0;
            padding-right: 0;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Star background styling */
        .star {
            position: absolute;
            background-color: var(--white);
            border-radius: 50%;
            z-index: 0;
        }
        
        @keyframes twinkle {
            0% { opacity: 0.2; }
            50% { opacity: 1; }
            100% { opacity: 0.2; }
        }
        
        /* Eid title styling */
        .eid-title {
            font-family: 'Great Vibes', cursive;
            font-size: 5rem;
            color: var(--gold);
            text-align: center;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
        }
        
        .eid-subtitle {
            font-size: 1.5rem;
            color: var(--white);
            text-align: center;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        /* Mosque styling */
        .mosque-container {
            text-align: center;
            margin: 2rem 0 3rem 0;
            position: relative;
        }
        
        /* Moon styling */
        .moon {
            position: absolute;
            top: 50px;
            right: 20%;
            width: 60px;
            height: 60px;
            background-color: var(--gold);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--gold);
            z-index: 1;
        }
        
        .moon::before {
            content: '';
            position: absolute;
            top: -5px;
            right: -5px;
            width: 60px;
            height: 60px;
            background-color: var(--dark-blue);
            border-radius: 50%;
            transform: translate(10px, -10px);
        }
        
        /* Lantern styling */
        .lanterns {
            display: flex;
            justify-content: space-around;
            margin-bottom: 2rem;
        }
        
        .lantern {
            width: 40px;
            height: 60px;
            background-color: var(--gold);
            border-radius: 20px;
            position: relative;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
            animation: swing 3s infinite ease-in-out;
        }
        
        .lantern::before {
            content: '';
            position: absolute;
            top: -10px;
            left: 15px;
            width: 10px;
            height: 10px;
            background-color: var(--gold);
            border-radius: 50%;
        }
        
        .lantern::after {
            content: '';
            position: absolute;
            top: -20px;
            left: 17px;
            width: 6px;
            height: 20px;
            background-color: var(--gold);
        }
        
        @keyframes swing {
            0% { transform: rotate(3deg); }
            50% { transform: rotate(-3deg); }
            100% { transform: rotate(3deg); }
        }
        
        .lantern:nth-child(1) {
            animation-delay: 0s;
            height: 50px;
        }
        
        .lantern:nth-child(2) {
            animation-delay: 0.5s;
            height: 70px;
        }
        
        .lantern:nth-child(3) {
            animation-delay: 1s;
            height: 55px;
        }
        
        .lantern:nth-child(4) {
            animation-delay: 1.5s;
            height: 65px;
        }
        
        /* Countdown styling */
        .countdown-section {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .countdown-section h2 {
            color: var(--gold);
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 1.8rem;
        }
        
        .countdown-section p {
            color: var(--white);
            margin-bottom: 1.5rem;
            opacity: 0.8;
        }
        
        .countdown-item {
            background: rgba(10, 25, 49, 0.6);
            border: 2px solid var(--gold);
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 1.5rem 1rem;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
            transition: transform 0.3s ease;
        }
        
        .countdown-item:hover {
            transform: translateY(-5px);
        }
        
        .countdown-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }
        
        .countdown-label {
            font-size: 0.9rem;
            color: var(--white);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Eid message styling */
        .eid-message {
            background: rgba(10, 25, 49, 0.4);
            border: 1px solid var(--gold);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2.5rem;
            text-align: center;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.1);
        }
        
        .eid-message h2 {
            color: var(--gold);
            font-weight: 600;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        
        .eid-message p {
            color: var(--white);
            line-height: 1.8;
            opacity: 0.9;
        }
        
        /* Islamic decoration styling */
        .islamic-decoration {
            text-align: center;
            margin: 1.5rem 0;
        }
        
        .bismillah {
            font-family: 'Amiri', serif;
            font-size: 2.5rem;
            color: var(--gold);
            opacity: 0.9;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            padding: 2rem;
            color: var(--white);
            opacity: 0.7;
        }
        
        .footer p {
            font-size: 0.9rem;
        }
        
        .footer .heart {
            color: #e74c3c;
        }
        
        /* Refresh button styling */
        .stButton>button {
            background-color: var(--gold) !important;
            color: var(--dark-blue) !important;
            font-weight: bold !important;
            border: none !important;
            padding: 0.5rem 1.5rem !important;
            border-radius: 30px !important;
            box-shadow: 0 0 10px rgba(212, 175, 55, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.5) !important;
        }
        
        /* Generated stars */
        .star:nth-child(1) { top: 10%; left: 15%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 0s; }
        .star:nth-child(2) { top: 20%; left: 25%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 0.5s; }
        .star:nth-child(3) { top: 15%; left: 60%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 1s; }
        .star:nth-child(4) { top: 30%; left: 80%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 1.5s; }
        .star:nth-child(5) { top: 40%; left: 10%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 2s; }
        .star:nth-child(6) { top: 50%; left: 30%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 2.5s; }
        .star:nth-child(7) { top: 60%; left: 65%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 3s; }
        .star:nth-child(8) { top: 70%; left: 75%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 3.5s; }
        .star:nth-child(9) { top: 80%; left: 20%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 4s; }
        .star:nth-child(10) { top: 85%; left: 90%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 4.5s; }
        .star:nth-child(11) { top: 5%; left: 50%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 5s; }
        .star:nth-child(12) { top: 25%; left: 40%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 5.5s; }
        .star:nth-child(13) { top: 45%; left: 85%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 6s; }
        .star:nth-child(14) { top: 65%; left: 50%; width: 1px; height: 1px; animation: twinkle 4s infinite; animation-delay: 6.5s; }
        .star:nth-child(15) { top: 75%; left: 5%; width: 2px; height: 2px; animation: twinkle 4s infinite; animation-delay: 7s; }
    </style>
    """, unsafe_allow_html=True)

# Apply custom CSS
apply_custom_css()

# Star background and decorative elements
st.markdown("""
<div style="position: relative; z-index: 0;">
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
</div>

<!-- Moon -->
<div class="moon"></div>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("""
<h1 class="eid-title">Eid Mubarak</h1>
<p class="eid-subtitle">Het gezegende feest vieren met vreugde en dankbaarheid</p>
""", unsafe_allow_html=True)

# Lanterns (decorative element)
st.markdown("""
<div class="lanterns">
    <div class="lantern"></div>
    <div class="lantern"></div>
    <div class="lantern"></div>
    <div class="lantern"></div>
</div>
""", unsafe_allow_html=True)

# Mosque illustration
st.markdown("""
<div class="mosque-container">
    <svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
        <!-- Main dome -->
        <ellipse cx="200" cy="60" rx="60" ry="30" fill="#ffc94b"/>
        <!-- Mosque body -->
        <rect x="80" y="60" width="240" height="100" fill="#ffc94b"/>
        <!-- Main door -->
        <path d="M180 160 L180 100 Q200 80 220 100 L220 160" fill="#0a1931"/>
        <!-- Left minaret -->
        <rect x="50" y="60" width="15" height="120" fill="#ffc94b"/>
        <circle cx="57.5" cy="50" r="10" fill="#ffc94b"/>
        <!-- Right minaret -->
        <rect x="335" y="60" width="15" height="120" fill="#ffc94b"/>
        <circle cx="342.5" cy="50" r="10" fill="#ffc94b"/>
        <!-- Small domes -->
        <ellipse cx="130" cy="60" rx="20" ry="10" fill="#ffc94b"/>
        <ellipse cx="270" cy="60" rx="20" ry="10" fill="#ffc94b"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Countdown Section
st.markdown("""
<div class="countdown-section">
    <h2>Resterende Tijd Tot Eid</h2>
    <p>Zondag 30 maart 2025</p>
</div>
""", unsafe_allow_html=True)

# Set countdown end date (Eid al-Fitr: March 30, 2025)
end_date = datetime(2025, 3, 30)

# Get countdown values
def get_countdown():
    now = datetime.now()
    delta = end_date - now
    
    # If countdown is finished
    if delta.total_seconds() <= 0:
        return 0, 0, 0, 0
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Create columns for countdown display
col1, col2, col3, col4 = st.columns(4)

# Display countdown
days, hours, minutes, seconds = get_countdown()

with col1:
    st.markdown(f"""
    <div class="countdown-item">
        <div class="countdown-value">{days:02d}</div>
        <div class="countdown-label">Dagen</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="countdown-item">
        <div class="countdown-value">{hours:02d}</div>
        <div class="countdown-label">Uren</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="countdown-item">
        <div class="countdown-value">{minutes:02d}</div>
        <div class="countdown-label">Minuten</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="countdown-item">
        <div class="countdown-value">{seconds:02d}</div>
        <div class="countdown-label">Seconden</div>
    </div>
    """, unsafe_allow_html=True)

# Add space
st.markdown("<br>", unsafe_allow_html=True)

# Eid message
st.markdown("""
<div class="eid-message">
    <h2>Eid Mubarak</h2>
    <p>Moge deze Eid vreugde, geluk, vrede en voorspoed brengen voor jou en je familie. De gezegende maand Ramadan leert ons de waarde van mededogen, geduld en dankbaarheid. Terwijl we wachten op Eid al-Fitr, laten we deze lessen onthouden en meenemen in ons leven.</p>
</div>
""", unsafe_allow_html=True)

# Islamic decoration
st.markdown("""
<div class="islamic-decoration">
    <div class="bismillah">﷽</div>
</div>
""", unsafe_allow_html=True)

# Decorative pattern
st.markdown("""
<div style="display: flex; justify-content: center; margin: 2rem 0;">
    <svg width="300" height="50" xmlns="http://www.w3.org/2000/svg">
        <line x1="10" y1="25" x2="290" y2="25" stroke="#d4af37" stroke-width="1" stroke-dasharray="5,5" />
        <circle cx="50" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="50" cy="25" r="10" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="50" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="150" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="150" cy="25" r="10" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="150" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="250" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="250" cy="25" r="10" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="250" cy="25" r="5" fill="#d4af37" />
    </svg>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Gemaakt met <span class="heart">❤</span> door Zakaria Akanni</p>
</div>
""", unsafe_allow_html=True)

# Refresh button for updating the countdown
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.experimental_rerun()