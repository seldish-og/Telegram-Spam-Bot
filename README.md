# Telegram-Spamer
Spam bot which can send messages at definite time. This is a working demo

DOCUMENTATION

MAIN!
TRACK PREPARATION SIGNS AND BRACKETS WHEN CHANGING JSON FILES
THIS IS VERY IMPORTANT THIS MAY STOP WORKING THE NEWSLETTER 

---WRITE TIME IN FORMS SAME AS TIME ON YOUR PC OR SERVER 
IN FORMAT: 10:5 (this is 10:05), 7:3 (this is 07:03), 21:30, etc
IF 0 IS BEFORE NUMBER THEN DELETE THIS 0 ---

The instruction to set up script on server

a) Put the folder on server.
б) Download Python 3.9 or better on server, than download requirements.txt
в) Run Message-Sender.py
г) During first run when time to send message will come you will be able to log in (in the therminal),


2) how to log in in telegram-app manager

a) go to
    https://my.telegram.org/auth
    log in here
б) than choose "API development tools"
в) in "App configuration" you can see 2 first fields:
1) App api_id: your id
2) App api_hash: your hash

г) than fill config.json with these numbers
{
  "API_ID": "your id",
  "API_HASH": "your hash"
}

---setting up forms.json---

1) open forms.json
2) I use Monday as an example
{
  (week day)
  "Monday": {

    (instead of group1_name you need to put group id. Read about Id below)
    "group1_id": [
      {

        (message1 don't change, read about it below)
        "message1": ["23:41", "type your message here"]
        (in square brackets put [time to send msg, msg text]
      }
    ],
    (next group)
    "group2_id": [
      {
        "message1": ["11:00", "type your message here"]
      }
    ]
  },


3) more about changeable parts
--- WARNING!, LOOK AFTER PUNKTUATION MARKS AND BRACKETS!! WITHOUT THEM SCRIPT WON'T WORK, CAUSE JSON FORMAT IS VERY PINCH---

а) Don't change weekdays spelling. Also don't delet them ("Monday": is always "Monday":
б) if you don't want to send message at the exact days. For example-

--no messages in monday--

(don't delete brackets and commas!)
  "Monday": {},

  "Tuesday": {
    "group1_id": [
      {
        "message1": ["23:41", "type your message here"]
      }
    ],
    "group2_id": [
      {
        "message1": ["11:00", "type your message here"]
      }
    ]
  },

в)Channel and Groups ID
to get id:
go to telegram web version https://web.telegram.org
go to channel or group u need. The addres will be like that: https://web.telegram.org/z/#-2516392083
You need to copy al numbers after # in this case it is -2516392083 (copy with minus)
and straight after minus write 100, to get -1002516392083
This is your group or channel id


г) More about the send forms
one day example again ( same as other days)
"Monday": {
    "group1_id": [
      {
        "message1": ["23:41", "type your message here"]
      }
    ],
    "group2_id": [
      {
        "message1": ["11:00", "type your message here"]
      }
    ]
    add another group
  },

1) Monday isn't changeable
2) "group1_id": change it to group ID. Example id("-516745745":)
3) "message1":, Dont change can be only one. If you want more messages to one exact group add new block (grop3_id ...)
4) ["11:00", "type your message here"] - "11:00" time, changeable. Format("hours:minutes")
    "type your message here" - message text, all you need to send, wrap in double quotes.
    
if you want more groups, just add a new same block

after "ID" two dots : open square bracket [ open curly brace {
        "message1": ["hours:minutes", "your message"] no comma or dot at the end
close square bracket ] close curly brace }

"ID": [
      {
        "message1": ["hours:minutes", "text"]
      }
    ]

--After changes save forms.json and restart Message-Sender.py --

Sorry for my english, I'm not a native speaker
If you have any questions my mail: workgeorge2@gmail.com
