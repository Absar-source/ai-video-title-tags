from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
import re
import os
# API Key environment variable se load kar raha hai
api_key = os.getenv("GOOGLE_API_KEY")

# Gemini Model Initialize karna
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ.get("GOOGLE_API_KEY"))

# Prompt Template Define Karna
# Define Prompt Template
template = """You are an expert video content analyzer specializing in generating engaging and SEO-friendly metadata.
Based on the provided video transcript, generate a **structured JSON response** containing:

1. **title**: A compelling and click-worthy video title.
2. **description**: A concise and engaging video description (max 200 words).
3. **tags**: A list of 10-15 relevant SEO-friendly tags.

### Video Transcript:
{transcript}

### Expected JSON Output Format:
{{
  "title": "Your generated video title",
  "description": "Your detailed video description",
  "tags": ["tag1", "tag2", "tag3", ..., "tag15"]
}}

Ensure the response is **valid JSON format** and properly structured.
"""


# Create PromptTemplate Object
prompt = PromptTemplate(
    input_variables=["transcript"], 
    template=template
)
transcript_example = """
Welcome to our tutorial on Python automation. In this video, we will cover how to use Python to automate 
repetitive tasks such as web scraping, file handling, and data processing. Whether you're a beginner or 
an advanced programmer, this video will help you streamline your workflow with Python.
"""

# LLM Chain Banana
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Test Run
# Convert Response to Dictionary (if needed)
response = llm_chain.run({"transcript": transcript_example})
cleaned_response = re.sub(r"```json\n(.*)\n```", r"\1", response, flags=re.S).strip()
try:
    response_json = json.loads(response)
    print(response_json)
except json.JSONDecodeError:
    print("Invalid JSON response:", response)
