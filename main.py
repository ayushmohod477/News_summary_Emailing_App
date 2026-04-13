from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os


load_dotenv()

Google_Api_Key = os.getenv("Google_Api_Key")

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=Google_Api_Key
                        )


def summarize(prompt):
    response = model.invoke(f"summarize these news in one para to mail the summary :{prompt}")
    summary = response.content[0]['text']
    return summary
