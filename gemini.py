import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API"])

genAIModel = genai.GenerativeModel("gemini-1.5-flash")
