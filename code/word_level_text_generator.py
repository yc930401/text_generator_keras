import sys
import numpy
import nltk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
# load ascii text and covert to lowercase
filename = '/Workspace-Github/text_generator_keras/data/wonderland.txt'
raw_text = open(filename).read().lower()
# create mapping of unique chars to integers, and a reverse mapping
tokens = sorted(list(set(nltk.word_tokenize(raw_text))))
words = nltk.word_tokenize(raw_text)
word_to_int = dict((c, i) for i, c in enumerate(tokens))
int_to_word = dict((i, c) for i, c in enumerate(tokens))
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
# load the network weights
filename = '/Workspace-Github/text_generator_keras/data/weight_word/weights-improvement-19-5.4753.hdf5' 
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
# pick a random seed
print(len(dataX))
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print('Seed:', ' '.join([int_to_word[value] for value in pattern]))
sys.stdout.write('result: ')
# generate characters
for i in range(200):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(n_vocab)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_word[index]
    seq_in = [int_to_word[value] for value in pattern]
    sys.stdout.write(result+' ')
    pattern.append(index)
    pattern = pattern[1:len(pattern)]
print('\nDone.')
