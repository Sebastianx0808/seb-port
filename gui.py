import streamlit as st

def about_section():
    st.title("About Me")
    st.write("Hello! I'm Sebastian Jose, a passionate software engineer with a keen interest in artificial intelligence and open source contributions. I love building innovative solutions that make a difference in people's lives. With a strong foundation in software development, I enjoy tackling complex problems and continuously learning new technologies. When I'm not coding, you can find me exploring the latest trends in AI, contributing to open source projects, or sharing my knowledge with the community. Let's connect and collaborate on exciting projects!")

def contact_section():
    st.title("Contact Me")
    container = st.container()
    with container:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Connect with me on LinkedIn")
            st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/sebastian-jose-123456789/)")
        with col2:
            st.subheader("Follow me on GitHub")
            st.markdown("[GitHub Profile](https://github.com/sebastianjose12)")
    st.subheader("Get in Touch")
    st.write("Feel free to reach out for collaborations, questions, or just to say hi!")
    st.write("Email me at: [sebastianjose12.m@gmail.com](mailto:sebastianjose12.m@gmail.com)")
    st.write("Phone Number: +91 7356711236")

def main_section():
    st.title("Sebastian Jose")
    st.image("KP.JPG", width=150)
    st.subheader("Software Engineer | AI Enthusiast | Open Source Contributor")
    

def main():
    st.title("Personal Portfolio")
    if "current_section" not in st.session_state:
        st.session_state.current_section = "Home"

    st.sidebar.title("Navigation")
    if st.sidebar.button("Home"):
        st.session_state.current_section = "Home"
    if st.sidebar.button("About"):
        st.session_state.current_section = "About"
    if st.sidebar.button("Contact"):
        st.session_state.current_section = "Contact"

    if st.session_state.current_section == "Home":
        main_section()
    elif st.session_state.current_section == "About":
        about_section()
    elif st.session_state.current_section == "Contact":
        contact_section()


if __name__ == "__main__":
    main()
