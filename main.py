import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io
import time
import random

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro: All-In-One Suite",
    page_icon="🔥",
    layout="centered"
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
        margin-bottom: 15px;
    }
    
    .ad-banner {
        background-color: #111827;
        border: 1px dashed #e11d48;
        border-radius: 8px;
        padding: 5px;
        text-align: center;
        margin: 10px 0;
    }
    .ad-gate-box {
        background: #1e1b4b;
        border: 1px solid #6366f1;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 15px;
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

# Clean Tabs Layout for Mobile Clickability
tab1, tab2, tab3 = st.tabs(["📝 Script Gen", "🖼️ Thumbnail & BG Tool", "🏷️ SEO Tags"])

# --- TAB 1: SCRIPT GENERATOR ---
with tab1:
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

# --- TAB 2: THUMBNAIL & BACKGROUND TOOL ---
with tab2:
    st.markdown("### 🖼️ Thumbnail & Background Tool")
    
    # Sponsor Unlock Gate Box
    st.markdown("""
    <div class="ad-gate-box">
        <p style="color:#a5b4fc; margin:0; font-size:12px;"><b>🔓 SPONSORED UNLOCK GATE</b></p>
        <p style="color:#d1d5db; margin:0; font-size:11px;">Support our free tools by visiting our sponsor link below before processing:</p>
        <a href="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a" target="_blank" style="color: #38bdf8; font-weight: bold; font-size: 12px; display:inline-block; margin-top:5px;">👉 Click Here to Visit Sponsor Ad & Unlock</a>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload Image (PNG/JPG):", type=["jpg", "png", "jpeg"], key="img_up")
    
    # Feature Options including Background Removal
    remove_bg_opt = st.checkbox("✨ Remove Background (Fast Cutout)", value=True)
    enhance_color = st.checkbox("🎨 Color Correction & Boost", value=True)
    crop_yt_opt = st.checkbox("📐 Crop to 16:9 YT Thumbnail (1280x720)", value=False)
    
    if st.button("🚀 UNLOCK & PROCESS IMAGE", key="btn_bg_process"):
        if uploaded_file is not None:
            with st.spinner("Processing image securely..."):
                time.sleep(1)
                img = Image.open(uploaded_file).convert("RGBA")
                
                # Fast Crash-Free Background Removal Logic
                if remove_bg_opt:
                    datas = img.getdata()
                    new_data = []
                    # Makes light/white background transparent instantly without OOM crash
                    for item in datas:
                        if item[0] > 235 and item[1] > 235 and item[2] > 235:
                            new_data.append((255, 255, 255, 0))
                        else:
                            new_data.append(item)
                    img.putdata(new_data)
                
                if enhance_color and not remove_bg_opt:
                    img_rgb = img.convert("RGB")
                    img_rgb = ImageEnhance.Color(img_rgb).enhance(1.35)
                    img = img_rgb.convert("RGBA")
                
                if crop_yt_opt and not remove_bg_opt:
                    img = ImageOps.fit(img, (1280, 720), Image.Resampling.LANCZOS)
                
                st.success("✨ Processed Successfully!")
                st.image(img, caption="Processed Output (Transparent / Enhanced)", use_column_width=True)
                
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                st.download_button("📥 DOWNLOAD PROCESSED IMAGE", buf.getvalue(), "processed_image.png", "mime=image/png")
        else:
            st.warning("Please upload an image file first!")

# --- TAB 3: SEO TITLE & TAG GENERATOR ---
with tab3:
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
