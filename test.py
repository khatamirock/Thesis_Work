from keras.preprocessing.sequence import pad_sequences


def padder_enc(inp):
  decoder_input_sequences = pad_sequences(inp, maxlen=5, padding='post')
  print('decoder_inputs_sequences shape:', decoder_input_sequences.shape)
  return decoder_input_sequences

import numpy as np


def decode_sequence(input_sentence):
    # tokenized_input_sentence = source_vectorization([input_sentence])
    decoded_sentence = 1
    for i in range(20):
        tokenized_target_sentence = [decoded_sentence]


        # next_token_predictions = seq2seq_rnn.predict(
        #     [tokenized_input_sentence, tokenized_target_sentence])
        
        # sampled_token_index = np.argmax(next_token_predictions[0, i, :])

        decoded_sentence += " " + sampled_token
        if sampled_token == "[end]":
            break
    return decoded_sentence

test_eng_texts = [1,12,4,0,0]


decode_sequence(test_eng_texts)
