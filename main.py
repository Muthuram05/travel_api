import openai
import config
import re


api_key = "sk-WOs9YNsnaqvQq3S" + "ln8kLT3BlbkFJvmXoaBHYQJ" + "OOz3w9eEjm"
openai.api_key = api_key
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
    result = []
    for i in tourist_spots:
        x = re.sub(r'\s+', '', i)
        x = x.split("-")
        if (i == ''):
            pass
        else:
            district_name = x[0]
            latitude, longitude = x[1].split(',')
            if latitude[-1] == "N" or "E":
                latitude = latitude[:6]
                longitude = longitude[:6]
            result.append([district_name,float(latitude),float(longitude)])
    print(result)
    messages.append({"role": "assistant", "content": reply})
# tell 5 tourist spot between chennai to tirunelveli(only names and tell like place name - latitude,longtitude and no need to specify E N and degree in longatitude and latitude)
#friends','family','couple','students','devotional','riding','hills stations','adventure'''
