# data/ask_gpt.py — mock or live GPT insights 
import os 
# UNCOMMENT WHEN USING OPENAI 
# import openai 
# from dotenv import load_dotenv 
# load_dotenv() 
# openai.api_key = os.getenv("OPENAI_API_KEY") 
def ask_gpt(question, context=""): 
    # UNCOMMENT THIS WHEN USING OPENAI 
    # prompt = f"You are an MLB analytics expert. Based on this HR prediction data:\n{context}\n\nAnswer: {question}" 
    # response = openai.ChatCompletion.create( 
    # model="gpt-4", 
    # messages=[{"role": "user", "content": prompt}] #) 
    # return response['choices'][0]['message']['content'] 
    return "🧠 [Mock GPT Response] This would be a smart, insightful answer using HR probabilities and context."
