from openai import OpenAI


import os
def main():
    
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        reasoning_effort="low",
        messages=[
            {   "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Explain to me how AI works"
            }
        ]
    )

    print(response.choices[0].message)from openai import OpenAI

    client = OpenAI(
        api_key="GEMINI_API_KEY",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        reasoning_effort="low",
        messages=[
            {   "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Explain to me how AI works"
            }
        ]
    )

    print(response.choices[0].message)

if __name__ == "__main__":
    main()
