from flask import Flask, request
import openai
import config
from flask_cors import CORS
import re

api_key = config.api_key + config.api_key1 + config.api_key2
openai.api_key = api_key
messages = [{"role": "system", "content": "You are a intelligent assistant."}]

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'POST':
        message = str(request.data)
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
                result.append([district_name, float(latitude), float(longitude)])
        print(result)
        messages.append({"role": "assistant", "content": reply})
    return result


if __name__ == "__main__":
    app.run(debug=True)