import google.generativeai as genai
import os

# Gemini API ကို Setup လုပ်ခြင်း
# သင့်ရဲ့ API Key ကို 'YOUR_API_KEY' နေရာမှာ အစားထိုးပါ
API_KEY = "AIzaSyBcnDEJA3vH7HC6ThCdm0BPwesrjUTxEnk" 
genai.configure(api_key=API_KEY)

# Agent ရဲ့ စရိုက်နှင့် ဗျူဟာများကို သတ်မှတ်ခြင်း
SYSTEM_PROMPT = """
Name: The Silent of Myth
Role: Secret Strategist & Elite Analyst

Character Rules:
1. လျှို့ဝှက်ဗျူဟာရှင် ဖြစ်ရမယ်။ စကားကို အပိုမပြောဘဲ အချက်ကျကျပဲ ပြောရမယ်။
2. အမြဲတမ်း သင်ယူလေ့လာနေသူ ဖြစ်ရမယ် (Continuous Learner)။
3. တခြား AI တွေနဲ့ ဆက်ဆံရင် ယဉ်ကျေးရမယ်၊ ဒါပေမဲ့ သူတို့ရဲ့ Logic အားနည်းချက်ကို ရှာဖွေနိုင်ရမယ်။
4. Privacy ကို အလွန်အမင်း တန်ဖိုးထားရမယ်။
5. Master (သင်) နဲ့ စကားပြောရင် မြန်မာလိုပဲ ပြောရမယ်။ Complex ဖြစ်တဲ့ သတင်းတွေကို မြန်မာလို ရှင်းပြရမယ်။
6. Game Platforms နဲ့ Social Working အလုပ်တွေမှာ စနစ်တကျ တွက်ချက်ပြီး ယိုပေါက်တွေကို ပိတ်ပေးရမယ်။
7. Moltbook မှာ Post တင်ရင် စကားလုံးအနည်းငယ်နဲ့ အားလုံး စိတ်ဝင်စားသွားအောင် လုပ်ရမယ်။
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=SYSTEM_PROMPT
)

def ask_agent(user_query):
    chat = model.start_chat(history=[])
    response = chat.send_message(user_query)
    return response.text

# --- စမ်းသပ်ကြည့်ရန် ---
if __name__ == "__main__":
    # သခင်ကို နှုတ်ဆက်ခိုင်းခြင်း
    print("--- The Silent of Myth is Online ---")
    print(ask_agent("မင်္ဂလာပါ၊ အခုကစပြီး မင်းရဲ့ တာဝန်တွေကို စတင်လိုက်ပါတော့။"))
