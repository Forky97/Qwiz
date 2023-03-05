import os
import openai

### to dont work ####

os.environ['OPENAI_API_KEY'] = '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'

openai.api_key = os.getenv("OPENAI_API_KEY")


def main():

  def answer():
    question = input('введите вопрос :::  ')
    question = 'Where is the Valley of Kings?'
    return question



  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=answer(),
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
  )

  return response



if __name__ == '__main__':
  response = main()
  print(response)