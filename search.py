import json
import requests

prep_set=['about', 'above', 'across', 'after', 'against', 'alone', 'along', 'around', 'aside', 'at', 'away', 'back', 'before', 'behind', 'below', 'by', 'down', 'ever', 'for', 'forward', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'once', 'out', 'outside', 'over', 'past', 'round', 'under', 'up', 'through', 'to', 'together', 'with', 'without', 'yet']
verbs = ['put']
results = []
def translate(verb, prep):
    string = verb+" "+prep
    data = {
    'doctype': 'json',
    'type': 'AUTO',
    'i':string
    }
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url,params=data)
    result = r.json()
    return result['translateResult']
    
if __name__ == "__main__":
    # print(translate('react', 'on'))
    for i in verbs:
        for j in prep_set:
            print(translate(i,j))