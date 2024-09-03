import os
import streamlit as st
import requests

def call_codestral_chat(messages, max_tokens=150, temperature=0.7):
    api_key = "CwrLyHiZC3KkU3G5FSNk1oBxAOMVBDju"
    url = "https://codestral.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()



# Streamlit app layout
st.title("CodeSage: Your AI Debugging Companion 🧠")
st.write("""
### Welcome to **CodeSage** 💻🧙‍♂️ **The ultimate interactive debugging tool.** 
Simply paste your code into the editor below and let our AI-powered assistant help you identify and fix issues in real time. Whether you're a novice coder or a seasoned developer, **CodeSage** is here to enhance your coding efficiency and problem-solving skills.
- 🛠️ **Interactive Debugging**
- 🔍 **Real-Time Analysis**
- 🧩 **AI-Powered Assistance**
""")


code_input = st.text_area("Enter your code below:", height=300)

if st.button("Debug Code"):
    with st.spinner('Analyzing code...'):
        # The suffix can be customized or left empty based on your use case
        # suffix = ""  # Or any specific suffix you need
        try:
            # result = call_codestral_completion(code_input, suffix)
            chat_result = call_codestral_chat([
                {"role": "system", "content": "You are a helpful debugger."},
                {"role": "user", "content": code_input}
            ])
            print(chat_result['choices'][0]['message']['content'])
            # completion_result = call_codestral_completion(code_input)
            # print(completion_result)
            # if 'choices' in result:
            st.success("Debugging complete!")
            st.subheader("Response:")
            st.write(chat_result['choices'][0]['message']['content'])
            # st.write(completion_result)
            # else:
            #     st.error("The 'choices' key is missing in the response.")
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.title("Pro Tips 🧙‍♂️")
st.sidebar.write("""
1. **Paste Your Code:** Enter your code snippet in the editor.
2. **Hit Debug:** Click on 'Debug Code' to receive instant feedback and suggestions.
3. **Review & Iterate:** Use the AI-generated insights to refine your code.
""")
