import requests
import json
import sys
import re
from bs4 import BeautifulSoup

ollama_url = ' http://localhost:11434/api/generate'

if len(sys.argv) < 2 :
    print("Usage: python script.py <url>")
    sys.exit(1)

web_url = sys.argv[1]

def get_summary(url, webpage_text):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "llama3.2",
        "prompt": "Write down the key points of the following text. \nText:"+webpage_text,
        "stream": False,
        "format": {
            "type": "object",
            "properties": {
                "key-points": {
                    "type": "array"
                },
                "feel":  {
                    "enum": ["positive", "negative", "neutral"]
                }
            },
            "required": [
                "summary"
            ]
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        data = response.json()
        return data.get('response', 'No summary provided')
    else:
        return f"Error: {response.status_code} - {response.text}"
# End of get_summary

#get the web page
response = requests.get(web_url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML tag with the specific class name
# Replace 'div' with the tag name and 'example-class' with the class name
# tag = soup.find('div', class_='article-body')
tag = ""
if (re.match(r'.*\.yahoo\.com/.*', web_url)):
    tag = soup.find('div', class_='body yf-tsvcyu')
elif (re.match(r'.*\.fool\.com/.*', web_url)):
    tag = soup.find('div', class_='article-body')
elif (re.match(r'.*\.cnn\.com/.*', web_url)):
    tag = soup.find('div', class_='article__content-container')
else:
    tag = soup # unknown page

# Replace 'index.html' with your webpage file name and path
webpage_content = tag.get_text()

print ("Content:"+ webpage_content)

# webpage_content = '''
# Long text
# '''

summary = get_summary(ollama_url, webpage_content)

if summary:
    print(summary)
else:
    print("Failed to generate a summary.")
