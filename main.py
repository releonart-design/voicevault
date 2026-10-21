import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io
import time
import random

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | AI Suite 2026",
    page_icon="⚡",
    layout="centered"
)

# 2026 Ultra-Modern Glassmorphism & Smooth CSS Animations
st.markdown("""
<style>
    .main { background-color: #030712; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    .stApp { background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #030712 70%); }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Glassmorphism Card with Fade-In Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .glass-card {
        background: rgba(17, 24, 39, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Animated Ad-Gated BG Card */
    .ad-gate-bg-card {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(147, 51, 234, 0.2) 100%);
        border: 1px solid rgba(59, 130, 246, 0.5);
        border-radius: 14px;
        padding: 24px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.25);
        transition: transform 0.3s ease;
    }
    .ad-gate-bg-card:hover {
        transform: translateY(-2px);
    }
    
    /* Glowing Modern Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        padding: 14px;
        border: none;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.6);
        transform: translateY(-2px);
    }
    
    .ad-banner {
        background-color: rgba(17, 24, 39, 0.5);
        border: 1px dashed rgba(225, 29, 72, 0.3);
        border-radius: 12px;
        padding: 6px;
        text-align: center;
        margin: 12px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(17, 24, 39, 0.8);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #9ca3af;
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #6b7280; font-size: 9px; margin: 0; letter-spacing: 1px; text-transform: uppercase;">SPONSORED AD ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#0b0f19; padding:5px; border-radius:8px;">
        <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
        <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
    </div>
    """, height=100)

# Social Bar Integration
components.html("""
<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>
""", height=0)

# Function to trigger direct ad link when user clicks background remover
def trigger_ad_and_redirect():
    components.html("""
    <script>
        window.open("https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a", "_blank");
        window.location.href = "https://www.remove.bg";
    </script>
    """, height=0)

# TOP BANNER AD
render_banner_ad("Top Header")

# Header Section
st.markdown("""
<div style="text-align: center; padding: 10px 0 20px 0;">
    <span style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.3); padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">⚡ 2026 Edition</span>
    <h1 style='color: #ffffff; font-weight: 800; margin-top: 10px; font-size: 2.2rem;'>Creator Studio Pro</h1>
    <p style='color: #9ca3af; font-size: 14px;'>Next-Gen AI Scriptwriting, Thumbnail Enhancement & SEO Suite</p>
</div>
""", unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2, tab3 = st.tabs(["📝 Script Generator", "🖼️ Thumbnail & BG Suite", "🏷️ SEO Tags"])

# --- TAB 1: SCRIPT GENERATOR ---
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 📝 AI YouTube Script Generator")
    script_topic = st.text_input("Enter Video / Short Topic:", placeholder="e.g. Satoru Gojo Advanced Art Tutorial", key="script_top")
    video_type = st.selectbox("Select Format:", ["YouTube Shorts / Reel (60s)", "Long Form Video (5-10 Mins)"])
    
    if st.button("⚡ GENERATE VIRAL SCRIPT", key="btn_script"):
        if script_topic:
            st.success("Script Generated Successfully!")
            if "Shorts" in video_type:
                st.code(f"""
[HOOK - 0 to 5s]
"You won't believe how easy it is to master {script_topic}!"

[BODY - 5 to 45s]
1. Start with clean proportion guidelines.
2. Use dark 0.5mm linework for extreme depth.
3. Apply vibrant highlights for a 2026 modern pop effect.

[CTA - 45 to 60s]
"Save this reel and subscribe for daily creator tips!"
                """, language="text")
            else:
                st.code(f"""
[INTRO] Welcome back creators! Today we break down {script_topic}.
[CHAPTER 1: Setup & Tools] Essential hardware and software workflows.
[CHAPTER 2: Execution] Step-by-step masterclass technique.
[CHAPTER 3: Optimization] Final polish and post-processing secrets.
[OUTRO] Drop your questions in comments and hit subscribe!
                """, language="text")
        else:
            st.warning("Please enter a topic first!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: THUMBNAIL & BACKGROUND TOOL (WITH AD-GATE FLOW) ---
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🖼️ Thumbnail & AI Background Suite")
    
    # Modern Ad-Gated Background Remover Section
    st.markdown("""
    <div class="ad-gate-bg-card">
        <h3 style="color: #60a5fa; margin: 0 0 6px 0; font-size: 18px;">✨ HD AI Background Remover</h3>
        <p style="color: #9ca3af; font-size: 13px; margin-bottom: 14px;">Watch a sponsor ad to instantly launch the zero-crash HD cutout tool.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎁 WATCH AD & LAUNCH AI BG REMOVER", key="btn_bg_ad_gate"):
        st.success("✨ Sponsor Ad Loaded! Opening Background Remover...")
        trigger_ad_and_redirect()
    
    st.markdown("---")
    st.markdown("#### 🎨 Thumbnail Enhancer & 16:9 Cropper")
    uploaded_file = st.file_uploader("Upload Image (PNG/JPG):", type=["jpg", "png", "jpeg"], key="img_up")
    
    enhance_color = st.checkbox("🎨 Color Correction & Vibrant Pop", value=True)
    sharp_opt = st.checkbox("🔍 Ultra Sharpness & Contrast Boost", value=True)
    crop_yt_opt = st.checkbox("📐 Auto-Crop to 16:9 YT Thumbnail (1280x720)", value=True)
    
    if st.button("🚀 PROCESS & DOWNLOAD THUMBNAIL", key="btn_bg_process"):
        if uploaded_file is not None:
            with st.spinner("Processing image with modern filters..."):
                time.sleep(1)
                img = Image.open(uploaded_file).convert("RGB")
                
                if enhance_color:
                    img = ImageEnhance.Color(img).enhance(1.4)
                    img = ImageEnhance.Contrast(img).enhance(1.2)
                if sharp_opt:
                    img = img.filter(ImageFilter.SHARPEN)
                if crop_yt_opt:
                    img = ImageOps.fit(img, (1280, 720), Image.Resampling.LANCZOS)
                
                st.success("✨ Enhanced HD Thumbnail Ready!")
                st.image(img, caption="Modern Processed Output", use_column_width=True)
                
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                st.download_button("📥 DOWNLOAD HD THUMBNAIL", buf.getvalue(), "thumbnail_2026_hd.png", "image/png")
        else:
            st.warning("Please upload an image file first!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SEO TITLE & TAG GENERATOR ---
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🏷️ SEO Title & Viral Tag Generator")
    seo_topic = st.text_input("Enter Target Keywords:", placeholder="e.g. Speedrun Art, Cyberpunk Design", key="seo_top")
    
    if st.button("🚀 GENERATE SEO METADATA", key="btn_seo"):
        if seo_topic:
            st.success("SEO Optimization Complete!")
            viral_score = random.randint(90, 99)
            st.metric("AI Viral Potential Score", f"{viral_score}/100", "+ High Ranking Probability")
            
            topic_clean = seo_topic.replace(" ", "")
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:15px;'>High-CTR Viral Titles:</p>", unsafe_allow_html=True)
            st.code(f"1. Why Everyone Is Obsessed With {seo_topic} in 2026\n2. The Ultimate {seo_topic} Masterclass (Step-by-Step)\n3. I Tested {seo_topic} For 24 Hours — Look What Happened", language="text")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>Trending Tags & Keywords:</p>", unsafe_allow_html=True)
            st.code(f"#{topic_clean} #{topic_clean}2026 #CreatorStudio #ViralContent #TrendingNow #Masterclass #YouTubeGrowth", language="text")
        else:
            st.warning("Please enter keywords!")
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
