import streamlit as st
import yt_dlp
import os
import glob

st.title("YouTube Video Downloader")

yt_link = st.text_input("Enter YouTube video link:")

if st.button("Download"):
    if not yt_link:
        st.error("Please enter a YouTube link.")
    else:
        temp_folder = "downloads"
        os.makedirs(temp_folder, exist_ok=True)
        output_template = os.path.join(temp_folder, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_template
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_link])
            # Find the most recently downloaded file
            list_of_files = glob.glob(os.path.join(temp_folder, '*'))
            latest_file = max(list_of_files, key=os.path.getctime)
            with open(latest_file, "rb") as file:
                st.success("Download completed! Click below to save the video.")
                st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=os.path.basename(latest_file),
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"Error: {e}")