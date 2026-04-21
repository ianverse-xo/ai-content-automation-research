import os
import time
import requests
from dotenv import load_dotenv
from instagrapi import Client
from openai import OpenAI

load_dotenv()

# Setup OpenAI
ai_client = OpenAI(api_key=os.getenvsk-proj-gWXIs14rV2_Wj2hqaZaL_vq2hH8pPSPueMvi9YBSdFtOIpkziKBGPeMObmOhPFBjjexidL1Q5xT3BlbkFJ1QAxWfc4WuN6MtDSkYeEkWuA0hYJz5kczhxsWFdz4X_Rj6AsxpFdsEQesJ2iksPq5-WVRd_awA
                  )
def get_viral_idea():
    print("🔍 Scouting for daily trends...")
    # This tells the AI to act as a trend-setter
    prompt = "Find a trending Gen-Z lifestyle topic today. Create a viral idea for an AI girl influencer to post about. Keep it lively and fun."
    response = ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def produce_content(trend_idea):
    print(f"💡 Thinking of a caption for: {trend_idea}")
    # Generate the Caption
    caption_res = ai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Write a high-energy Instagram caption for this idea: {trend_idea}. Use Gen-Z slang, emojis, and 5 trending hashtags."}]
    )
    caption = caption_res.choices[0].message.content
    
    # Placeholder for your Fal.ai Image URL
    # In the future, we will put the actual image-making code here
    image_url = "https://your-generated-image-link.com" 
    
    return image_url, caption

def ignition_and_post(url, caption):
    cl = Client()
    print("🔐 Logging into Instagram...")
    cl.login(os.getenvitz_.allabout_.mih, os.getenvrichardian16)
    
    # Download the image temporarily
    with open("upload_me.jpg", "wb") as f:
        f.write(requests.get(url).content)
        
    print("📤 Pushing content live!")
    cl.photo_upload("upload_me.jpg", caption)
    print("✅ Success!")

if __name__ == "__main__":
    print("🚀 Aura Dynamic 2.0 is starting...")
    while True:
        try:
            idea = get_viral_idea()
            img, text = produce_content(idea)
            ignition_and_post(img, text)
            
            print("😴 Post finished. Waiting 12 hours for the next trend...")
            time.sleep(43200)
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(3600) # Wait an hour if something fails
