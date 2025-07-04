
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from LLaMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    try:
        # Load the LLaMA model
        llm = CTransformers(
            model=r"C:\Users\DIPIKA VISHWAKARMA\Downloads\llama-2-7b-chat.ggmlv3.q4_0.bin",

            model_type='llama',
            config={
                'max_new_tokens': 200,  # You can change this to no_words if numeric
                'temperature': 0.7
            }
        )
        print("✅ Model loaded successfully")

        # Prompt Template
        template = """
        Write a {no_words}-word blog for a {blog_style} audience on the topic: "{input_text}".
        Make it engaging and easy to understand.
        """

        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )

        formatted_prompt = prompt.format(
            blog_style=blog_style,
            input_text=input_text,
            no_words=no_words
        )

        print("📝 Prompt formatted successfully")

        # Generate response
        response = llm(formatted_prompt)
        print("✅ Response generated successfully")

        return response

    except Exception as e:
        print(f"❌ Error in getLLamaresponse: {e}")
        return "An error occurred while generating the blog."


# Streamlit UI
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Two columns for No. of words and Blog style
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )

submit = st.button("Generate")

# Final response with spinner
if submit:
    if input_text and no_words:
        with st.spinner('Generating blog... please wait ⏳'):
            output = getLLamaresponse(input_text, no_words, blog_style)
            st.subheader("📝 Generated Blog")
            st.write(output)
    else:
        st.warning("⚠️ Please fill in all fields before generating.")
