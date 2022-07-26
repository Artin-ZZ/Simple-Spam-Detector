#######################
# Import Dependencies #
#######################
import json







#############
# Min Class #
#############
class SpamFilter(object):
    def __init__(self, data={"wordlist":[], "spammers": [], "word_frequency": [], "blacklist_messages": []}):
        self.data = data

    def hash(self):
        return hash(str(self.data))

    def average(self, list_):
        a = 0
        for i in list_:
            a += i

            self.average_result = a / len(list_)

    def report_spam(self, message, keyword, spammer):
        self.data['wordlist'].append(keyword)
        self.data['blacklist_messages'].append(message)
        self.data['spammers'].append(spammer)
        for i in self.data['wordlist']:
            try:
                if keyword == self.data['wordlist'][i]:self.data['word_frequency'][i] += 1
            
            except:
                self.data["word_frequency"].append(1)

    def check_spam(self, text):
        text = text.replace(" ", "\n")
        texts = text.splitlines()
        a = self.data['word_frequency']

        for word in texts:
            for _ in range(len(a)):
                self.average(a)

                if a[_] > (self.average_result) * 0.9:
                    try:
                        c = self.data["wordlist"][_]
                    except IndexError:
                        break
                    if word == c:
                        return 1
                    if word == c + ".":
                        return 1
                    if word == c + "!":
                        return 1
                    if word == c + "?":
                        return 1
                    if " " + word + "." in text:
                        return 1
                    if " " + word + "!" in text:
                        return 1
                    if  word + "." in text:
                        return 1
                    if "." + word + " " in text:
                        return 1
                
                else:
                    continue
            return 0
    
    def save_filter(self):
        return json.dumps(self.data)
    
    def load_filter(self, j):
        return json.loads(j)