import json
import random
import openai

def load_intents():
    try:
        with open('intents.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: The 'intents.json' file is not found.")
    except json.JSONDecodeError:
        print("Error: Unable to parse 'intents.json'.")
    return None

def find_matching_intent(user_input, intents):
    for intent in intents['intents']:
        if user_input in map(str.lower, intent['patterns']):
            return random.choice(intent['responses'])
    return None

def generate_openai_response(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )

    if completion.choices[0].message is not None:
        return completion.choices[0].message
    else:
        return 'Failed to Generate response!'

def main():
    intents = load_intents()
    openai.api_key = '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'  # Replace with your OpenAI API key

    if intents:
        while True:
            user_input = input("Enter your message (or type 'exit' to quit): ").lower()

            if user_input == 'exit':
                print("Goodbye!")
                break

            response = find_matching_intent(user_input, intents)

            if response:
                print(response)
            else:
                openai_response = generate_openai_response(user_input)
                print(openai_response)

if __name__ == "__main__":
    main()