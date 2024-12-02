import streamlit as st
from PIL import Image
import requests

URL_Main_Server = 'http://127.0.0.1:8000'
URL_Bento_Server = 'http://localhost:3000'

st.write("""# Сирвис для распознование лиц""")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
if image_file is not None:
    img = Image.open(image_file)
    
    st.image(img ,width=250)
    response_get = requests.post(URL_Main_Server + '/api/get_person/', params={'img': img})
    name = response_get.json()["name"]
    st.write(name)
    if name == '':
        new_name = st.text_input("Имя человека", "")
        if st.button("Добавить в БД"):
            response_post = requests.post(URL_Main_Server + '/api/new_person/', params={'name': new_name, 'img': img})
            if response_post.status_code == 200:
                st.write("Пользователь добавлен.")
            else:
                st.write("Ошибка! Пользователь уже добавлен в БД.")
