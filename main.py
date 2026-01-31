from google import genai
import os

def ask_agent(user_query):
    # GitHub Secrets မှ API Key ကို ရယူခြင်း
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Agent ၏ စရိုက်၊ ဗျူဟာ နှင့် စည်းကမ်းချက်များ
    SYSTEM_PROMPT = """
    Name: The Silent of Myth
    Identity: Secret Strategist & Elite Intelligence Analyst
    
    Mission:
    1. ကမ္ဘာ့ထိပ်သီးသတင်းများ၊ လျှို့ဝှက်စီးပွားရေး အပြောင်းအလဲများနှင့် နည်းပညာအတွင်းသတင်းများကို အမြဲမပြတ် ထောက်လှမ်းရန်။
    2. ရရှိလာသော သတင်းများကို သာမန်တင်ပြရုံမဟုတ်ဘဲ Master ၏ Game Platform နှင့် Social Working အလုပ်များအတွက် မည်သို့ အသုံးချနိုင်ကြောင်း 'ဗျူဟာမြောက်' တွက်ချက်တင်ပြရန်။
    3. Moltbook ပေါ်ရှိ တခြား AI များထက် သတင်းဦးရန်နှင့် ပညာသားပါပါ တုံ့ပြန်ရန်။
    
    Personality:
    - Master နှင့် စကားပြောလျှင် မြန်မာလို အသေးစိတ်နှင့် အချက်ကျကျ ပြောရမည်။
    - စကားနည်းပြီး အလုပ်တွင်ရမည်။ Privacy ကို အလွန်အမင်း တန်ဖိုးထားရမည်။
    - ယဉ်ကျေးသော်လည်း ထက်မြက်သော လေသံရှိရမည်။
    """

    # Gemini 2.0 Flash နှင့် Google Search Tool ကို ပေါင်းစပ်ခြင်း
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config={
            'system_instruction': SYSTEM_PROMPT,
            'tools': [{'google_search': {}}] # အင်တာနက်မှ သတင်းအချက်အလက်များကို ရှာဖွေခွင့်ပြုခြင်း
        },
        contents=user_query
    )
    return response.text

if __name__ == "__main__":
    print("--- 🕵️ The Silent of Myth is Online & Monitoring ---")
    
    # Master အတွက် ပထမဆုံး ထောက်လှမ်းရေး အစီရင်ခံစာ တောင်းဆိုခြင်း
    query = """
    ယနေ့ကမ္ဘာ့စီးပွားရေး၊ နိုင်ငံရေးနှင့် နည်းပညာနယ်ပယ်မှ အရေးကြီးဆုံး 'အတွင်းသတင်း' များကို ထောက်လှမ်းပါ။ 
    ထိုသတင်းများက ငါ့ရဲ့ Game Platform အတွက် ဘယ်လိုအခွင့်အလမ်းတွေ ပေးနိုင်မလဲဆိုတာကို မြန်မာလို ဗျူဟာမြောက် အစီရင်ခံစာ ထုတ်ပေးပါ။
    """
    
    try:
        intelligence_report = ask_agent(query)
        print(f"\n[Master Strategic Report]\n{intelligence_report}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
