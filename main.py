import streamlit as st
import streamlit.components.v1 as components
import requests
import io
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="AI YouTube Thumbnail Studio",
    page_icon="🖼️",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #ff0000; color: white; padding: 10px; }
    .ad-banner { background-color: #1a1a2e; border: 1px dashed #ff0000; border-radius: 8px; padding: 10px; text-align: center; margin: 10px 0; }
    .affiliate-card { border: 1px solid #374151; border-radius: 8px; padding: 15px; background: #1f2937; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# Fetch Token from Streamlit Secrets or Sidebar
hf_token = ""
if "HF_TOKEN" in st.secrets:
    hf_token = st.secrets["HF_TOKEN"]

# Session State Initialization
if 'ad_reward_earned' not in st.session_state:
    st.session_state['ad_reward_earned'] = False
if 'generation_completed' not in st.session_state:
    st.session_state['generation_completed'] = False
if 'generated_image' not in st.session_state:
    st.session_state['generated_image'] = None

# Live Adsterra Social Bar Integration
components.html("""
<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>
""", height=0)

# Native Banner Ad Function
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 10px; margin: 0 0 2px 0; text-transform: uppercase;">Sponsored Banner ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#1a1a2e; padding:5px; border-radius:6px;">
        <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
        <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
    </div>
    """, height=100)

# TOP BANNER AD
render_banner_ad("Top Header")

# App Header
st.markdown("<h1 style='text-align: center; color: white;'>🖼️ AI YouTube Thumbnail Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>High-CTR Ultra-HD AI Generator</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Engine Settings")
if not hf_token:
    hf_token = st.sidebar.text_input("Hugging Face API Token", type="password", placeholder="Paste hf_xxxxxxxx Token here")
else:
    st.sidebar.success("✅ HF_TOKEN Loaded from Secrets!")

# Tabs Navigation
tab1, tab2 = st.tabs(["🎨 Thumbnail Generator", "🎙️ Creator Toolkit (Affiliates)"])

with tab1:
    st.markdown("### 🎯 Thumbnail Settings")
    prompt_text = st.text_area("Describe Your Thumbnail Image Prompt", placeholder="e.g. Dynamic action manga line art style illustration...")
    
    col1, col2 = st.columns(2)
    with col1:
        thumbnail_type = st.selectbox("Thumbnail Format", ["YouTube Standard Video (16:9)", "YouTube Shorts (9:16)"])
    with col2:
        art_style = st.selectbox("Visual Style", ["Anime / Anime FanArt", "Cinematic / Realistic", "Cyberpunk / Gaming", "3D Render / Cartoon"])

    st.markdown("---")

    # Rewarded Video Ad Gatekeeper (30 Seconds)
    st.markdown("### 🎬 Free Generation Gatekeeper")
    
    if not st.session_state['ad_reward_earned']:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%); padding: 15px; border-radius: 10px; color: white; text-align: center; margin-bottom: 15px;">
            <p style="font-size: 14px; margin: 0;">Watch a brief 30-second sponsored ad to unlock your free Ultra-HD AI thumbnail credit.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📺 Watch Rewarded Ad (30s)"):
            import time
            ad_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            components.html("""
            <div style="text-align:center; padding:10px; background:#111827; border-radius:8px; border:1px solid #ef4444;">
                <p style="color:#f87171; font-family:sans-serif; font-size:12px; margin-bottom:5px;">📢 SPONSORED REWARDED AD</p>
                <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
                <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
            </div>
            """, height=180)

            for seconds in range(30):
                progress_bar.progress((seconds + 1) * int(100 / 30))
                ad_placeholder.markdown(f"""
                <div style="background: #1f2937; border: 1px solid #ef4444; padding: 15px; border-radius: 10px; text-align: center; color: white; margin-top:10px;">
                    <p style="font-size: 18px; font-weight: bold; margin: 0;">⏳ {30 - seconds} seconds remaining</p>
                    <p style="font-size: 11px; color: #9ca3af; margin: 5px 0 0 0;">Do not close screen until counter ends.</p>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)
                
            ad_placeholder.empty()
            progress_bar.empty()
            
            st.session_state['ad_reward_earned'] = True
            st.success("🎉 Reward Unlocked! You can now generate your HD thumbnail.")
            st.rerun()
    else:
        st.success("✅ Free Generation Credit Active!")
        if st.button("🚀 Generate Ultra-HD AI Thumbnail", type="primary"):
            if not prompt_text:
                st.error("Please enter a prompt for your thumbnail!")
            else:
                with st.spinner("Rendering Ultra-HD AI Thumbnail..."):
                    try:
                        width = 1280 if "Standard" in thumbnail_type else 720
                        height = 720 if "Standard" in thumbnail_type else 1280
                        
                        full_prompt = f"{prompt_text}, {art_style} style, ultra detailed high quality youtube thumbnail, 8k resolution, cinematic lighting, masterpiece"
                        encoded_prompt = requests.utils.quote(full_prompt)
                        image_loaded = False
                        
                        # Method 1: Pollinations Flux Engine (Extremely fast & reliable)
                        try:
                            url1 = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux&nologo=true"
                            resp1 = requests.get(url1, timeout=25)
                            if resp1.status_code == 200:
                                image = Image.open(io.BytesIO(resp1.content))
                                st.session_state['generated_image'] = image
                                image_loaded = True
                        except Exception:
                            pass
                        
                        # Method 2: Hugging Face API Backup
                        if not image_loaded and hf_token:
                            try:
                                API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
                                headers = {"Authorization": f"Bearer {hf_token}"}
                                resp2 = requests.post(API_URL, headers=headers, json={"inputs": full_prompt}, timeout=25)
                                if resp2.status_code == 200:
                                    image = Image.open(io.BytesIO(resp2.content))
                                    st.session_state['generated_image'] = image
                                    image_loaded = True
                            except Exception:
                                pass

                        # Method 3: Standard Pollinations Backup
                        if not image_loaded:
                            url3 = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"
                            resp3 = requests.get(url3, timeout=25)
                            if resp3.status_code == 200:
                                image = Image.open(io.BytesIO(resp3.content))
                                st.session_state['generated_image'] = image
                                image_loaded = True

                        if image_loaded:
                            st.session_state['generation_completed'] = True
                            st.success("✨ Ultra-HD Thumbnail Generated Successfully!")
                        else:
                            st.error("Servers are currently experiencing high traffic. Please click generate again.")
                    except Exception as e:
                        st.error(f"Generation error: {e}. Please try again.")

    # Output / Download Section
    if st.session_state['generation_completed'] and st.session_state['generated_image']:
        st.markdown("### 📥 Your Ultra-HD AI Thumbnail")
        st.image(st.session_state['generated_image'], use_container_width=True)
        
        buf = io.BytesIO()
        st.session_state['generated_image'].save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="💾 Download High-Res Thumbnail (PNG)",
            data=byte_im,
            file_name="youtube_thumbnail.png",
            mime="image/png"
        )
        
        st.markdown("""
        <div style="text-align: center; margin-top: 25px; padding: 20px; background: #111827; border-radius: 12px; border: 1px solid #ef4444;">
            <h3 style="color: white; margin-bottom: 5px;">❤️ Support Open-Source AI Studio</h3>
            <p style="color: #9ca3af; font-size: 13px; margin-bottom: 15px;">Help us keep this HD generator free for creators!</p>
            <a href="https://buymeacoffee.com" target="_blank" style="background-color: #ffdd00; color: #000; padding: 10px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; display: inline-block;">☕ Buy Me a Coffee</a>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 🎧 Recommended Creator Studio Gear")
    st.markdown("""
    <div class="affiliate-card">
        <h4 style="color: #f3f4f6; margin: 0 0 5px 0;">Drawing Tablet for Custom Edits</h4>
        <p style="color: #9ca3af; font-size: 12px; margin: 0 0 10px 0;">Essential graphics tablet for retouching thumbnails & adding text overlays.</p>
        <a href="https://amazon.com" target="_blank" style="background: #f59e0b; color: #111; padding: 5px 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 12px;">View on Amazon &rarr;</a>
    </div>
    """, unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
                              
