import re
!pip install contractions
import contractions
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


def clean_data(data):
  
  # Convert text to lowercase
  data['text'] = data['text'].str.lower()

  # Expand contractions e.g "gonna" to "going to" and "i've" to "i have"
  data['text'].replace( {r"`": "'"}, inplace= True, regex = True)
  data['text'] = data['text'].apply(contractions.fix)

  # Remove @, Unicode characters, punctuation, emojis, URLs, retweets, words with digits, and 1 or 2 letter words
  data['text'].replace( {r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?|\w*\d\w*|\b\w{1,2}\b": " "}, inplace= True, regex = True)

  # Remove extra whitespaces
  data['text'].replace( {r" +": " "}, inplace= True, regex = True)
  data['text'] = data['text'].str.strip()

  # Correct spellings
  #spell = SpellChecker()

  #def correct_spellings(text):
  #    corrected_text = []
  #    misspelled_words = {}
  #    words = text.split()
  #    for w in spell.unknown(words):
  #        corr = spell.correction(w)
  #        if corr:
  #            misspelled_words[w] = spell.correction(w) or w
  #    corrected_text = [misspelled_words.get(w, w) for w in words]
  #    return " ".join(corrected_text)

  #data['text'] = data['text'].apply(lambda x : correct_spellings(x))

  # Remove stopwords
  stop = stopwords.words('english')
  data['text'] = data['text'].apply(lambda text: " ".join([word for word in text.split() if word not in (stop)]))

  # Stemming
  stemmer = PorterStemmer()
  data['text'] = data['text'].apply(lambda text: " ".join([stemmer.stem(word) for word in text.split()]))

  # Lemmatizing
  lemmatizer = WordNetLemmatizer()
  data['text'] = data['text'].apply(lambda text: " ".join([lemmatizer.lemmatize(word) for word in text.split()]))

  return data
