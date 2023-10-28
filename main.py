from flask import Flask, request
import litellm, dotenv
import random

dotenv.load_dotenv()
app = Flask(__name__)

default_messages = [
    """I can't believe how hot it is outside today.""",
    """Have you seen the latest episode of that TV show? It's mind-blowing!""",
    """I had the most delicious dinner at this new restaurant last night.""",
    """Do you have any plans for the weekend?""",
    """I'm feeling really stressed about this upcoming project deadline""",
    """Did you hear about the new store opening in the mall? I'm so excited!""",
    """I just got a puppy, and he's the cutest thing ever!""",
    """I'm struggling with the decision of whether to quit my job or not.""",
    """I passed my driving test today! I'm officially a licensed driver!""",
    """I'm planning a trip to Europe next summer. Any recommendations?""",
    """You know, I've been thinking a lot about the environment lately. It's concerning to see the impact of pollution and climate change on our planet. I believe we all need to take responsibility and make more sustainable choices. By reducing our use of single-use plastics, conserving energy, and supporting renewable energy sources, we can make a positive difference. It's important for individuals, governments, and corporations to come together and implement policies and practices that protect our environment for future generations.""",
    """I recently read this incredible book that completely changed my perspective on life. The author explored themes of self-discovery, resilience, and the power of human connection. It made me reflect on my own journey and the importance of embracing vulnerability. This novel touched my soul and reminded me of the complexity and beauty of human experiences. I think everyone should read it; it truly is a transformative piece of literature.""",
    """I had a deeply meaningful conversation with a close friend the other day, and it made me realize the importance of open and honest communication in relationships. We discussed our fears, insecurities, and shared our dreams, which created a profound sense of understanding and connection between us. It's incredible how vulnerability can strengthen bonds and foster deeper connections. It made me appreciate the value of authentic conversations and the power they have to bring people closer together.""",
    """I recently had the opportunity to travel to a remote village in a developing country for a volunteer project. It was eye-opening to witness the challenges and resilience of the local community. Despite facing adversity, they were filled with warmth, kindness, and an unwavering spirit. Interacting with the villagers and collaborating on sustainable development initiatives was a truly humbling experience. It reminded me of the importance of empathy and giving back to those in need. I hope to continue supporting similar causes and making a positive impact in the lives of others."""
]

@app.route("/chat/completions")
def chat_completions(): 
    global default_messages
    print("request received")
    message = random.choice(default_messages)
    messages = [{"role": "user", "content": message}]
    response = litellm.completion(model="gpt-3.5-turbo", messages=messages, 
                       fallbacks=[{"model": "azure/gpt-turbo", "api_key": "6a5ae4c5b2bd4e8088248067799c6899", "api_base": "https://openai-france-1234.openai.azure.com/"}, 
                                  {"model": "azure/chatgpt-v-2", "api_key": "6314c6dc63f448c9873844297f408c74", "api_base": "https://openai-gpt-4-test-v-1.openai.azure.com/"},
                                  {"model": "azure/chatgpt-functioncalling", "api_key": "6314c6dc63f448c9873844297f408c74", "api_base": "https://openai-gpt-4-test-v-1.openai.azure.com/"}])
    return response 

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    # You can specify the number of threads using the threads parameter
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000, threads=500)