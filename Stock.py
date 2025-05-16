import streamlit as st
import yfinance as yf
from plotly import graph_objects as go
import pandas as pd

# Function to create a card
def create_card(title, description, image_url, link):
    st.markdown(
        f"""
        <a href="{link}" target="_blank" style="text-decoration: none;">
            <div style="background-image: url('{image_url}'); background-size: cover; height: 300px; border-radius: 10px; padding: 20px; color: white; display: flex; flex-direction: column; justify-content: flex-end; margin: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# Main function to run the app
def main():
    st.set_page_config(page_title="Dashboard", layout="wide")

    # Navigation menu
    menu = ["Home", "Analyze Stock Trends", "Page 2"]
    choice = st.sidebar.selectbox("Select a page", menu)

    # Set background image for the pages
    if choice == "Home":
        st.markdown(
            """
            <style>
            .main {
                background-image: url('https://via.placeholder.com/800x600');
                background-size: cover;
                background-repeat: no-repeat;
                padding: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.title("Stock Price Predictor using Transformer Project")
        st.subheader("Explore various companies that are pioneer in their fields.")

        st.write("""
            ***The Stock Price Prediction Dashboard is designed to provide an interactive comparison of stock predictions for five companies, alongside their competitors. It visualizes short-term stock price movements predicted by a lightweight Transformer model, allowing users to analyze trends, assess the accuracy of predictions, and make data-driven decisions. With a clean and intuitive interface, the dashboard offers a seamless experience for monitoring multiple stocks and their market performance.***
           """)


        # Create a grid layout for cards
        cols = st.columns(3)

        # Card data
        card_data = [
            {
                "title": "Apple",
                "description": " Revolutionizing consumer technology with iconic devices like the iPhone and Mac, blending innovation with style to define modern lifestyles.",
                "image_url": "https://cdn.pixabay.com/photo/2016/11/19/13/53/apple-1839363_960_720.jpg",
                "link": "https://apple.com"
            },
            {
                "title": "Amazon",
                "description": "A global e-commerce giant, transforming industries with its vast product offerings, fast delivery, and pioneering cloud computing services through AWS",
                "image_url": "https://cdn.pixabay.com/photo/2021/02/03/12/35/guinea-pig-5977807_960_720.jpg",
                "link": "https://amazon.com"
            },
            {
                "title": "Wells Fargo",
                "description": "A financial services leader offering a wide range of banking, investment, and mortgage solutions, known for its strong customer focus and global reach.",
                "image_url": "https://www.investopedia.com/thmb/suQ3TaNEgrUgYV3EUw9fQQfupmI=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/INV_WellsFargo_GettyImages-1529602605-9e520021baa84f258bf1d52f78f7fabb.jpg",
                "link": "https://wellsfargo.com"
            },
            {
                "title": "Tesla",
                "description": "Redefining the automotive and energy industries by producing cutting-edge electric vehicles and advancing sustainable energy solutions for a greener future.",
                "image_url": "https://cdn.pixabay.com/photo/2016/10/08/22/34/tesla-1724773_960_720.jpg",
                "link": "https://tesla.com"
            },
            {
                "title": "Pfizer",
                "description": "A global leader in the pharmaceutical industry, driving medical innovation with life-saving drugs, vaccines, and cutting-edge research to improve global health.",
                "image_url": "https://img-cdn.thepublive.com/fit-in/1280x960/filters:format(webp)/entrackr/media/media_files/2024/11/12/fqgE7TuRs2ahfN0D9Wwo.png",
                "link": "https://pfizer.com"
            },
        ]

        # Display cards
        for i, card in enumerate(card_data):
            with cols[i % 3]:
                create_card(card["title"], card["description"], card["image_url"], card["link"])

    if choice == "Analyze Stock Trends":
     st.markdown(
        """
        <style>
        .main {
            background-image: url('https://via.placeholder.com/800x600');
            background-size: cover;
            background-repeat: no-repeat;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
     st.title("Stock Data Viewer")
     d=pd.read_csv('PFE2.csv')
     st.dataframe(d)

    elif choice == "Page 2":
        st.markdown(
            """
            <style>
            .main {
                background-image: url('https://via.placeholder.com/800x600');
                background-size: cover;
                background-repeat: no-repeat;
                padding: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.title("Page 2")
        st.write("Content for Page 2")

if __name__ == "__main__":
    main()