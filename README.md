# 🧠 Neuro Shield – Smart Packet Classifier

A machine learning-based network traffic classification system that categorizes packet flows into behavioral classes such as **Normal**, **Streaming**, and **Suspicious**, using structured flow features derived from real-world datasets.

---

## 🚀 Key Features

* 🤖 Random Forest-based classification model
* 📊 Trained on CICIDS dataset (45K+ samples)
* 📈 Achieves **~95% accuracy** with balanced precision-recall
* 🌐 Streamlit-based interactive web interface
* 📊 Real-time prediction visualization (bar charts)
* 📝 Automatic logging of predictions to CSV
* 📥 Downloadable logs for further analysis
* 🧠 Extensible pipeline for additional traffic features

---

## 📊 Model Performance

* **Dataset:** CICIDS (45K+ samples)
* **Model:** Random Forest
* **Accuracy:** **95.07%**
* **Precision / Recall:** ~0.94 – 0.96

---

## 🧠 How it Works

1. Extract network flow features
2. Feed features into trained ML model
3. Classify traffic into behavior categories
4. Display results via Streamlit dashboard
5. Log predictions for analysis

---

## 📂 Project Structure

SmallPacketClassifier/
├── train_model.py        # Model training script
├── streamlit_app.py      # Web interface
├── packet_model.pkl      # Saved model (ignored in Git)
├── cicids_aligned.csv    # Dataset (ignored in Git)
├── requirements.txt
└── README.md

---

## ⚙️ Setup & Run

# Clone repo

git clone <your-repo-link>

cd SmallPacketClassifier

# Create virtual environment

python3 -m venv venv
source venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Train model

python train_model.py

# Run app

streamlit run streamlit_app.py

---

## 🧠 Project Context

This project extends a broader network security pipeline by focusing on **multi-class traffic behavior classification**, complementing intrusion detection systems (IDS) that perform binary attack detection.

---

## 👩‍💻 Author

Developed by **Vibha R**
ECE | AI/ML | Networking Systems
