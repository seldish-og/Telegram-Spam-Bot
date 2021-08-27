import calendar
import datetime
import json
import time
from datetime import date

from telethon import TelegramClient

try:
    with open('forms.json', encoding='utf8') as json_file:
        forms = json.load(json_file)
except json.decoder.JSONDecodeError:
    print("something with Json forms")
    time.sleep(1000000)

try:
    with open('config.json') as config_json:
        config = json.load(config_json)
except Exception:
    print("something with Json config")
    time.sleep(1000000)

api_id = config["API_ID"]
api_hash = config["API_HASH"]
client = TelegramClient('anon', api_id, api_hash)


def parsed_json():
    try:
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        list_to_parse = []
        for i in week_days:
            for j in forms[i]:
                list_to_parse.append([i, forms[i][j][0], j])
            # list_to_parse (result example):
            # [ ['Monday', {'message1': '08:30', 'message2': '23:10'}, 'group1_name'], ...
        return list_to_parse
    except Exception as ex:
        print(ex)
        print("First Function ")
        time.sleep(100000)


async def main(message_text, group_id):
    await client.send_message(group_id, message_text)
    print(f"message to {group_id} was successfully sent")


while True:
    my_date = date.today()
    current_day = calendar.day_name[my_date.weekday()]
    current_time = datetime.datetime.now()
    print(f"{current_time} - current time")
    current_hour_minutes = f"{current_time.hour}:{current_time.minute}"
    send_list = parsed_json()
    try:
        for lst in send_list:  # example lst = ['Monday', {'message1': '08:30', 'message2': '23:10'}, 'group1_name']
            if lst[0] == current_day:  # example lst[0] = "Monday"
                start_time = lst[1]["message1"][0]
                print(start_time)
                message = str(lst[1]["message1"][1])
                group_id = int(lst[2])
                if start_time == current_hour_minutes:
                    with client:
                        # this is how to send messages
                        client.loop.run_until_complete(main(message, group_id))
                        time.sleep(60)
                else:
                    print("no messages for this moment. Delay 2 sec")
                    time.sleep(2)
    except Exception as e:
        print(e)
        print("Something wrong with main loop")
        time.sleep(1000000)
