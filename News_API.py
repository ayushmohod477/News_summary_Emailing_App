import requests
from send_email import send_email
from main import summarize
from dotenv import load_dotenv
import os


load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}&sortBy="
       "publishedAt&"
       f"apiKey={NEWS_API_KEY}")

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][0:20]:
    title = article["title"] or ""
    description = article["description"] or ""
    link = article["url"] or ""

    body += f"{title}\n{description}\n{link}\n\n"

body = summarize(body)
body = body.encode("utf-8")
send_email(body)
