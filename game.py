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
        data = df[df.topic.str.lower() == user_topic]
        if len(data) >= 5:
            random_indices = random.sample(range(len(data)), 5)
            st.session_state.questions = [data.iloc[i] for i in random_indices]  
        else:
             st.session_state.questions = [data.iloc[i] for i in range(len(data))]
        st.session_state.initialized = True
        st.session_state.topic = user_topic
        st.session_state.index = 0
        st.rerun()

elif not st.session_state.finished:
    if st.session_state.index < len(st.session_state.questions):
        st.write(f"Question {st.session_state.index + 1} of {len(st.session_state.questions)}")
        question = st.session_state.questions[st.session_state.index]["question"]
        correct_answer = st.session_state.questions[st.session_state.index]["correct_answer"]
        user_answer = st.text_input(f"{question} \nANSWER!!!!!!!", key=f"q_{st.session_state.index}")

        if st.button("Submit"):
            is_correct = user_answer.lower() == correct_answer.lower()
            st.session_state.user_answers.append({
                "question": question,
                "your_answer": user_answer,
                "correct_answer": correct_answer[0],
                "is_correct": user_answer.lower() == correct_answer[0].lower()
            })
            print(correct_answer[0]) 
            print(question)
            print(user_answer)
            print(is_correct)
            print(correct_answer)
            if is_correct == True:
                st.session_state.score += 1
                st.success("WOWOWOWOW",icon="✅")
            else:
                st.error("NONONONO",icon="🚨")
                
            if st.button("Next"):
                print("AHHH")
                st.rerun()
            st.session_state.index += 1
    else:
        st.success(f"Well Done! You did all 5 questions! You can now leave freely. Your final score was {st.session_state.score}!")

    

        