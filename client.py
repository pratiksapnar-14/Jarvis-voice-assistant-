from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"
        },
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(completion.choices[0].message)