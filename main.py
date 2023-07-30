import openai
import config
openai.api_key = config.api_key
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

while True:
    message = input("User: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    data = reply
    if (data[0] == "1") or (data[0] == 1):
        tourist_spots = data.splitlines()
    elif (data[1] == "1") or (data[1] == 1):
        tourist_spots = data.splitlines()
    else:
        tourist_spots = data.splitlines()[1:-1]
    print(tourist_spots)
    messages.append({"role": "assistant", "content": reply})
# tell 5 tourist spot between chennai to tirunelveli(only names and tell like name - latitude,longtitude and no need to specify E N and degree in longatitu and latitude)