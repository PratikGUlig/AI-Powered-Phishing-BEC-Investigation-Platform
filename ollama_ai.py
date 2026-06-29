import requests
import json


def explain(indicators):

    prompt = f"""
You are a SOC Analyst.

Analyze the following phishing indicators and explain why this email appears suspicious.

Indicators:

{indicators}

Provide:
1. Summary
2. Why it is suspicious
3. Recommended action

Keep the explanation simple and professional.
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",

            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },

            timeout=120
        )

        # Check if request succeeded
        if response.status_code != 200:
            return f"Ollama Error: HTTP {response.status_code}"

        data = response.json()

        # Debugging (optional)
        print("OLLAMA RESPONSE:")
        print(json.dumps(data, indent=2))

        # Current Ollama format
        if "response" in data:
            return data["response"]

        # Some newer APIs return message/content
        if "message" in data:
            if "content" in data["message"]:
                return data["message"]["content"]

        return str(data)

    except Exception as e:
        return f"Ollama Exception: {str(e)}"