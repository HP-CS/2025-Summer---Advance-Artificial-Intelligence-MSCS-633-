from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('SimpleBot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

print("Type something to begin chatting with the bot (type 'exit' to stop)!")

    user_input = input("user: ")
    if user_input.lower() == 'exit':
        print("bot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("bot:", response)
