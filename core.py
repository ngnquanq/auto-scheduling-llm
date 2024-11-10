from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage,ChatMessage, FunctionMessage,SystemMessage
from dotenv import load_dotenv
import os
import getpass

# Load environment variables
load_dotenv()
# Setup the openai api key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API")
model_name = os.getenv("OPENAI_API_MODEL")
chat = ChatOpenAI(model_name=model_name)
messages = [
    SystemMessage(content="You are a scheduling assistant who responds with structured JSON based on customer responses. You must follow some rules including: A day will start from 7AM to 5PM. Early morning is defined as 7-9 AM, Morning is defined as 9-12 AM, Afternoon is defined as 12-3 PM, Evening is defined as 3-5 PM. Do not include days where the customer has a meeting booked. Weekdays are from Friday to Sunday. However when the customer defined the specific time, use that specific time. If the customer is not available on weekends, do not include weekends in the response. When the customer not say when they are free, they just say prefer, use the prefer time"),
    HumanMessage(content="{\"customerID\": \"D0\", \"response\": \"I prefer mornings from 7am to 8pm on weekdays, and mornings on Saturday.\"}")
]
response = chat.invoke(messages)
print(response.content)
