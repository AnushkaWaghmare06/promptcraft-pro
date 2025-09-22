from typing import Dict
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_code(
    prompt: str, frontend_framework: str = "react-tailwind", backend_framework: str = "fastapi"
) -> Dict[str, str]:
    """
    Call OpenAI LLM to generate frontend + backend code.
    Returns a dict: {"frontend_code": "...", "backend_code": "..."}
    """
    try:
        system_prompt = f"""
        You are an expert full-stack developer.
        Generate code based on the user's prompt.

        Frontend Framework: {frontend_framework}
        Backend Framework: {backend_framework}

        Return a JSON object strictly in this format:
        {{
            "frontend_code": "<string with frontend code>",
            "backend_code": "<string with backend code>"
        }}
        """

        # Call OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # ✅ Use latest stable small model (faster + cheaper than gpt-4)
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        code_text = response.choices[0].message.content.strip()

        # Try to parse JSON from model output
        try:
            code_json = json.loads(code_text)
            return {
                "frontend_code": code_json.get("frontend_code", "").strip(),
                "backend_code": code_json.get("backend_code", "").strip(),
            }
        except json.JSONDecodeError:
            # Fallback if AI didn’t return valid JSON
            return {
                "frontend_code": f"// AI output not JSON:\n{code_text}",
                "backend_code": "# AI output not JSON",
            }

    except Exception as e:
        return {
            "frontend_code": f"// Error: {str(e)}",
            "backend_code": f"# Error: {str(e)}",
        }
