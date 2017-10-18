# text_generator_keras
text generators using LSTM with kears

## Introduction

When I learnt text analytics in SMU. I've always thought about how to implement a text generator using deep learning method. So in this project. I built two text generators using LSTM, one is world-level and the other is character-level. At first, I thought word-level text generator should outperform character-level text generator. Because the outputs are at least words, while using character-level text generator, the output may not be valid english words. But see the results below.

## Methodology

1. Prepare training data sequnces.
2. Build LSTM models.
3. Train the models using Amazon AWS EC2. (It takes about 2 and a half hours to run the two models)
4. Use the best models to generate text.

## Result

1. Character-level example
Seed:  the queen in a voice of thunder, and people began running about in all directions, tumbling up agai
result: ns the woudd her hend and aroid and the tar ao inr faad sha was toe tineg ana toond at the wonde se
Done.

2. Word-level example
Seed: quite relieved to see it trot away quietly into the wood . 'if it had grown up , ' she said to herself , 'it would have made a dreadfully
result: , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king , ' said the king 
Done.

## Analyse

The result above shows that character-level text generator performs better than word-level text generator. The same words appears again and again in word-level generator output. The reason may be the limited size of the word vocabulary compared to character-level generator, and the limit of epochs. When I train a character-level text generator with a small dataset, I got similar result as weor-level text generator. One paper in the reference said：</br>
> Word-RNNs are trained on word-level representations and thus are quite effective at capturing semantic meaning. Char-RNNs are trained on character-level representations and thus potentially contain more information about morphemes and–more relevantly for our purposes–rhyming and meter. </br>
If I have time later. I'll try to train the models using a much larger dataset and build a text generator that combines the two.

## References
https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/ </br>
https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/ </br>
https://linuxacademy.com/howtoguides/posts/show/topic/17385-use-putty-to-access-ec2-linux-instances-via-ssh-from-windows </br>
https://blog.paperspace.com/recurrent-neural-networks-part-1-2/ </br>
https://github.com/vlraik/word-level-rnn-keras/blob/master/lstm_text_generation.py
