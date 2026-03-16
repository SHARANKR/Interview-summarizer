AI Voice Interview Assistant
Overview

The AI Voice Interview Assistant is an AI-powered application built during a hackathon to help candidates during interviews by providing real-time speech transcription, automatic summarization, and filler phrase suggestions. The system listens to the user's speech, converts it into text, generates concise summaries of responses, and detects pauses to suggest natural filler phrases so that the conversation flow remains smooth. The main idea behind the project is to demonstrate how AI can assist users in communication-heavy scenarios such as interviews, presentations, or discussions.

The application is developed using Python with an interactive interface built using Streamlit. It integrates speech processing, natural language processing, and model inference in a single system to simulate an intelligent interview assistant.

Features

Real-time speech-to-text transcription

Automatic summarization of spoken responses

Pause detection with intelligent filler phrase suggestions

Performance metrics such as model load time and inference latency

Simple and interactive web interface

Tech Stack

Python

Streamlit for the user interface

SpeechRecognition for converting speech to text

ONNX Runtime for running the AI model

DistilBART CNN 12-6 for text summarization

pyttsx3 for generating spoken filler phrases

Project Structure
voice_interview_ai/

app.py                # Main Streamlit application
summarizer.py         # ONNX model inference for summarization
speech_engine.py      # Speech-to-text module
filler.py             # Pause detection and filler phrase generator
metrics.py            # Performance metrics

models/
   summarizer.onnx    # Summarization model

requirements.txt
How It Works

The user clicks Start Listening in the interface.

The system records audio through the microphone.

The speech is converted into text using the speech recognition module.

The transcript is stored and displayed in the interface.

When the user clicks Generate Summary, the transcript is processed by the summarization model.

The summarized response is displayed along with inference latency.

If the user pauses for more than a few seconds, the system suggests a filler phrase such as “That’s a great question” to maintain a natural conversational flow.

Installation
1. Clone the Repository
git clone <repository-url>
cd voice_interview_ai
2. Create Virtual Environment
python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Running the Application

Start the Streamlit server:

streamlit run app.py

Then open the application in your browser:

http://localhost:8501
Model Optimization

The summarization model was converted into ONNX format so it could run efficiently during inference using ONNX Runtime. This optimization reduces runtime overhead and improves execution speed.

An attempt was also made to quantize the model into a smaller and faster version to further reduce model size and improve latency. However, due to compatibility issues related to tensor type inference and certain graph operations in the ONNX model, the quantization process could not be completed successfully within the hackathon timeframe. As a result, the project uses the optimized ONNX model without quantization.

Challenges Faced

During the development of this project, several challenges were encountered:

Integrating speech recognition with a real-time web interface

Handling microphone dependencies and audio input

Running a transformer-based summarization model efficiently

Attempting model quantization, which resulted in compatibility issues

Managing state and user interactions within the Streamlit interface

Future Improvements

Some possible improvements for the project include:

Implementing real-time streaming speech recognition

Improving summarization quality and context awareness

Successfully applying model quantization or other optimization techniques

Adding conversation memory and context tracking

Deploying the system as a cloud-based AI assistant

Conclusion

The AI Voice Interview Assistant demonstrates how modern AI technologies such as speech recognition and transformer-based summarization can be integrated into a practical application. The project highlights the potential of AI-driven tools to assist users in interviews by improving communication flow, organizing responses, and providing helpful conversational support. It also provided valuable hands-on experience in integrating multiple AI components into a real-time interactive system.
