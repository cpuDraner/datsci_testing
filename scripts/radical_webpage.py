import flask
import gensim
import numpy as np

website=flask.Flask('API')
#ft_model=fasttext.load_model("data\cc.en.50.bin")
gen_model=None#get from github

@website.route('/')
def heartbeat():
    return flask.jsonify({"alive":True})

@website.route('/vec')
def vec():
    input_words=flask.request.args.get('words')
    if input_words and len(input_words)>0:
        words=input_words.split('_')
        vecs=[ft_model.get_sentence_vector(word) for word in words]
        au_vector=np.mean(vecs, axis=0)


website.run(port=8000)
#fix later
