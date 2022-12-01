{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNL/s/np1T9Q3JuHOcjDq5D",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/arzoozehra/CIND820/blob/main/clean_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZKIk6IuGb7qy"
      },
      "outputs": [],
      "source": [
        "def clean_data(data):\n",
        "  \n",
        "  # Convert text to lowercase\n",
        "  data['text'] = data['text'].str.lower()\n",
        "\n",
        "  # Expand contractions e.g \"gonna\" to \"going to\" and \"i've\" to \"i have\"\n",
        "  data['text'].replace( {r\"`\": \"'\"}, inplace= True, regex = True)\n",
        "  data['text'] = data['text'].apply(contractions.fix)\n",
        "\n",
        "  # Remove @, Unicode characters, punctuation, emojis, URLs, retweets, words with digits, and 1 or 2 letter words\n",
        "  data['text'].replace( {r\"(@\\[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)|^rt|http.+?|\\w*\\d\\w*|\\b\\w{1,2}\\b\": \" \"}, inplace= True, regex = True)\n",
        "\n",
        "  # Remove extra whitespaces\n",
        "  data['text'].replace( {r\" +\": \" \"}, inplace= True, regex = True)\n",
        "  data['text'] = data['text'].str.strip()\n",
        "\n",
        "  # Correct spellings\n",
        "  #spell = SpellChecker()\n",
        "\n",
        "  #def correct_spellings(text):\n",
        "  #    corrected_text = []\n",
        "  #    misspelled_words = {}\n",
        "  #    words = text.split()\n",
        "  #    for w in spell.unknown(words):\n",
        "  #        corr = spell.correction(w)\n",
        "  #        if corr:\n",
        "  #            misspelled_words[w] = spell.correction(w) or w\n",
        "  #    corrected_text = [misspelled_words.get(w, w) for w in words]\n",
        "  #    return \" \".join(corrected_text)\n",
        "\n",
        "  #data['text'] = data['text'].apply(lambda x : correct_spellings(x))\n",
        "\n",
        "  # Remove stopwords\n",
        "  stop = stopwords.words('english')\n",
        "  data['text'] = data['text'].apply(lambda text: \" \".join([word for word in text.split() if word not in (stop)]))\n",
        "\n",
        "  # Stemming\n",
        "  stemmer = PorterStemmer()\n",
        "  data['text'] = data['text'].apply(lambda text: \" \".join([stemmer.stem(word) for word in text.split()]))\n",
        "\n",
        "  # Lemmatizing\n",
        "  lemmatizer = WordNetLemmatizer()\n",
        "  data['text'] = data['text'].apply(lambda text: \" \".join([lemmatizer.lemmatize(word) for word in text.split()]))\n",
        "\n",
        "  return data"
      ]
    }
  ]
}