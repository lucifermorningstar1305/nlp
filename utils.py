from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import string


def tokenize(text, tokenizer):

	return tokenizer.tokenize(text)


def apostophes(text):

	if text == "n't":
		return "not"

	if text == "'ll":
		return "will"

	if text == "'re":
		return "are"

	if text == "'s":
		return "is"

	if text == "'m":
		return "am"

	if text == "'ve":
		return "have"

	else:
		return text


def deal_with_few_tokens(text):

	if text == "mr.":
		return "mister"

	if text == "mrs.":
		return "mistress"

	if text == "ms.":
		return "miss"

	if text == "br":
		return ""

	if text == "dr.":
		return "doctor"

	if text == "jr.":
		return "junior"

	if text == "hon.":
		return "honourable"

	if text == "prof.":
		return "professor"

	if text == "rev.":
		return "reverend"

	if text == "sr.":
		return "senior"

	if text == "st.":
		return "saint"

	else:
		return text



def preprocess(data, lemmatize=False, stem=False):
	"""
	-------------------------------------------------
	Description : Function to preprocess text data

	Parameters:
	@param data -- a python list containing text data
	@param lemmatize -- a bool function to ensure lemmatization (default=False)
	@param stem -- a bool function to ensure stemming (default=False)

	Return:
	@ret preprocessed_string -- a python list containing the preprocessed strings
	--------------------------------------------------------
	"""

	stemmer = None
	lemmatizer = None
	preprocessed_data = []

	if stem:
		stemmer = PorterStemmer()

	if lemmatize:
		lemmatizer = WordNetLemmatizer()

	tokenizer = TreebankWordTokenizer()
	STOPWORDS = set(stopwords.words('english'))

	for text in data:

		# Lower case the text
		text = text.lower()

		# Replace hyperlinks if any
		text = re.sub(r"http\S+", r"", text)

		# Tokenize the data
		tokenized_data = tokenize(text, tokenizer)

		# Replace apostophes
		tokenized_data = [apostophes(i) for i in tokenized_data]

		# Remove stopwords
		tokenized_data = [i for i in tokenized_data if i not in STOPWORDS]

		#Remove punctuations
		tokenized_data = ["" if i in string.punctuation else i for i in tokenized_data]

		# Deal with a few texts
		tokenized_data = [deal_with_few_tokens(i) for i in tokenized_data]

		if lemmatize:
			tokenized_data = [lemmatizer.lemmatize(i) for i in tokenized_data]

		if stem:
			tokenized_data = [stemmer.stem(i) for i in tokenized_data]

		new_text = " ".join(tokenized_data)
		preprocessed_data.append(new_text)


	return preprocessed_data




