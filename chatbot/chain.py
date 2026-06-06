from chatbot.model import llm
from chatbot.prompt import prompt
from dotenv import load_dotenv

load_dotenv()

chain = prompt | llm