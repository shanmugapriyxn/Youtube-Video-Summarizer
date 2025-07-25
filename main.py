import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("Youtube Video Summarizer")

youtube_url=st.text_input("Youtube Video URL")

if st.button("Summarize video"):
    loader = YoutubeLoader.from_youtube_url(youtube_url)

    data =loader.load()
    transcript =data[0].page_content

    prompt = ChatPromptTemplate.from_messages([("system","You are a helpful AI assistant specialized in summarizing YouTube video transcripts. Provide a easy-to-understand summary of the following transcript: "),("human","{transcript}")])

    chain = prompt | llm

    summary = chain.invoke({"transcript":transcript})

    st.write(summary.content)



    