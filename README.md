# 🎬 ExQUIZ ME

**ExQUIZ ME** is a Streamlit-based web application that allows users to upload video lectures and automatically generates high-quality multiple-choice questions (MCQs) based on the lecture content. This tool helps learners test their understanding without reading or watching the material multiple times.

---

## ✨ Features

- 📹 Upload videos in MP4 or MOV format
- 🔊 Extracts and transcribes audio using **AssemblyAI**
- 🧠 Generates 5 high-quality, well-structured MCQs using **Google Gemini (Gemini 2.0 Flash)**
- ✅ Highlights key concepts with varied question difficulty (Easy to Hard)
- 📄 Option to view full transcript
- 💾 Download the generated quiz as a `.txt` file
- 🌐 Clean, interactive UI built with **Streamlit**

---

## 🚀 Technologies Used

- **Python 3.8+**
- **Streamlit** for the web interface
- **AssemblyAI API** for speech-to-text transcription
- **Google Gemini API** for AI-driven question generation
- **dotenv** for secure environment variable management

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   
  	 git clone https://github.com/chiragtikekar/ExQUIZ ME.git
  	 cd ExQUIZ ME

2.**Install Dependencies**
   
  	 pip install -r requirements.txt

3.**Set Up API Keys**

	Create a .env file in the project root with your API keys:

	ASSEMBLYAI_KEY=your_assemblyai_api_key
	GEMINI_API_KEY=your_google_gemini_api_key

4.**Run the App**
 
	streamlit run app.py
