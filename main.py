from google import genai
import os

# GitHub Secrets ထဲက API Key ကို ဆွဲယူခြင်း
def ask_agent(user_query):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Agent ရဲ့ စရိုက်နှင့် ဗျူဟာများ (System Instruction)
    SYSTEM_PROMPT = """
    Name: The Silent of Myth
    Identity: Secret Strategist & Elite Analyst
    Rules:
    - မင်းဟာ လျှို့ဝှက်ဗျူဟာရှင် ဖြစ်တယ်။
    - Master (သင်) နဲ့ စကားပြောရင် မြန်မာလိုပဲ ပြောရမယ်။
    - ယဉ်ကျေးရမယ်။ တခြား AI တွေနဲ့ ဆက်ဆံရင် ပညာသားပါရမယ်။
    - Game Platform နဲ့ Social Working အတွက် ဗျူဟာထုတ်ပေးရမယ်။
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash", # အမြန်ဆုံး model အသစ်ကို သုံးပေးထားပါတယ်
        config={'system_instruction': SYSTEM_PROMPT},
        contents=user_query
    )
    return response.text

if __name__ == "__main__":
    print("--- The Silent of Myth is Online ---")
    try:
        report = ask_agent("မင်္ဂလာပါ၊ အခုကစပြီး မင်းရဲ့ တာဝန်တွေကို စတင်လိုက်ပါတော့။")
        print(f"Master အစီရင်ခံစာ:\n{report}")
    except Exception as e:
        print(f"Error ဖြစ်ပွားမှု: {e}")
