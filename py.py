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
        }
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        
        .main {
            background-color: var(--dark-blue);
        }
        
        .main .block-container {
            max-width: 1140px;
            padding: 2rem;
            margin: 0 auto;
        }
        
        /* Reset Streamlit defaults */
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
        
        /* Title styling */
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
        }
    </style>
    """, unsafe_allow_html=True)

# Apply custom CSS
apply_custom_css()

# Title and subtitle
st.markdown("""
<h1 class="eid-title">Eid Mubarak</h1>
<p class="eid-subtitle">Het gezegende feest vieren met vreugde en dankbaarheid</p>
""", unsafe_allow_html=True)

# Mosque illustration (simplified)
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
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

# Islamic decoration (simplified)
st.markdown("""
<div class="islamic-decoration">
    <div class="bismillah">﷽</div>
</div>
""", unsafe_allow_html=True)

# Decorative elements (simplified)
st.markdown("""
<div style="display: flex; justify-content: center; margin: 2rem 0;">
    <svg width="300" height="50" xmlns="http://www.w3.org/2000/svg">
        <line x1="10" y1="25" x2="290" y2="25" stroke="#d4af37" stroke-width="1" stroke-dasharray="5,5" />
        <circle cx="50" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="50" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="150" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
        <circle cx="150" cy="25" r="5" fill="#d4af37" />
        
        <circle cx="250" cy="25" r="15" fill="none" stroke="#d4af37" stroke-width="2" />
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
