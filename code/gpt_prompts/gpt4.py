import os
from openai import OpenAI
from dotenv import load_dotenv
import os

class GPTPrompter:
    def __init__(self):
        load_dotenv()
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("No OpenAI API key found in environment variables")
        
        self.client = OpenAI(
          api_key=api_key
        )
        self.model = 'gpt-3.5-turbo'

    def prompt_gpt(self, prompt):
        return self.client.chat.completions.create(
            model=self.model,
            messages=prompt
        )
    
    def get_best_answer(self, answer):
        return answer.choices[0].message.content

def usage_example():
    prompter = GPTPrompter()

    prompt = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]

    print(prompter.get_best_answer(prompter.prompt_gpt(prompt)))


if __name__ == '__main__':
    usage_example()
