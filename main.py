import streamlit as st
import streamlit.components.v1 as components
import os
import tempfile
from gtts import gTTS
from googletrans import Translator

# Page Configuration
st.set_page_config(
    page_title="VoiceVault - AI Voice Dubbing",
    page_icon="🎙️",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #4f46e5; color: white; padding: 10px; }
    .ad-banner { background-color: #1a1a2e; border: 1px dashed #4f46e5; border-radius: 8px; padding: 10px; text-align: center; margin: 10px 0; }
    .affiliate-card { border: 1px solid #374151; border-radius: 8px; padding: 15px; background: #1f2937; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'ad_reward_earned' not in st.session_state:
    st.session_state['ad_reward_earned'] = False
if 'generation_completed' not in st.session_state:
    st.session_state['generation_completed'] = False
if 'dubbed_audio_path' not in st.session_state:
    st.session_state['dubbed_audio_path'] = None

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

# Top Banner Ad
render_banner_ad("Top")

# App Header
st.markdown("<h1 style='text-align: center; color: white;'>🎙️ VoiceVault</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>100% Free AI Video Voice Dubbing Studio</p>", unsafe_allow_html=True)

# Language Code Mapping for Free AI
lang_codes = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Japanese": "ja",
    "English": "en"
}

# Tabs Navigation
tab1, tab2 = st.tabs(["🎬 Dubbing Studio", "🎙️ Creator Toolkit (Affiliates)"])

with tab1:
    st.markdown("### 📤 Input Media & Text")
    input_text = st.text_area("Enter Text / Script to Dub (or upload file below)", placeholder="Type or paste your script here...")
    uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])
    target_lang = st.selectbox("Select Target Language", list(lang_codes.keys()))

    st.markdown("---")

    # Rewarded Video Ad Gatekeeper (30 Seconds)
    st.markdown("### 🎬 Free Generation Gatekeeper")
    
    if not st.session_state['ad_reward_earned']:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 15px; border-radius: 10px; color: white; text-align: center; margin-bottom: 15px;">
            <p style="font-size: 14px; margin: 0;">Watch a brief 30-second sponsored ad to unlock your free AI voice dubbing credit.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📺 Watch Rewarded Ad (30s)"):
            import time
            ad_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            components.html("""
            <div style="text-align:center; padding:10px; background:#111827; border-radius:8px; border:1px solid #4f46e5;">
                <p style="color:#818cf8; font-family:sans-serif; font-size:12px; margin-bottom:5px;">📢 SPONSORED REWARDED AD</p>
                <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
                <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
            </div>
            """, height=180)

            for seconds in range(30):
                progress_bar.progress((seconds + 1) * int(100 / 30))
                ad_placeholder.markdown(f"""
                <div style="background: #1f2937; border: 1px solid #4f46e5; padding: 15px; border-radius: 10px; text-align: center; color: white; margin-top:10px;">
                    <p style="font-size: 18px; font-weight: bold; margin: 0;">⏳ {30 - seconds} seconds remaining</p>
                    <p style="font-size: 11px; color: #9ca3af; margin: 5px 0 0 0;">Do not close screen until counter ends.</p>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)
                
            ad_placeholder.empty()
            progress_bar.empty()
            
            st.session_state['ad_reward_earned'] = True
            st.success("🎉 Reward Unlocked! You can now generate your dub.")
            st.rerun()
    else:
        st.success("✅ Free Generation Credit Active!")
        if st.button("🚀 Start Free AI Voice Dubbing", type="primary"):
            if not input_text and uploaded_file is None:
                st.error("Please enter some text or upload an audio file to dub!")
            else:
                with st.spinner("Processing 100% Free AI Translation & Voice Synthesis..."):
                    try:
                        translator = Translator()
                        target_code = lang_codes[target_lang]
                        
                        text_to_dub = input_text if input_text else "Hello, welcome to VoiceVault free AI dubbing service."
                        
                        # Step 1: Translate Text
                        translated = translator.translate(text_to_dub, dest=target_code)
                        translated_text = translated.text
                        
                        # Step 2: Convert Translated Text to Free AI Speech
                        tts = gTTS(text=translated_text, lang=target_code, slow=False)
                        
                        # Save to Temp File
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                        tts.save(temp_file.name)
                        
                        st.session_state['dubbed_audio_path'] = temp_file.name
                        st.session_state['generation_completed'] = True
                        st.success("✨ Voice Dubbing Completed Successfully!")
                    except Exception as e:
                        st.error(f"Error processing AI audio: {e}")

    # Output / Download Section
    if st.session_state['generation_completed'] and st.session_state['dubbed_audio_path']:
        st.markdown("### 📥 Download Dubbed Output")
        st.audio(st.session_state['dubbed_audio_path'])
        
        # Buy Me a Coffee
        st.markdown("""
        <div style="text-align: center; margin-top: 25px; padding: 20px; background: #111827; border-radius: 12px; border: 1px solid #4f46e5;">
            <h3 style="color: white; margin-bottom: 5px;">❤️ Support Open-Source AI</h3>
            <p style="color: #9ca3af; font-size: 13px; margin-bottom: 15px;">Help us cover server bandwidth costs!</p>
            <a href="https://buymeacoffee.com" target="_blank" style="background-color: #ffdd00; color: #000; padding: 10px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; display: inline-block;">☕ Buy Me a Coffee</a>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    # Creator Toolkit Affiliate Section
    st.markdown("### 🎧 Recommended Studio Gear & Creator Toolkit")
    st.markdown("""
    <div class="affiliate-card">
        <h4 style="color: #f3f4f6; margin: 0 0 5px 0;">Shure MV7 USB Microphone</h4>
        <p style="color: #9ca3af; font-size: 12px; margin: 0 0 10px 0;">Broadcast podcast mic for crystal-clear voice input accuracy.</p>
        <a href="https://amazon.com" target="_blank" style="background: #f59e0b; color: #111; padding: 5px 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 12px;">View on Amazon &rarr;</a>
    </div>
    """, unsafe_allow_html=True)

# Bottom Banner Ad
render_banner_ad("Bottom")
