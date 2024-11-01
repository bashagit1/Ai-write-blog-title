import os
import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title and description for the Streamlit app
st.title("SEO-Optimized Blog Title Generator")
st.write("""
    Welcome to the SEO-Optimized Blog Title Generator! 
    This tool helps you generate catchy, SEO-friendly blog titles using the OpenAI API. 
    Just enter your blog topic, and let the app create engaging title ideas.
""")

# Input for blog topic
blog_topic = st.text_area(
    "Enter your blog topic:",
    placeholder="e.g., Digital Marketing Tips",
    help="Enter the topic of your blog post. The model will generate titles based on this."
)

# Generate button
if st.button("Generate Titles"):
    # Ensure the blog topic is not empty
    if blog_topic.strip() == "":
        st.warning("Please enter a blog topic to generate titles.")
    else:
        # Define the prompt for title generation
        prompt = f"Generate 10 catchy SEO-optimized blog titles for the topic: {blog_topic}."

        # Call the OpenAI API to generate titles
        with st.spinner("Generating titles..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="gpt-3.5-turbo",
                )

                # Extract the generated text correctly
                generated_text = chat_completion.choices[0].message.content.strip()

                # Split the generated text into lines/titles
                generated_titles = generated_text.split('\n')

                # Display the generated titles
                st.subheader("Generated Blog Titles")
                for idx, title in enumerate(generated_titles, 1):
                    st.write(f"{idx}. {title}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
