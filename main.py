import streamlit as st
from gtts import gTTS
import tempfile
import os

def main():
    st.header("Food SPARK!")

    choice = st.selectbox(
        "Gastronomy: Choose and learn Iloilo's best local dishes",
        ("Batchoy", "Pancit Molo", "Bibingka", "Palang’s Buko Pie", "Kansi")
    )

    food_maps = {
        "Batchoy": { 
            "history": "La Paz Batchoy originated in the La Paz district in the 1940s. A hearty noodle soup made with miki, pork, liver, and a flavorful broth.",
            "speak": "La Paz Batchoy is one of Iloilo’s most beloved comfort foods, originating from the La Paz district in the 1940s. This hearty noodle soup features freshly made miki noodles in a rich, savory broth, topped with thin slices of pork, tender liver, and crunchy chicharron. Traditionally served steaming hot, Batchoy is enjoyed by locals and visitors alike as a filling meal and a cultural icon of Iloilo. Popular spots like Netong’s, Ted’s, and Deco’s have been serving it for generations, preserving its authentic flavor.",
            "place": "La Paz Public Market, Iloilo City. (Deco’s, Netong’s, Ted’s)",
            "image": "./static/foods/La-Paz-Batchoy.jpg"
        },
        "Pancit Molo": {
            "history": "Pancit Molo is a dumpling soup from Molo district, inspired by Chinese settlers. It has no noodles, only dumpling wrappers.",
            "speak": "Pancit Molo is a comforting soup that traces its roots to the historic Molo district of Iloilo, once home to many Chinese settlers. Despite its name, it contains no actual noodles; instead, the dish features delicate dumpling wrappers filled with seasoned pork and shrimp. These are simmered in a flavorful chicken broth, creating a warm and hearty soup that’s perfect for rainy days. Pancit Molo reflects a fusion of Chinese culinary influence and Filipino taste, making it a symbol of Iloilo’s diverse food heritage.",
            "place": "Molo Plaza area, Iloilo City",
            "image": "./static/foods/Pancit-Molo.jpg"
        },
        "Bibingka": {
            "history":"Bibingka is a traditional Filipino rice cake that dates back to the Spanish colonial era. In Iloilo City, it became a popular delicacy enjoyed not just during Christmas after Simbang Gabi, but also as a year-round snack sold in markets and roadside stalls.",
            "speak": "The Biscocho Haus in Jaro, Iloilo, has been a household name since the 1970s, famous for its sweet, crunchy biscocho—twice-baked bread slices topped with butter and sugar. Equally beloved are its barquillos, thin rolled wafers sometimes filled with sweet polvoron. These treats are a staple pasalubong for travelers and a nostalgic snack for locals. The shop has preserved its recipes for decades, offering a taste of tradition and homegrown craftsmanship that continues to delight sweet-toothed visitors from all over the Philippines.",
            "place": "Public markets and local stalls in Iloilo City",
            "image": "./static/foods/bibingka.jpeg"
        },
        "Palang’s Buko Pie": {
            "history": "Palang’s Buko Pie in Oton is famous for its flaky crust and creamy coconut filling.",
            "speak": "Palang’s Buko Pie, found in the town of Oton, Iloilo, has earned a loyal following for its perfectly flaky crust and rich coconut filling. Made from fresh young coconuts, the pie boasts a creamy texture and natural sweetness that balances beautifully with its golden pastry shell. For years, travelers passing through Oton have made it a point to stop and take home a pie or two as pasalubong. Its enduring popularity is a testament to the Palang family’s commitment to quality and tradition.",
            "place": "Palang’s Buko Pie, Oton, Iloilo.",
            "image": "./static/foods/palangs-bukopie.jpeg"
        },
        "Kansi": {
            "history": "Kansi is an Ilonggo beef soup that combines the sourness of sinigang with the richness of bulalo, often flavored with batwan fruit for a distinctly regional taste.",
            "speak": "Kansi is a hearty Ilonggo beef soup often described as a cross between sinigang and bulalo. Originating from Negros Occidental but also popular in Iloilo, it features tender beef shank with bone marrow, simmered slowly until the meat is fall-off-the-bone tender. The broth is made tangy with batwan, a native fruit that gives it a unique regional sourness, and enriched by the marrow’s savory depth. Usually served steaming hot, kansi is both a comforting meal and a cultural emblem of Western Visayas cuisine, perfect for rainy days or festive gatherings.",
            "place": "Local eateries and specialty kansi houses in Iloilo City",
            "image": "./static/foods/Kansi.jpg"
}
    }

    st.subheader(choice)
    st.image(food_maps[choice]["image"], caption=choice)
    st.write(f"**History:** {food_maps[choice]['history']}")
    st.write(f"**Best Place to Try:** {food_maps[choice]['place']}")

    if st.button("🔊 Read History Aloud"):
        text_to_speak = food_maps[choice]['speak']
        tts = gTTS(text=text_to_speak, lang='en')

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            tmp_path = tmp_file.name

        audio_file = open(tmp_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        audio_file.close()
        os.remove(tmp_path)

if __name__ == "__main__":
    main()
