import os
import telebot
from google import genai

# Master's Credentials
TELEGRAM_TOKEN = "8443942197:AAF9tDCAcZhIIMSHZ454RLxPwsHVLzpDnwg"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PASSCODE = "Little Silent"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

authenticated_users = set()

# Master ၏ ဒုတိယဦးနှောက်အတွက် အစွမ်းထက် အရည်အချင်း (၁၂) မျိုး
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
        bot.reply_to(message, "🔐 Identity Verified. 'The Silent of Myth' အလုပ်စတင်ပါပြီ။ အရည်အချင်း (၁၂) မျိုးလုံး Master ၏ လက်ဝယ်တွင်ရှိပါသည်။")
        return

    if user_id not in authenticated_users:
        bot.reply_to(message, "⚠️ Access Denied. စကားဝှက်မှန်မှသာ ကျွန်ုပ်၏ ဦးနှောက်ကို အသုံးချနိုင်ပါမည်။")
        return

    # Processing through Gemini 2.0 Flash
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config={
                'system_instruction': SYSTEM_PROMPT,
                'tools': [{'google_search': {}}]
            },
            contents=text
        )
        bot.send_message(message.chat.id, response.text)
    except Exception as e:
        bot.reply_to(message, f"❌ စနစ်အတွင်း အမှားအယွင်း: {str(e)}")

if __name__ == "__main__":
    print("The Silent of Myth - Ultimate Sovereign Version is Running...")
    bot.infinity_polling()
