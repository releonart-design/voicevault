import streamlit as st
import streamlit.components.v1 as components
import random
import requests

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | 2026 Global AI Suite",
    page_icon="👑",
    layout="centered"
)

# 2026 Ultra-Modern Neon Glassmorphism & High-Moving Emoji Animations CSS
st.markdown("""
<style>
    @keyframes auroraBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes borderGlow {
        0% { border-color: rgba(99, 102, 241, 0.4); box-shadow: 0 0 15px rgba(99, 102, 241, 0.2); }
        50% { border-color: rgba(236, 72, 153, 0.85); box-shadow: 0 0 35px rgba(236, 72, 153, 0.6); }
        100% { border-color: rgba(99, 102, 241, 0.4); box-shadow: 0 0 15px rgba(99, 102, 241, 0.2); }
    }

    @keyframes floatEmoji {
        0% { transform: translateY(0px) rotate(0deg) scale(1); }
        50% { transform: translateY(-10px) rotate(8deg) scale(1.12); }
        100% { transform: translateY(0px) rotate(0deg) scale(1); }
    }

    @keyframes bounceEmoji {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-14px) scale(1.18); }
    }

    @keyframes pulseGlow {
        0% { transform: scale(1); filter: drop-shadow(0 0 2px rgba(236,72,153,0.5)); }
        50% { transform: scale(1.15); filter: drop-shadow(0 0 15px rgba(236,72,153,0.95)); }
        100% { transform: scale(1); filter: drop-shadow(0 0 2px rgba(236,72,153,0.5)); }
    }

    .emoji-float { display: inline-block; animation: floatEmoji 2.5s ease-in-out infinite; }
    .emoji-bounce { display: inline-block; animation: bounceEmoji 1.4s ease-in-out infinite; }
    .emoji-pulse { display: inline-block; animation: pulseGlow 1.8s ease-in-out infinite; }
    
    .main { background-color: #030712; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    .stApp {
        background: linear-gradient(-45deg, #030712, #1e1b4b, #311042, #0f172a, #030712);
        background-size: 400% 400%;
        animation: auroraBG 15s ease infinite;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    @keyframes popAndDrop {
        0% { opacity: 0; transform: translateY(-30px) scale(0.95); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .glass-card {
        background: rgba(17, 24, 39, 0.75);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 22px;
        padding: 30px;
        box-shadow: 0 15px 45px 0 rgba(0, 0, 0, 0.6);
        margin-bottom: 26px;
        animation: popAndDrop 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards, borderGlow 6s infinite;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        padding: 14px;
        border: none;
        box-shadow: 0 4px 25px rgba(236, 72, 153, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: pulseGlow 3s infinite ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #db2777 100%);
        box-shadow: 0 6px 30px rgba(236, 72, 153, 0.75);
        transform: translateY(-3px) scale(1.01);
    }
    
    .ad-banner {
        background-color: rgba(17, 24, 39, 0.6);
        border: 1px dashed rgba(225, 29, 72, 0.4);
        border-radius: 14px;
        padding: 8px;
        text-align: center;
        margin: 14px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(17, 24, 39, 0.85);
        padding: 8px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        color: #9ca3af;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff;
        background: rgba(236, 72, 153, 0.2);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        box-shadow: 0 4px 20px rgba(236, 72, 153, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners Function
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 9px; margin: 0; letter-spacing: 1.5px; text-transform: uppercase;"><span class="emoji-bounce">💎</span> SPONSORED AD ({position}) <span class="emoji-bounce">💎</span></p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#0b0f19; padding:6px; border-radius:10px;">
        <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
        <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
    </div>
    """, height=100)

# Social Bar Integration
components.html("""
<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>
""", height=0)

# TOP BANNER AD
render_banner_ad("Top Header")

# Animated Top Badge with Moving Emojis
st.markdown("""
<div style="text-align: center; padding: 10px 0 15px 0;">
    <span style="background: rgba(236, 72, 153, 0.15); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.4); padding: 6px 18px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; display: inline-block; box-shadow: 0 0 20px rgba(236, 72, 153, 0.3);">
        <span class="emoji-bounce">👑</span> 2026 GLOBAL VIRAL CREATOR SUITE <span class="emoji-float">🚀</span> <span class="emoji-pulse">🔥</span>
    </span>
</div>
""", unsafe_allow_html=True)

# Perfectly Centered Responsive Anime Elemental Box with Canvas Animation
def render_anime_elemental_box():
    components.html("""
    <div id="wrapperBox" style="width:100%; border-radius:18px; overflow:hidden; position:relative; background:#070a13; border:1px solid rgba(255,255,255,0.15); box-shadow:0 10px 35px rgba(0,0,0,0.7); margin-bottom: 24px;">
        <canvas id="animeCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%; display:block;"></canvas>
        <div style="position:relative; z-index:2; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; background:rgba(3,7
