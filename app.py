import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


## function to get response from LLama 2 model


def getLLamaresponse(input_text, no_words, blog_style):
    """
    Function to get response from LLama 2 model
    
    """

    llm = CTransformers(
        model='C:/Work/Personal Projects/LLM Models/LLama 2/llama-2-7b-chat/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )

    # Prompt Template
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "n_words"], template=template
    )

    ## Generate the response from the LLama 2 model

    response = llm(
        prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    )

    print(response)

    return response


st.set_page_config(page_title = "Generate Blogs",
                    page_icon = "🤖",
                    layout = 'centered',
                    initial_sidebar_state= "collapsed")

st.header("generate Blogs 🤖")
input_text = st.text_input('Enter the Blog Topic')

# Creating 2 more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('writing the blog for',("Researchers", "Data Scientist", "Common people"), index=0)


submit = st.button("Generate")


## Final response

if submit:
    
      st.write(getLLamaresponse(input_text, no_words, blog_style))