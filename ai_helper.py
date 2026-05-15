import urllib.request
import json
import os
import sys

error_text = sys.stdin.read()

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"A GitHub Actions build just failed. Here is the error:\n\n{error_text}\n\nIn 3 bullet points tell me: what went wrong, how to fix it, how to prevent it next time."
                }
            ]
        }
    ]
}

api_key = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

request = urllib.request.Request(
    url,
    data=json.dumps(payload).encode(),
    headers={"content-type": "application/json"}
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read())
    print(result["candidates"][0]["content"]["parts"][0]["text"])
