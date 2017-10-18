import numpy
import nltk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
# load text and covert to lowercase
filename = '/home/ec2-user/text_generator_keras/data/wonderland.txt'
raw_text = open(filename).read().lower()
# create mapping of unique chars to integers
tokens = sorted(list(set(nltk.word_tokenize(raw_text))))
words = nltk.word_tokenize(raw_text)
word_to_int = dict((c, i) for i, c in enumerate(tokens))
# summarize the loaded data
n_words = len(words)
n_vocab = len(tokens)
print('Total Characters: ', n_words)
print('Total Vocabulary: ', n_vocab)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 30
dataX = []
dataY = []
for i in range(0, n_words - seq_length, 1):
    seq_in = words[i:i + seq_length]
    seq_out = words[i + seq_length]
    dataX.append([word_to_int[char] for char in seq_in])
    dataY.append(word_to_int[seq_out])
n_patterns = len(dataX)
print('Total Patterns: ', n_patterns)
# reshape X to be [samples, time steps, features]
x = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
x = x / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(512, input_shape=(x.shape[1], x.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(512, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
# define the checkpoint
filepath = 'weights-improvement-{epoch:02d}-{loss:.4f}.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(x, y, epochs=20, batch_size=128, callbacks=callbacks_list)
