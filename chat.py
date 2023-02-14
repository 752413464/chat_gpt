import openai
import streamlit as st
from streamlit.elements.image import image_to_url

st.set_page_config(page_title="ChatGPT", page_icon="🤖")



openai.api_key = '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'

def get_response(prompt):
    request = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 1024,
        top_p = 1,
        stop = None,
        temperature=0.2,
    )
    feedback = request.choices[0].text
    return feedback

st.markdown(f'<p style="background-image: linear-gradient(to right, #ff1a1a, #ff8080 ,#ffffff);background-color:;color:white;font-size:24px;border-radius:1rem;">与ChatGPT进行对话</p', unsafe_allow_html=True)
user_input = st.empty().text_input(label="请输入你要提问的问题, 输入完成后按回车键提交！")
record = []
if len(user_input) > 0:
    with st.spinner("请稍后，Chatgpt🤖正在快速思考"):
        st.info(get_response(user_input))
