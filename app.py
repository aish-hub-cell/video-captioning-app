import streamlit as st
from moviepy import VideoFileClip
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import tempfile


device = "cuda" if torch.cuda.is_available() else "cpu"  #device setup 
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device) #Loading the model

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.livelife.guide/wp-content/uploads/2018/04/Depositphotos_12283216_m-2015.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
            
    .text-block {
        background-color: rgba(0, 0, 0, 0.6);   
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-top: 20px;
    }
            
     h1 {
        font-size: 48px !important;
        text-align: center;
        color: white !important;
        text-shadow:
            0 0 5px #ff0080,
            0 0 10px #ff0080,
            0 0 20px #ff0080,
            0 0 40px #00ffff,
            0 0 60px #00ffff;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from {
            text-shadow:
                0 0 5px #ff0080,
                0 0 10px #ff0080,
                0 0 20px #ff0080,
                0 0 30px #00ffff,
                0 0 40px #00ffff;
        }
        to {
            text-shadow:
                0 0 10px #00ffff,
                0 0 20px #00ffff,
                0 0 30px #ff0080,
                0 0 40px #ff0080,
                0 0 50px #ff0080;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎥 Video Captioning</h1>", unsafe_allow_html=True)
st.markdown("<div class='text-block'><h4>Upload a video file to generate a caption.</h4></div>", unsafe_allow_html=True)
st.markdown("<div class='text-block'><p style='color:white; font-weight:bold;'>📁 Upload your file below</p></div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["mp4", "avi", "mov"])

def extract_frames(video_path, num_frames=1):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    timestamps = [duration * (i+1)/(num_frames+1) for i in range(num_frames)]
    frames = [Image.fromarray(clip.get_frame(t)) for t in timestamps]
    clip.close()
    return frames

def generate_caption(images):
    captions = []
    for image in images:
        inputs = processor(images=image, return_tensors="pt").to(device)
        with torch.no_grad():
            output = model.generate(**inputs, max_length=30)
        caption = processor.tokenizer.decode(output[0], skip_special_tokens=True)
        captions.append(caption)
    return ". ".join(list(set(captions)))

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        video_path = tmp_file.name

    col1,col2= st.columns(2)
    with col1:
       st.video(video_path)
   

    with st.spinner("Generating caption..."):
        frames = extract_frames(video_path)
        caption = generate_caption(frames)
        st.success("Caption generated!")
    with col2:
       st.markdown(f"<div class='text-block'><p style='color:white; font-size:16px;'><strong>Caption:</strong> {caption}</p></div>", unsafe_allow_html=True)

