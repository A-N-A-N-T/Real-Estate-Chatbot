from chatbot.model import llm
from chatbot.prompt import prompt

chain = prompt | llm