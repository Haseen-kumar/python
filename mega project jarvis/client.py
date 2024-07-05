from openai import OpenAI 
client=OpenAI(
    api_key="sk-proj-EZ41WkBgPJ2l7Ief88l8T3BlbkFJ1X6EAHPT1bD6TLNMR7Yc",
)




completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtaul assistant name jarvis, skilled in explaining the task like alexa and google."},
    {"role": "user", "content": "what is coding."}
  ]
)

print(completion.choices[0].message)