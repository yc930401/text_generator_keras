# text_generator_keras
text generators using LSTM with keras

## Introduction

When I learnt text analytics, I've always thought about how to implement a text generator using deep learning method. So in this project. I built two text generators using LSTM, one is world-level and the other is character-level. At first, I thought word-level text generator should outperform character-level text generator. Because the outputs are at least words, while using character-level text generator, the output may not be valid english words. But the result of character-level text generator is quit good.

## Methodology

1. Prepare training data sequnces.
2. Build 2 layer LSTM models. (Note: the return_sequence in the first lstm layer should be set to True. See the reason in the last reference link.) </br>
![LSTM](/data/LSTM.png)
3. Train the models using Tesla P100-SXM2 gpu (character-level text generator takes about 3 to 4 hours, and word level takes about 1 hour).
4. Use the best models to generate text given random seed.
* Here I only upload the best model, because the files are too large. 100 models for word-level and 30 models for character-level.

## Result

1. Character-level example </br>
* Seed: n!' for the mouse was swimming
away from her as hard as it could go, and making quite a commotion in
* Result:  the way of execution the window, and said in a vhile to stenble the toot. alice cid not like the look of the court, and said to the kury as he spoke, and she was quite surprised to be then they lake out that the was now that they were littening about in the mittle golden key and she was qoeaking about it out of the wood, and the poor little thing sabbit hoterrupted to see what she was now about the courte, and the whole party sereat of the courte, and said to the kury and the cook and the moment all the while, and looking at the moment she was now that they were nying down and looked at the was jo the words: 'when the mock turtle shgned to be a long tide of the lobk turtle, and said to the knry, and the queen said so the went on, 'what a curious pincering in the ban!' and she wanted uith tome time and stiekly and ttoping the soom. and the white rabbit read out of the wasted on the blok, and the white rabbit read out of the wasted on the blok, and the white rabbit read out of the wast
Done.

2. Word-level example </br>
* Seed: when they saw alice coming . 'there 's plenty of room ! ' said alice indignantly , and she sat down in a large arm-chair at one end of the
* Result: back . the time ? ' 'i quite have the see ? ' the the king , with to alice again as looking , the was 's great out . an all the rabbit her the end a a in is her to away in as in time , 'i must next to , ' alice said to herself , who had been into out this the bottle out , but it -- him as round . when the . ) queer for , bit then had all moment in two , he looked . and if tried , , 'what it all ! ' , the 's ' the gryphon went after the 's with way . to first thing his . who up nothing by upon were other when , . the not had thing to be them , for last him , all when was arm her thought about with she other side eyes the out out a how , she there , ) why enough the off of into out , and . * was came was much its , ' alice eat know mean up . '' she he the herself , 'it 'm sure 
Done.

## Analyse

The result above shows that character-level text generator performs better than word-level text generator. The quantitative result can be measured by perplexity score. which is e to the power of loss. The loss of the two models are 1.0522 for character-level (the minimum loss with epoch = 16) and 2.1040 for word-level(the minimum loss with epoch = 99). This measurement is mentioned in the tensorflow tutorial - Recurrent Neural Networks. 
The word-level text generator is a very naive model, because I do not consider sentence level but only the single word, and I do not perform vectorization to transform a word integer to a one-hot vector.  
One paper in the reference said：</br>
> Word-RNNs are trained on word-level representations and thus are quite effective at capturing semantic meaning. Char-RNNs are trained on character-level representations and thus potentially contain more information about morphemes and–more relevantly for our purposes–rhyming and meter. </br>

## Future work

1. Try to use word embedding (e.g. embedding layer in keras) instead of map each char to a int index.
2. Combine character-level and word-level text generator to get a better model.

## References
https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/ </br>
https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/ </br>
https://linuxacademy.com/howtoguides/posts/show/topic/17385-use-putty-to-access-ec2-linux-instances-via-ssh-from-windows </br>
https://blog.paperspace.com/recurrent-neural-networks-part-1-2/ </br>
https://github.com/vlraik/word-level-rnn-keras/blob/master/lstm_text_generation.py </br>
https://www.tensorflow.org/tutorials/recurrent </br>
https://stackoverflow.com/questions/42755820/how-to-use-return-sequences-option-and-timedistributed-layer-in-keras
