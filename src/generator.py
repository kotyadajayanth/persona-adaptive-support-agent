import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(query, persona, context):

    if persona == "Technical Expert":

        style = """
        Give a detailed technical explanation.
        Explain root cause.
        Give troubleshooting steps.
        """

    elif persona == "Frustrated User":

        style = """
        Be empathetic.
        Use simple language.
        Reassure the user.
        """

    else:

        style = """
        Be concise.
        Focus on business impact.
        Avoid technical jargon.
        """

    prompt = f"""
    Persona:
    {persona}

    Context:
    {context}

    User Question:
    {query}

    Instructions:
    {style}

    Answer only using the provided context.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text