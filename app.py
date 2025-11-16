
import streamlit as st
import os
from PIL import Image

# ---------------- APP TITLE ----------------
st.set_page_config(page_title="Molvi Birthday App", layout="centered")

st.markdown("<h1 style='text-align:center; color:#ff1493;'>🎉 Welcome to Molvi's Birthday App 🎉</h1>", unsafe_allow_html=True)

# ---------------- ENTER NAME ----------------
name = st.text_input("Enter your name:")

if name:
    # ---------------- COUNTDOWN ----------------
    import time
    for i in range(3, 0, -1):
        st.write(f"Starting in {i}…")
        time.sleep(1)
        st.empty()

    st.markdown(f"""
    <h1 style='text-align:center; color:#ff0066; font-size:45px;'>
    🎉 HAPPY 18th BIRTHDAY DEAR MOLVI {name}! 🎉
    </h1>

    <h2 style='text-align:center; color:#9900ff;'>
    From Your Best Friend ❤️ Pasha ❤️
    </h2>
    """, unsafe_allow_html=True)

    # ---------------- BIRTHDAY MESSAGE ----------------
    st.markdown("""
    <div style='font-size:20px; text-align:center; margin-top:20px;'>
    Today is not just any birthday — it's your *18th Birthday*, the beginning of adulthood!<br><br>
    
    May Allah bless you with happiness, success, wisdom and strength.<br>
    May every moment of your life shine bright like the stars. 🌟<br><br>

    Stay humble, stay strong, stay smiling — and stay the amazing person you are! 💫<br><br>

    <b>🎂 Happy 18th Birthday! 🎂</b>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- SHOW MEMORIES BUTTON ----------------
    if st.button("📸 Press to See Your Memories"):
        st.markdown("<h2 style='text-align:center; color:blue;'>📷 Your Pictures 📷</h2>", unsafe_allow_html=True)

        # ---------- DISPLAY ALL IMAGES IN images/ ----------
        image_folder = "images"
        if os.path.exists(image_folder):
            image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

            if image_files:
                for img in image_files:
                    st.image(os.path.join(image_folder, img), use_column_width=True)
                    st.write("----")
            else:
                st.warning("No images found in /images folder.")
        else:
            st.error("Folder 'images' not found. Please upload it.")

        # ---------- DISPLAY ALL VIDEOS IN videos/ ----------
        st.markdown("<h2 style='text-align:center; color:green;'>🎥 Your Videos 🎥</h2>", unsafe_allow_html=True)

        video_folder = "videos"
        if os.path.exists(video_folder):
            video_files = [f for f in os.listdir(video_folder) if f.lower().endswith((".mp4", ".mov", ".mkv"))]

            if video_files:
                for vid in video_files:
                    st.video(os.path.join(video_folder, vid))
                    st.write("----")
            else:
                st.warning("No videos found in /videos folder.")
        else:
            st.error("Folder 'videos' not found. Please upload it.")

    # ---------------- FINAL MESSAGE ----------------
    st.markdown("""
    <h1 style='text-align:center; color:red; margin-top:40px;'>
    ❤️ MOLVI G, LOVE YOU ❤️
    </h1>
    """, unsafe_allow_html=True)
