import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Enhanced Mosque Design",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS for the enhanced mosque design
st.markdown("""
<style>
    /* Background setup */
    .main {
        background-color: #0a0e1a;
    }
    
    /* Container for the mosque */
    .mosque-container {
        width: 100%;
        max-width: 800px;
        height: 400px;
        margin: 50px auto;
        position: relative;
    }
    
    /* Mosque dome/roof with improved curve and gradient */
    .mosque-dome {
        width: 70%;
        height: 180px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        border-radius: 100% 100% 0 0 / 180% 180% 0 0;
        margin: 0 auto;
        position: relative;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Mosque base/body with enhanced styling */
    .mosque-body {
        width: 70%;
        height: 140px;
        background: linear-gradient(to bottom, #efc22c, #d4af37);
        margin: 0 auto;
        position: relative;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Main door (center) - taller than other windows */
    .main-door {
        width: 40px;
        height: 80px;
        background-color: #0a0e1a;
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 20px 20px 0 0;
    }
    
    /* Windows styling */
    .mosque-window {
        width: 30px;
        height: 60px;
        background-color: #0a0e1a;
        position: absolute;
        bottom: 20px;
        border-radius: 15px 15px 0 0;
    }
    
    /* Position each window */
    .window-1 {
        left: 20%;
    }
    .window-2 {
        left: 35%;
    }
    .window-3 {
        right: 35%;
    }
    .window-4 {
        right: 20%;
    }
    
    /* Minaret columns with enhanced design */
    .minaret {
        width: 20px;
        height: 260px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        position: absolute;
        bottom: 0;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Position minarets */
    .minaret-left {
        left: 5%;
    }
    .minaret-right {
        right: 5%;
    }
    
    /* Minaret tops */
    .minaret-top {
        width: 30px;
        height: 30px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        border-radius: 50%;
        position: absolute;
        top: -15px;
        left: -5px;
        box-shadow: 0 0 20px rgba(230, 180, 34, 0.3);
    }
    
    /* Subtle decorative elements */
    .decoration {
        width: 100%;
        height: 10px;
        position: absolute;
        bottom: 0;
        left: 0;
        background: linear-gradient(to right, rgba(230, 180, 34, 0), rgba(230, 180, 34, 0.3), rgba(230, 180, 34, 0));
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Enhanced mosque HTML structure
st.markdown("""
<div class="mosque-container">
    <div class="mosque-dome"></div>
    <div class="mosque-body">
        <div class="main-door"></div>
        <div class="mosque-window window-1"></div>
        <div class="mosque-window window-2"></div>
        <div class="mosque-window window-3"></div>
        <div class="mosque-window window-4"></div>
        <div class="decoration"></div>
    </div>
    <div class="minaret minaret-left">
        <div class="minaret-top"></div>
    </div>
    <div class="minaret minaret-right">
        <div class="minaret-top"></div>
    </div>
</div>
""", unsafe_allow_html=True)
