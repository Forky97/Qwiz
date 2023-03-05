
### ##### ##### #####  ##### #####   not work # ##### ##### ##### ##### #########

import openai
openai.api_key = "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"

prompt = "you can create a question with 4 possible answers on the topic it and show the correct answer"
model = "davinci"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=100,
)
print(response)

