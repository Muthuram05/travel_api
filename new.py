from flask import Flask, request
import openai

openai.api_key = "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"
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})