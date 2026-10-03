import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

 

load_dotenv()

model = ChatGroq(

api_key=os.getenv("GROQ_API_KEY"),

model="openai/gpt-oss-20b",

temperature=0

)

question = input("Ask a question: ")

response = model.invoke(question)

print(response.content)