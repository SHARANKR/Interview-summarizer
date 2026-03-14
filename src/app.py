import streamlit as st

from speech_engine import listen
from summarizer import generate_summary
from filler import detect_pause, update_time
from metrics import load_time

st.set_page_config(layout="wide")

st.title("AI Voice Interview Assistant")

st.write("Real-time summaries and filler phrases")

# Session memory
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

col1, col2 = st.columns(2)

# Speech input
with col1:

    st.subheader("Speech Input")

    if st.button("Start Listening"):

        speech = listen()

        if speech:

            update_time()

            st.session_state.transcript += " " + speech

            st.success("Speech captured")

# Summary generation
with col2:

    st.subheader("Generate Summary")

    if st.button("Generate Summary"):

        if st.session_state.transcript:

            summary, latency = generate_summary(
                st.session_state.transcript
            )

            st.session_state.summary = summary

            st.success(f"Latency: {latency:.2f} ms")

# Display transcript
st.subheader("Transcript")
st.write(st.session_state.transcript)

# Display summary
st.subheader("Summary")
st.write(st.session_state.summary)

# Pause detection
pause = detect_pause()

if pause:
    st.warning(f"Suggested filler: {pause}")

# Metrics
st.subheader("Metrics")
st.write(f"Model load time: {load_time():.2f} ms")