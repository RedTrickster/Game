import streamlit as st
import pandas as pd
import random
import json
import random

st.write("""
# AHHHH! This is a very scary quiz!
Very *scary*!
""")

# Initialize session state variables
if "initialized" not in st.session_state:
    st.session_state.initialized = False
    st.session_state.topic = ""
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.finished = False
    st.session_state.questions = []

# Topic selection phase
if not st.session_state.initialized:
    user_topic = st.text_input("What topic would you like to do? (History, Geography, Math, Astronomy, Computer Science): ")
    
    if st.button("Start Quiz") and user_topic:
        df = pd.read_json('quiz_dataset_extended-1.json')
        print(type(df))
        print(df)
        data = df[df.topic == user_topic]
        print(data)
        if len(data) >= 5:
            random_indices = random.sample(range(len(data)), 5)
            st.session_state.questions = [data.iloc[i] for i in random_indices]  
        else:
             st.session_state.questions = [for i in range(len(data))]
            
"""        
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



    """
