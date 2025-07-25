# Youtube-Video-Summarizer
No worries, thala. Here's exactly what you can **copy-paste into your `README.md` file** — it's already in the correct format and complete:

---

````markdown
# YouTube Video Summarizer using Streamlit and Gemini AI

This is a simple web application that summarizes YouTube videos by extracting their transcripts and generating a concise, easy-to-understand summary using Google’s Gemini 2.0 Flash model. It’s a helpful tool for anyone who wants to quickly understand the content of a video without watching the whole thing.

---

## About the Project

The YouTube Video Summarizer is built with Python and Streamlit. It takes a YouTube URL as input, loads the transcript of the video, and sends it through a language model to generate a readable summary. The goal is to save time and provide value to users who prefer reading over watching or need quick insights from long videos.

---

## Key Features

- Accepts any public YouTube video URL  
- Extracts the transcript using LangChain's YouTubeLoader  
- Uses Gemini 2.0 Flash (Google Generative AI) for fast, high-quality summarization  
- Simple and clean interface with Streamlit  
- No manual transcript copy-pasting required  

---

## Technologies Used

- Python  
- Streamlit  
- LangChain  
- Google Generative AI (Gemini)  
- dotenv (for API key management)  

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-video-summarizer.git
cd youtube-video-summarizer
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your Google Generative AI API key:

```
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## How It Works

* The user inputs a YouTube video URL.
* The app fetches the video transcript using LangChain's YouTubeLoader.
* The transcript is sent to a prompt template and passed to the Gemini model.
* The model returns a summary which is then displayed on the screen.

---

## Use Cases

* Summarizing educational or technical videos
* Quickly extracting key points from long content
* Aiding research and note-taking
* Helping students and professionals consume content more efficiently

---

## Contribution

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository, raise issues, or submit pull requests.

