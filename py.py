import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Extremely minimal CSS to match the image
st.markdown("""
<style>
    body {
        font-family: sans-serif;
    }
    
    .main {
        background-color: #0f1116;
    }
    
    h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    
    p {
        color: white;
        text-align: center;
    }
    
    .countdown-box {
        border: 2px solid #ffc94b;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        background-color: #0f1116;
    }
    
    .countdown-value {
        color: #ffc94b;
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
    }
    
    .countdown-label {
        color: white;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button styling */
    .stButton>button {
        background-color: #ffc94b !important;
        color: #0f1116 !important;
        font-weight: bold !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Simple spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# Title exactly as in image
st.markdown("<h1>Eid Mubarak</h1>", unsafe_allow_html=True)
st.markdown("<p>Het gezegende feest vieren met vreugde en dankbaarheid</p>", unsafe_allow_html=True)

# Lanterns (exact match to image)
st.markdown("""
<div style="display: flex; justify-content: space-around; margin: 2rem 0;">
    <svg width="50" height="80" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="20" width="10" height="2" fill="#ffc94b"/>
        <ellipse cx="25" cy="50" rx="15" ry="25" fill="#ffc94b"/>
    </svg>
    
    <svg width="50" height="80" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="20" width="10" height="2" fill="#ffc94b"/>
        <ellipse cx="25" cy="50" rx="15" ry="25" fill="#ffc94b"/>
    </svg>
    
    <svg width="50" height="80" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="20" width="10" height="2" fill="#ffc94b"/>
        <ellipse cx="25" cy="50" rx="15" ry="25" fill="#ffc94b"/>
    </svg>
    
    <svg width="50" height="80" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="20" width="10" height="2" fill="#ffc94b"/>
        <ellipse cx="25" cy="50" rx="15" ry="25" fill="#ffc94b"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Mosque illustration (exact match to image)
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
        <!-- Minaret - left -->
        <rect x="30" y="40" width="10" height="60" fill="#ffc94b"/>
        <circle cx="35" cy="35" r="5" fill="#ffc94b"/>
        
        <!-- Main structure -->
        <rect x="60" y="50" width="180" height="50" fill="#ffc94b"/>
        
        <!-- Dome/roof -->
        <path d="M60 50 C100 20, 200 20, 240 50" fill="#ffc94b"/>
        
        <!-- Minaret - right -->
        <rect x="260" y="40" width="10" height="60" fill="#ffc94b"/>
        <circle cx="265" cy="35" r="5" fill="#ffc94b"/>
        
        <!-- Door -->
        <rect x="135" y="60" width="30" height="40" fill="#0f1116"/>
        
        <!-- Windows -->
        <rect x="80" y="65" width="15" height="25" fill="#0f1116"/>
        <rect x="110" y="65" width="15" height="25" fill="#0f1116"/>
        <rect x="175" y="65" width="15" height="25" fill="#0f1116"/>
        <rect x="205" y="65" width="15" height="25" fill="#0f1116"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Countdown Section
st.markdown("<h3 style='text-align: center; color: white;'>Resterende Tijd Tot Eid</h3>", unsafe_allow_html=True)
st.markdown("<p>Zondag 30 maart 2025</p>", unsafe_allow_html=True)

# Set countdown end date
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
    <div class="countdown-box">
        <h3 class="countdown-value">{days:02d}</h3>
        <p class="countdown-label">Dagen</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{hours:02d}</h3>
        <p class="countdown-label">Uren</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{minutes:02d}</h3>
        <p class="countdown-label">Minuten</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{seconds:02d}</h3>
        <p class="countdown-label">Seconden</p>
    </div>
    """, unsafe_allow_html=True)

# Refresh button for updating the countdown
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.rerun()
