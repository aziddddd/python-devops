import streamlit as st

st.beta_set_page_config(
    page_title="Page Title",
    # page_icon="path/to/favicon.ico",
    # initial_sidebar_state="expanded",
)

def main():
    st.sidebar.title('Sidebar Title')
    st.title('Title')
main()