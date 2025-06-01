# 📹 Video Metadata Generator using LangChain & Gemini

This Python script leverages Google's **Gemini 1.5 Flash** model via LangChain to **automatically generate SEO-optimized metadata** for videos based on their transcripts.

It outputs a structured JSON containing:
- 📌 A compelling **title**
- 📝 An engaging **description**
- 🔖 A list of 10–15 relevant **tags**

---

## ✅ Features

- Uses **LangChain** with **Gemini API (via `langchain-google-genai`)**
- Accepts a transcript and generates metadata in **clean JSON format**
- Designed for **YouTube creators**, **automation tools**, and **SEO pipelines**

---

## 🧪 Example

### ▶️ Input Transcript
```text
Welcome to our tutorial on Python automation. In this video, we will cover how to use Python to automate 
repetitive tasks such as web scraping, file handling, and data processing. Whether you're a beginner or 
an advanced programmer, this video will help you streamline your workflow with Python.

```
---

## ▶️ Output Transcript

<pre lang="markdown"> ```
{
  "title": "Master Python Automation: Web Scraping, File Handling & More",
  "description": "Discover how to streamline your tasks using Python in this hands-on tutorial. Learn practical automation tips covering web scraping, file handling, and data processing techniques. Whether you're a beginner or pro, this video will enhance your productivity.",
  "tags": ["python", "automation", "web scraping", "file handling", "data processing", "python tutorial", "workflow automation", "scripting", "tech tips", "productivity", "learn python", "python coding", "how to automate", "python automation", "python tasks"]
}
 ``` </pre>
