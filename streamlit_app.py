# streamlit_app.py

import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
from datetime import datetime

# Load model
with open('packet_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Neuro Shield Packet Classifier", page_icon="🧠", layout="centered")

st.title("🧠 Neuro Shield - Smart Packet Classifier")
st.markdown("Analyze packet traffic and detect types with clarity, speed, and style.")

# Input fields
flow_duration = st.number_input("Flow Duration (ms)", min_value=0)
total_fwd = st.number_input("Total Forward Packets", min_value=0)
total_bwd = st.number_input("Total Backward Packets", min_value=0)
fwd_len = st.number_input("Forward Packet Length Mean (bytes)", min_value=0.0, format="%.2f")
bwd_len = st.number_input("Backward Packet Length Mean (bytes)", min_value=0.0, format="%.2f")

# Session state
if 'counts' not in st.session_state:
    st.session_state.counts = {'Normal': 0, 'Video Stream': 0, 'Suspicious': 0}

# Quotes
quotes = [
    "📡 Staying secure, one packet at a time!",
    "🌐 Smart traffic scan completed!",
    "🚀 Packet analysis done like a pro!",
    "🧠 Network IQ: Activated.",
    "🛡️ Safety first, always!"
]

def beautify(pred):
    return {
        "Normal": "✅ Normal Traffic 🌐",
        "Video Stream": "🎬 Video Stream Detected",
        "Suspicious": "🚨 Suspicious Activity!"
    }.get(pred, "❌ Unknown Traffic")

def save_log(data, prediction):
    file = 'packet_log.csv'
    header = "Timestamp,Flow Duration,Total Fwd Packets,Total Bwd Packets,Fwd Mean,Bwd Mean,Prediction\n"
    row = f"{datetime.now()},{','.join(map(str, data))},{prediction}\n"
    write_header = not os.path.exists(file)
    with open(file, 'a') as f:
        if write_header:
            f.write(header)
        f.write(row)

# Screenshot function (Streamlit way)
screenshot_trigger = st.empty()

# Predict button
if st.button("🚀 Classify Traffic"):
    features = [[flow_duration, total_fwd, total_bwd, fwd_len, bwd_len]]
    prediction = model.predict(features)[0]

    # Update count
    if prediction in st.session_state.counts:
        st.session_state.counts[prediction] += 1

    # Show result
    st.success(beautify(prediction))
    st.caption(random.choice(quotes))

    # Save to log
    save_log([flow_duration, total_fwd, total_bwd, fwd_len, bwd_len], prediction)

# Live chart
st.subheader("📊 Live Traffic Summary")

labels = list(st.session_state.counts.keys())
values = list(st.session_state.counts.values())

fig, ax = plt.subplots()
ax.bar(labels, values, color=['green', 'blue', 'red'])
ax.set_ylabel("Count")
ax.set_title("Traffic Type Frequency")

st.pyplot(fig)

# CSV log
if os.path.exists("packet_log.csv"):
    with open("packet_log.csv", "rb") as f:
        st.download_button("📥 Download CSV Log", f, file_name="packet_log.csv")

# Save screen snapshot link (Streamlit style)
st.markdown(
    "[📸 Save Screenshot: Use browser 'Print to PDF/Image'](javascript:window.print())",
    unsafe_allow_html=True,
)

# Footer
st.markdown("---")
st.markdown("👩‍💻 **Project by: Neuro Shield** 🧠")
