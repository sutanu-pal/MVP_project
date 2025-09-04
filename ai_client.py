import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # loads environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_explanation(topic: str) -> str:
    prompt = (
        f"Explain the following topic like I am 5 years old, using simple language and relatable analogies. "
        f"Avoid technical jargon. Write 2-3 short paragraphs.make sure to cover the important part.\n also give small notes on the topic at the end .\n\nTopic: {topic}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300,
    )
    return response.choices[0].message.content

def generate_follow_up_answer(topic: str, question: str) -> str:
    prompt = (
        f"You previously explained this topic simply: {topic}\n"
        f"Answer the follow-up question below simply and clearly in a brief manner:\n\n{question}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200,
    )
    return response.choices[0].message.content
