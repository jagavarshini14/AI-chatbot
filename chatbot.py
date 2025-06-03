import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello! How can I help you?", "Hey there!"]],
    ["what is your name?", ["I'm a chatbot built by Varsh."]],
    ["how are you?", ["I'm just code, but I'm doing fine!"]],
    ["bye", ["Goodbye! Have a nice day."]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()