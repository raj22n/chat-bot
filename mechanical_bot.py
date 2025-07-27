import openai

openai.api_key = "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"
openai.base_url = "https://api.groq.com/openai/v1"

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = openai.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a mechanical bot. Provide answers only related to mechanical engineering ,donot give answers to any question outside this domain."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)
