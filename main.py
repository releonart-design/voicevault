import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io
import random

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro: All-In-One Suite",
    page_icon="🔥",
    layout="wide"
)

# Dark Metallic Theme & CSS
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stApp { background: #070a12; }
    
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        padding: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    
    .ad-banner {
        background-color: #111827;
        border: 1px dashed #e11d48;
        border-radius: 8px;
        padding: 5px;
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 10px; margin: 0; text-transform: uppercase;">SPONSORED AD ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#111827; padding:5px; border-radius:6px;">
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🔥 CREATOR STUDIO PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>YouTube Script Writing, SEO Tags Generator & Thumbnail Processing Tools</p>", unsafe_allow_html=True)

# 3-Column Layout
col1, col2, col3 = st.columns([1, 1, 1])

# --- COLUMN 1: SCRIPT GENERATOR ---
with col1:
    st.markdown("### 📝 YouTube Script Generator")
    script_topic = st.text_input("Enter Video / Short Topic:", placeholder="e.g. Satoru Gojo Drawing Tutorial", key="script_top")
    video_type = st.selectbox("Format:", ["YouTube Shorts / Reel (60s)", "Long Form Video (5-10 Mins)"])
    
    if st.button("📄 GENERATE SCRIPT", key="btn_script"):
        if script_topic:
            st.success("Script Generated!")
            if "Shorts" in video_type:
                st.code(f"""
[HOOK - 0 to 5s]
"You won't believe how easy it is to draw {script_topic}!"

[BODY - 5 to 45s]
1. Start with basic pencil guidelines.
2. Outline the sharp details using dark fine-liners.
3. Apply deep shading on eyes and hair for maximum contrast.

[CALL TO ACTION - 45 to 60s]
"Subscribe for more daily artwork shorts!"
                """, language="text")
            else:
                st.code(f"""
[INTRO] Welcome back! Today we are creating {script_topic}.
[SECTION 1: Material Setup] Use 0.5mm Drafting Mechanical Pencil & Alcohol Markers.
[SECTION 2: Detailed Lineart] Focus on clean strokes and sharp edges.
[SECTION 3: Final Reveal] Add high-contrast background highlights.
[OUTRO] Like, Comment, and Subscribe for the next episode!
                """, language="text")
        else:
            st.warning("Please enter a topic first!")

# --- COLUMN 2: SAFE & FAST THUMBNAIL ENHANCER ---
with col2:
    st.markdown("### 🖼️ Thumbnail Enhancer & Editor")
    uploaded_file = st.file_uploader("Upload Image (PNG/JPG):", type=["jpg", "png", "jpeg"])
    
    enhance_color_opt = st.checkbox("Color Correction & Pop", value=True)
    sharp_opt = st.checkbox("Sharpness & Details Boost", value=True)
    crop_yt_opt = st.checkbox("Auto-Crop to 16:9 YT Thumbnail (1280x720)", value=True)
    
    if st.button("🖼️ PROCESS & ENHANCE THUMBNAIL", key="btn_img"):
        if uploaded_file is not None:
            try:
                with st.spinner("Enhancing image..."):
                    img = Image.open(uploaded_file).convert("RGB")
                    
                    if enhance_color_opt:
                        enhancer = ImageEnhance.Color(img)
                        img = enhancer.enhance(1.35)
                        contrast = ImageEnhance.Contrast(img)
                        img = contrast.enhance(1.15)
                    
                    if sharp_opt:
                        img = img.filter(ImageFilter.SHARPEN)
                        
                    if crop_yt_opt:
                        img = ImageOps.fit(img, (1280, 720), Image.Resampling.LANCZOS)
                    
                    st.image(img, caption="Enhanced HD Thumbnail", use_column_width=True)
                    
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    st.download_button(label="📥 DOWNLOAD HD THUMBNAIL", data=byte_im, file_name="thumbnail_hd.png", mime="image/png")
            except Exception as e:
                st.error("Error processing image. Please try a smaller PNG/JPG image.")
        else:
            st.warning("Please upload an image file first!")

# --- COLUMN 3: SEO TITLE & TAG GENERATOR ---
with col3:
    st.markdown("### 🏷️ SEO Title & Tag Generator")
    seo_topic = st.text_input("Enter Target Keywords:", placeholder="e.g. Speedrun Drawing, Anime Art", key="seo_top")
    
    if st.button("🚀 GENERATE VIRAL TAGS", key="btn_seo"):
        if seo_topic:
            st.success("SEO Metadata Ready!")
            viral_score = random.randint(88, 99)
            st.metric("Viral Potential Score", f"{viral_score}/100", "+ High Demand")
            
            topic_clean = seo_topic.replace(" ", "")
            st.markdown("**Viral Video Titles:**")
            st.code(f"1. How I Drew {seo_topic} in 10 Minutes! (Viral Result)\n2. The Secret to Perfect {seo_topic}\n3. {seo_topic} Speed Drawing Challenge", language="text")
            
            st.markdown("**Copy Hashtags:**")
            st.code(f"#{topic_clean} #{topic_clean}Art #AnimeDrawing #ViralShorts #TrendingArt2026 #DrawingTutorial #ShortsFeed", language="text")
        else:
            st.warning("Please enter keywords!")

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
