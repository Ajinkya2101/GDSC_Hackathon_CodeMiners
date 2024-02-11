import streamlit as st
import subprocess


def run_selected_file(selected_file):
    if selected_file == 'PDF Chat App':
        subprocess.Popen(['streamlit', 'run', 'app.py'])
    elif selected_file == 'Website Chat App':
        subprocess.Popen(['streamlit', 'run', 'app2.py'])
    else:
        st.error("Invalid selection")


def main():
    st.title('Choose an app you want to run \n 1. PDF Chat (app) \n 2. Website Chat (app2)')
    selected_file = st.selectbox('Select File:', ['PDF Chat App', 'Website Chat App'])
    if st.button('Run Selected File'):
        run_selected_file(selected_file)


if __name__ == "__main__":
    main()
