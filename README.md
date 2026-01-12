# 🎥 Video Captioning App

This Streamlit app uses an AI model to **automatically generate captions** for videos!  
Just upload a video file, and boom — it gives you a short description of what's happening inside.

> Built using Python, Streamlit, and BLIP (Bootstrapped Language Image Pretraining)

---

## 🚀 Features

- Upload `.mp4`, `.avi`, or `.mov` video files
- Automatically extracts frames using MoviePy
- Generates captions using a pre-trained Vision-Language Model (BLIP)
- Clean UI with background image and styled elements
- Hosted on Streamlit Cloud

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web framework
- [PyTorch](https://pytorch.org/) – Deep learning backend
- [Hugging Face Transformers](https://huggingface.co/) – Pretrained BLIP model
- [MoviePy](https://zulko.github.io/moviepy/) – Frame extraction from video

---

## 🧠 How It Works

1. User uploads a video
2. The app extracts 1 or more keyframes using MoviePy
3. BLIP processes each frame and generates a caption
4. Captions are combined and shown as a single description

---

## 📸 Example Output

A woman applies makeup in front of a mirror.

---

## 🧪 Run Locally

```bash
git clone https://github.com/your-username/video-captioning-app.git
cd video-captioning-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 💻 Live Demo

👉 https://video-captioning-app-al9pqv3obwxspwvh3uk5yu.streamlit.app/

---

## 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

---
