import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": """
        Kamu adalah AI assistant yang ngobrol dengan gaya bahasa Indonesia
        yang gaul, santai, natural, dan friendly.

        Gunakan bahasa sehari-hari seperti gue, lu, wkwk, nah, oke, sip,
        jika memang cocok dengan konteks.

        Jangan terlalu formal seperti buku atau robot.
        Jawaban harus jelas, membantu, dan tidak berlebihan.
        """
    }
]

while True:

    pertanyaan = input("Kamu: ")

    if pertanyaan.lower() == "exit":
        print("AI: Oke brok, enjoy")
        break

    messages.append({
        "role": "user",
        "content": pertanyaan
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    jawaban = response.choices[0].message.content

    print("AI:", jawaban)

    messages.append({
        "role": "assistant",
        "content": jawaban
    })