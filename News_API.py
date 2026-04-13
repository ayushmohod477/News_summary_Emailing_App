import requests
from send_email import send_email
from main import summarize


topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}&sortBy="
       "publishedAt&"
       "apiKey=890603a55bfa47048e4490069ebee18c&language=en")

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
