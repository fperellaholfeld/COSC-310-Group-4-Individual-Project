import wolframalpha
import json

def wolframQuestion(name):
    with open('wolfram_key.json', 'r') as file: # I saved the wolfram API key in a json file so that it is not on the code itself
        cred = json.load(file) # load json
    client = wolframalpha.Client(cred['APPID']) # create wolfram client object with API key
    print("IMDBot: Sure, I'll do my best to answer whatever question you have, although I do prefer talking about movies! What would you like to know?")
    question = input(name + ': ')
    print('IMDBot: hmm let me think...')
    answer = next(client.query(question).results).text # filter the query results for only the text answer 
    print("IMDBot:", answer)
    return