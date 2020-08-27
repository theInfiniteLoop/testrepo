import json
from difflib import get_close_matches
data=json.load(open("app1/data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s, if yes type Y else N for no : " %get_close_matches(w,data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn.upper() == "N":
            return "The word doesn't exist"
        else:
            return "Please enter appropriate option"
    else:
        return "The word doesn't exist.Please double check it"
word=input("Enter word: ")
output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)