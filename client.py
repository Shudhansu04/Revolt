from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)