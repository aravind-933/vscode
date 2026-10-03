import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

 

# Load variables from the .env file

load_dotenv()

 

# Read the API key

api_key = os.getenv("GROQ_API_KEY")
 

# Check whether the API key exists

if not api_key:

    raise ValueError("GROQ_API_KEY is missing from the .env file")

 

# Connect to the language model

model = ChatGroq(

    api_key=api_key,

    model="openai/gpt-oss-20b",

    temperature=0

)

 

# Create a prompt template

prompt = ChatPromptTemplate.from_template(

    """

    You are a friendly teacher.

    Explain the following topic in simple language.

    Give one real-life example.

    Topic: {topic}

    """

)

 

# Connect the prompt and model

chain = prompt | model

 

# Get input from the student

student_topic = input("Enter a topic: ")

 

# Run the chain

response = chain.invoke(

    {"topic": student_topic}

)

 

# Display the final answer

print("\nAnswer:\n")

print(response.content)