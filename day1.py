from gtts import gTTS

sms=""
amount=""
avl_balance= ""

if "credited" in sms.lower():
    text=amount+" jama ayithu, avl_balance "+avl_balance
elif "debited" in sms.lower():
    text=amount+" karchu ayithu, avl_balance "+avl_balance

myobj= gTTS(text,lang='kn')
myobj.save("keli.mp3")