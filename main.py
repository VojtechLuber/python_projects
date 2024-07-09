import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Vojtech Luber")
    content = """
    I specialize in web development with a strong focus on JavaScript, Python, and PHP technologies.
     I am passionate about creating dynamic and responsive websites that provide a seamless user experience.
      Explore my portfolio to see some of my work and discover how I can help bring your ideas to life.
      Since high school, I've been enamored with programming. 
      Even during my 12-hour shifts at the factory, 
      I devoted my evenings to coding and pursued programming retraining at Technical University of Ostrava.
       This experience taught me that with dedication, anything is possible.
    """
    st.info(content)