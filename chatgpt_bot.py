import openai
import logging

prompts = []

class ChatGPTBot:
    #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
    def __init__(self, api_key):
        """
        Initializes the ChatGPTBot API with the provided OpenAI API key.
        """
        openai.api_key = api_key


    def create_prompt(self, prompt):
        """
        Takes a user-provided prompt as input and stores it for later interactions with the ChatGPT bot.
        """
        prompts.append(prompt)
        

    def get_response(self, prompt_index):
        """
        Takes the index of a previously stored prompt and returns the ChatGPT bot's response to that prompt.
        """
        if prompt_index < 0 or prompt_index >= len(prompts):
            return "Invalid prompt index."
        
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompts[prompt_index],
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None,
        )
        
        return response.choices[0].text.strip()

    def update_prompt(self, prompt_index, new_prompt):
        """
        Updates an existing prompt at the given index with a new prompt provided by the user.
        """
        if prompt_index < 0 or prompt_index >= len(prompts):
            return "Invalid prompt index."
    
        prompts[prompt_index] = new_prompt
        
        return prompts
