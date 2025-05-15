import os
import streamlit as st
import assemblyai as aai
import google.generativeai as genai
from dotenv import load_dotenv

# Load API keys
load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# App UI
st.title("🎬 Lecture Quiz Generator ")
uploaded_file = st.file_uploader("Upload video (MP4/MOV)", type=["mp4", "mov"])

if uploaded_file:
    st.video(uploaded_file)
    
    # Transcribe with AssemblyAI
    with st.spinner("🔍 Analyzing video..."):
        transcript = aai.Transcriber().transcribe(uploaded_file)
        if transcript.error:
            st.error(f"Transcription failed: {transcript.error}")
        else:
            text = transcript.text
            st.success("✅ Transcription complete!")
            with st.expander("View Transcript"):
                st.write(text)
            
            # Generate MCQs with Gemini
            with st.spinner("🧠 Generating quiz..."):
                prompt = f"""Generate 5 high-quality MCQs from this lecture transcript. Follow these strict rules:

                            1. **Question Design**:
                            - Cover all key concepts proportionally
                            - Each question must test understanding, not just recall
                            - Use phrases like "Which statement best..." or "What is the primary reason..."

                            2. **Distractor Engineering**:
                            - Include 1 option that's *almost* correct but has a subtle flaw
                            - Include 1 common misconception
                            - Include 1 option that's related but irrelevant
                            - Make all options grammatically consistent

                            3. **Formatting**:\n
                            Q) [Question stem]\n
                            A) [Option 1]\n
                            B) [Option 2]\n
                            C) [Option 3]\n
                            D) [Option 4]\n\n
                            Answer: [Letter]\n
                            Explanation: [1-sentence justification]

                            4. **Difficulty**:
                            - 20% Easy (basic recall)
                            - 50% Medium (application)
                            - 30% Hard (analysis/evaluation)

                            Example:
                            Q) Which cognitive bias causes people to overestimate predictable events after they occur?\n
                            A) Confirmation bias\n
                            B) Hindsight bias\n
                            C) Availability heuristic\n
                            D) Anchoring effect\n\n
                            Answer: B\n
                            Explanation: Hindsight bias makes past events seem more predictable than they were.

                            Now generate for this transcript:
                            {text}"""
                
                try:
                    response = model.generate_content(prompt)
                    quiz = response.text
                    st.markdown("### 📝 Generated Quiz")
                    st.write(quiz)
                    
                    # Download button
                    st.download_button(
                        label="Download Quiz",
                        data=quiz,
                        file_name="quiz.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Gemini error: {str(e)}")