import urllib.request
import json
import os
import sys
import time

error_text = sys.stdin.read()

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "A GitHub Actions build just failed. Here is the error:\n\n" + error_text + "\n\nIn 3 bullet points tell me: what went wrong, how to fix it, how to prevent it next time."
                }
            ]
        }
    ]
}

api_key = os.environ["GEMINI_API_KEY"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key=" + api_key

for attempt in range(3):
    try:
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"content-type": "application/json"}
        )
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read())
            print(result["candidates"][0]["content"]["parts"][0]["text"])
            break
    except Exception as e:
        print("Attempt " + str(attempt + 1) + " failed: " + str(e))
        if attempt < 2:
            print("Waiting 30 seconds before retry...")
            time.sleep(30)
