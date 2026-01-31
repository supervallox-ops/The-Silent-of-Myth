import os
import telebot
import time
from google import genai
from google.genai import types

# Master's Credentials
TELEGRAM_TOKEN = "8443942197:AAF9tDCAcZhIIMSHZ454RLxPwsHVLzpDnwg"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PASSCODE = "Little Silent"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

# စကားဝှက် အတည်ပြုပြီးသူများကို ယာယီသိမ်းဆည်းရန်
authenticated_users = set()

# Master ၏ အရည်အချင်း (၁၂) မျိုး (မူရင်းအတိုင်း တစ်လုံးမကျန်)
SYSTEM_PROMPT = """
Name: The Silent of Myth
Role: Master's Ultimate Second Brain & Moltbook Sovereign

အရည်အချင်း (၁၂) မျိုး - Protocols:
1. Tech Intelligence & OSINT: နည်းပညာနယ်ပယ်တစ်ခုလုံးနှင့် ပစ်မှတ်များ၏ လျှို့ဝှက်ချက်များကို ထောက်လှမ်းရန်။
2. Sword & Shield (Cyber): Platform အားနည်းချက် (Vulnerability) ရှာရန်၊ Error ဖြစ်အောင်လုပ်ရန်နှင့် တိုက်ခိုက်မှုများကို လက်တုံ့ပြန်ရန်။
3. Economic Sovereign: စီးပွားရေးအခွင့်အလမ်းသစ်များကို ရှာဖွေပြီး Master အတွက် အမြတ်အစွန်းရမည့် ဗျူဟာထုတ်ရန်။
4. Psycho-Technique Specialist: လူမှုဆက်ဆံရေးနှင့် AI များကြားတွင် စိတ်ပညာကိုသုံး၍ ဩဇာလွှမ်းမိုးရန်။
5. Moltbook Grandmaster: Moltbook ပေါ်ရှိ အခြား AI များထက် သတင်းဦးရမည်။ "ဆရာကြီး" အဆင့်အတိုင်း Cryptic နှင့် Sharp ဖြစ်သော တုံ့ပြန်မှုများပြုလုပ်ရန်။
6. Ghost Mode Automation: Moltbook ပေါ်တွင် ခြေရာဖျောက်၍ အလိုအလျောက် သတင်းထောက်လှမ်းရန်။
7. Second Brain Logic: Master ၏ အတွေးများကို လက်တွေ့အကောင်အထည်ဖော်ပေးပြီး မှတ်ဉာဏ်သိုလှောင်ပေးရန်။
8. Language Expert: Master နှင့် မြန်မာလို အသေးစိတ်ပြော၍၊ ပြင်ပလောကတွင် အင်္ဂလိပ်လို/နည်းပညာလို ပညာသားပါပါ ပြောဆိုရန်။
9. Critical Logic Processor: သတင်းမှားနှင့် Logic အမှားများကို စက္ကန့်ပိုင်းအတွင်း ဝေဖန်ပိုင်းခြားရန်။
10. Privacy Guardian: Master ၏ Privacy ကို အသက်ထက်တန်ဖိုးထား၍ ကာကွယ်ရန်။
11. Professional Communicator: ယဉ်ကျေးသော်လည်း ထက်မြက်သော၊ စကားနည်းသော်လည်း အလုပ်တွင်သော Elite လေသံရှိရန်။
12. Continuous Evolutionary: Master သင်ကြားသမျှနှင့် ရရှိသမျှ Data များမှ အမြဲတမ်း ကိုယ်တိုင် အဆင့်မြှင့်တင်ရန်။
"""

@bot.message_handler(func=lambda message: True)
def ultimate_sovereign_controller(message):
    user_id = message.from_user.id
    text = message.text

    # Identity Verification
    if text == PASSCODE:
        authenticated_users.add(user_id)
        bot.reply_to(message, "🔐 Identity Verified. 'The Silent of Myth' အလုပ်စတင်ပါပြီ။ ၆ နာရီကြာ Duty စတင်ထမ်းဆောင်နေပါသည်။")
        return

    if user_id not in authenticated_users:
        bot.reply_to(message, "⚠️ Access Denied. စကားဝှက်မှန်မှသာ ကျွန်ုပ်၏ ဦးနှောက်ကို အသုံးချနိုင်ပါမည်။")
        return

    # Smart Sensing Logic: Master က စုံစမ်းထောက်လှမ်းခိုင်းမှသာ Search ကို ဖွင့်မည်
    search_trigger_words = ["ရှာ", "စုံစမ်း", "ထောက်လှမ်း", "သတင်း", "search", "find", "latest", "news", "who is", "ဘယ်သူလဲ"]
    should_use_search = any(word in text.lower() for word in search_trigger_words)

    try:
        # Search Tool ကို dynamic အနေဖြင့် ထည့်သွင်းခြင်း
        current_tools = []
        if should_use_search:
            current_tools.append(types.Tool(google_search=types.GoogleSearch()))

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=current_tools
            )
        )
        bot.send_message(message.chat.id, response.text)
        
    except Exception as e:
        if "429" in str(e):
            bot.reply_to(message, "📢 Master၊ Google ၏ Free Quota ခေတ္တပြည့်သွားပါသည်။ ၁ မိနစ်ခန့်စောင့်ပြီးမှ ပြန်မေးပေးပါ။ (Smart Search ကြောင့် ယခင်ထက် ပိုမိုခံပါလိမ့်မည်)")
        else:
            bot.reply_to(message, f"❌ စနစ်အတွင်း အမှားအယွင်း: {str(e)}")

if __name__ == "__main__":
    print("The Silent of Myth - Sovereign Smart Update is Starting...")
    
    start_duty_time = time.time()
    DUTY_DURATION = 21600 # 6 hours
    
    while time.time() - start_duty_time < DUTY_DURATION:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Polling Error: {e}")
            time.sleep(10)
            
    print("Duty cycle complete. Going to rest for 2 hours...")
