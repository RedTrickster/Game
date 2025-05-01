import streamlit as st
import pandas as pd
import random
import json

st.write("""
# AHHHH! This is a very scary quiz!
Very *scary*!
""")

df = pd.read_json('/Users/caedenshaw/Desktop/School 2025/Robotics & Coding/Caeden Shaw R&C Assesment/quiz_dataset_extended-1.json')
user_topic = st.text_input("What topic would you like to do? (History, Geography, Math, Astromony, Computer Science): ")
data = df[df.topic == user_topic]
# Initialize session state variables
if "index" not in st.session_state:
    st.session_state.data = data
    st.session_state.topic = user_topic
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.finished = False
if not st.session_state.finished:
    question = data.iloc[st.session_state.index]["question"]
    correct_answer = data.iloc[st.session_state.index]["answer"]
    user_answer = st.text_input("ANSWER!!!!!!!", key=f"q_{st.session_state.index}")
    print(question)
    print(user_answer)
    if st.button("Submit"):
        st.session_state.user_answers.append({
            "question": question,
            "your_answer": user_answer,
            "correct_answer": correct_answer[0],
            "is_correct": user_answer.lower() == correct_answer[0].lower()
        })
        print(correct_answer[0])
        if str(correct_answer[0]) == str(user_answer):
            st.success("WOWOWOWOW",icon="✅")
            quest.remove(question)
            score += 1
        else:
            st.error("NONONONO",icon="🚨")
    st.success(f"Well Done! You did all 5 questions! You can now leave freely. Your final score was {st.session_state.score}!")