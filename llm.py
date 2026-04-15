from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
   model="gemini-2.5-flash", 
    temperature=0.3
)


def generate_tags(description: str):
    """
    This function uses Gemini (via LangChain) to extract meaningful tags
    from the agent description.
    """

    try:
        # Prompt sent to Gemini
        prompt = f"""
        Extract 3 to 5 meaningful keywords from this description:

       {description}

       Return ONLY a valid Python list like:
       ["tag1", "tag2", "tag3"]

       Do not include explanation.
       """

        # LLM processes the prompt
        response = llm.invoke(prompt)

        return response.content  # Gemini response format

    except Exception:
        # fallback if API fails
        return fallback_keywords(description)


def fallback_keywords(text: str):
    """
    Simple fallback logic if LLM fails.
    Splits text into words and returns unique ones.
    """
    words = text.lower().split()
    return list(set(words))[:5]
