from openai import OpenAI
import os
import json
import time 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api = os.getenv("OPENAI_API")

# Initiate client
client = OpenAI(api_key=openai_api)

# Load data
file_path = "./training_data.jsonl"
with open(file_path,"rb") as file:
    file = client.files.create(file=file, purpose='fine-tune')
print(f"Uploaded file ID: {file.id}")

# Create fine-tuning job
fine_tune = client.fine_tuning.jobs.create(model='gpt-4o-mini-2024-07-18', training_file=file.id)
print(f"Fine-tuning job ID: {fine_tune.id}")
while True:
    status = client.fine_tuning.jobs.retrieve(fine_tune.id)
    print(f"Fine-tuning status: {status.status}")
    if status.status== 'succeeded':
        print("Fine-tuning succeeded!")
        break
    elif status.status == 'failed':
        print("Fine-tuning failed.")
        break
    else:
        print("Fine-tuning in progress...")
        time.sleep(30)


