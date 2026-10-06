import os
from dotenv import load_dotenv
from groq import Groq

from skills.laptop import get_laptop_info

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

# SKILL CEK LAPTOP

    if pertanyaan.lower() == "cek laptop":
        info = get_laptop_info()

        print("\nNih info laptop lu:")
        print("OS:", info["os"])
        print("CPU:", info["cpu"])
        print("RAM:", info["ram_used"], "/", info["ram_total"])
        print("Storage:", info["storage_used"], "/", info["storage_total"])
        print()
        continue

# AI CHAT

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
