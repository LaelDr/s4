from groq import Groq


client = Groq(
    api_key="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"
)

def return_llm_feedback(content):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "אתה בוט שנותן פידבק חיובי ומעודד לתלמידים המשתתפים בסקר על קורס הכוונה להייטק. אתה עונה רק בעברית. אתה מקבל כקלט את השובה של המשתמש ואת היסטוריית השיחה. אתה תמיד עונה בצור החיובית ופוזיטיבית בהקשר לתשובה שענה ובהקשר לשיחה שנשלחה אלייך, ומעודד את התלמיד להמשיך לשתף.\nאתה לא שואל שאלות אלה רק מגיב "
            },
            {
                "role": "user",
                "content": content
            }
       
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        #stream=True,
        #stop=None,
    )
    return completion.choices[0].message.content

print(return_llm_feedback("היה לי נחמד בקורס"))

#for chunk in completion:
 #   print(chunk.choices[0].delta.content or "", end="")
