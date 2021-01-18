#input: lista de strings não tratadas
# output: lista de strings não tratadas

def text_treatment(reviews=reviews):
  import nltk
  import re
  from nltk.corpus import stopwords
  nltk.download('stopwords')
  nltk.download('punkt')
  nltk.download('wordnet')
  from nltk.stem import WordNetLemmatizer 
  lem = WordNetLemmatizer() 

  reviews_split=[]
  for review in reviews:
    review=review.split()
    reviews_split.append(review)
  reviews=reviews_split

  sw=stopwords.words()
  reviews_cleaned=[]
  for review in reviews:
    words_cleaned=[]
    for word in review:
      if len(word)>2:
        if word not in sw:
          words_cleaned.append(lem.lemmatize(word).lower())
    reviews_cleaned.append(words_cleaned)
  reviews=reviews_cleaned


  reviews_cleaned=[]
  for review in reviews:
    words_cleaned=[]
    for word in review:
      word = re.sub('\.',  '',    word)
      word = re.sub('\,',  '',    word)
      word = re.sub('\/',  '',    word)
      word = re.sub('\"',  '',    word)
      words_cleaned.append(word)
    reviews_cleaned.append(words_cleaned)
  reviews=reviews_cleaned

  review_joined=[]
  separator = ' '
  for review in reviews:
    review_joined.append(separator.join(review))
  reviews=review_joined
  return(reviews)