import json
import os.path
from json import JSONDecodeError
from datetime import datetime

knowledge = 'Knowledge_file.json'


class Agent:
    def __init__(self, name):
        self.name = name


class ChatBot(Agent):
    def __init__(self, name):
        super().__init__(name)

    def chat(self):
        def print_banner():
            banner = r"""
        ******   ******    *    *    ******
        *        *         *    *    *    *
        *****    *         ******    *    *
        *        *         *    *    *    *
        ******   ******    *    *    ******
        """
            print(banner)
        print_banner()
        print(f"{self.name} is active!")

        if not os.path.exists(knowledge):
            print(f"{knowledge} not found.\nCreating new file...")
            default_data = {"Conversation": []}
            with open(knowledge, 'w', encoding='utf-8') as file:
                json.dump(default_data, file, indent=4, ensure_ascii=False)

        try:
            with open(knowledge, 'r', encoding='utf-8') as file:
                data = json.load(file)

            if 'Conversation' not in data or not data['Conversation']:
                print(f"{self.name} notice: File conversation history is currently empty. Ready to learn!")

            while True:
                user_input = input('\nEnter a question (or type "quit"): ').strip()

                if user_input.lower() == 'quit':
                    print(f"{self.name} Exiting Bye👋👋...")
                    break
                elif user_input.lower() in ["what is the time?"]:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    print(f"{self.name}: The current local time is {current_time}.")
                    continue

                found = False

                # Looping through existing conversation
                for item in data['Conversation']:
                    if item['question'].lower() == user_input.lower():
                        print(f"{self.name}: {item['answer']}")
                        found = True
                        break

                if not found:
                    print(f"{self.name}: I do not know the answer yet.")
                    new_answer = input(f"Teach me! What is the answer to '{user_input}'?: ").strip()

                    new_entry = {
                        "question": user_input,
                        "answer": new_answer
                    }

                    data['Conversation'].append(new_entry)

                    with open(knowledge, 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)

                    print(f"{self.name}: Thank you! I have learned that.")

        except FileNotFoundError as error:
            print(f"File {knowledge} is not found because of {error}")
            return None
        except KeyboardInterrupt as error:
            print(f"Error: {error}")
            print(f"User did not enter answer to question")
            return None
        except TypeError as error:
            print(f"Error: {error}")
            return None
        except JSONDecodeError as error:
            print(f"Error: {error.msg}")
            print(f"Look up line: {error.lineno}")


bot1 = ChatBot('ECHO')
bot1.chat()
