import fasttext

model = fasttext.train_unsupervised('data/data.txt', model='skipgram')
print(model['test'])