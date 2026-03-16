import nltk
import spacy
class NounParser:
    def __init__(self):
        self.nlp=spacy.load("en_core_web_sm")

    def break_sentences(txt: str)->list[str]:
        """
        break text into a list of sentences
        """
        return nltk.tokenize.sent_tokenize(txt)

    print(break_sentences("break sentences breaks sentences. see? it works like so."))

    def phrases(self,txt:str)->list[str]: #NOTE: fixed in class, modify later
        """
        Convert text into nounphrases
        """
        doc = self.nlp(txt.lower())
        return list(doc.noun_chunks)

np=NounParser()
print(np.phrases("Our Market Research Shows That Players Like Really Long Card Names, So We Made this Card to Have the Absolute Longest Card Name Ever Elemental"))