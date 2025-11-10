import re
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize, TweetTokenizer

scene_one = "SOLDIER #1: This is the fourth sentence."

sentences = sent_tokenize(scene_one)

match = re.search("test", scene_one)

# print(match.start(), match.end())

square_pattern = r"\[.+?\]"

# print(re.search(square_pattern, scene_one))

pattern2 = r"[\w #]+:"

# print(re.search(pattern2, scene_one))

comas = "  ,   ,,"

pattern3 = r"(\s+|,)"
pattern4 = r"[\s]+|,"

# print(re.findall(pattern4, comas))

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"

pattern5 = r"(\w+|#\d|\?|\!|\:)"

# print(regexp_tokenize(my_string, pattern5))

text6 = "BBB #back sa7bi #backsa7bi #fuck this #fuck @bob @ficker"

# print(regexp_tokenize(text6, r"[#|@]\w+"))

tweets = ['This is the best #nlp exercise ive found online! #python', 
          '#NLP is super fun! <3 #learning', 
          'Thanks @datacamp :) #nlp #python']

twtoken = TweetTokenizer()

allTokens = [twtoken.tokenize(tweet) for tweet in tweets]
# print(allTokens)

germanText = "Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕"

all_words = word_tokenize(germanText)

capitalized_words = r"[A-ZÜ]\w+"

emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"

# print(regexp_tokenize(germanText ,emoji))

plt.hist([1, 2, 3, 4, 5, 6, 7, 8, 9])
# plt.show()