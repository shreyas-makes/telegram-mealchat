
# This code works
from openai import OpenAI

client = OpenAI(api_key='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')

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages= [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image url", 
                 "image_url": "https://placekitten.com/300/400"}
                        ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])