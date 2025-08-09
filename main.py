import streamlit as st

def main():
    st.header("Food SPARK!")

    choice = st.selectbox("Gastronomy: Choose and learn Iloilo's best local dishes",
                          ("La Paz Batchoy", "Molo", "Jaro", "Arevalo (Villa)", "Oton"))
    st.write(choice)

if __name__ == "__main__":
    main()
