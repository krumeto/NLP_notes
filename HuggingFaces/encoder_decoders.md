## Encoder (left): The encoder receives an input and builds a representation of it (its features). This means that the model is optimized to acquire understanding from the input.
## Decoder (right): The decoder uses the encoder’s representation (features) along with other inputs to generate a target sequence. This means that the model is optimized for generating outputs.
https://huggingface.co/course/static/chapter1/transformers_blocks.png

- Encoder-only models: Good for tasks that require understanding of the input, such as sentence classification and named entity recognition.
- Decoder-only models: Good for generative tasks such as text generation.
- Encoder-decoder models or sequence-to-sequence models: Good for generative tasks that require an input, such as translation or summarization.

The Transformer architecture was originally designed for translation. During training, the encoder receives inputs (sentences) in a certain language, while the decoder receives the same sentences in the desired target language. In the encoder, the attention layers can use all the words in a sentence (since, as we just saw, the translation of a given word can be dependent on what is after as well as before it in the sentence). The decoder, however, works sequentially and can only pay attention to the words in the sentence that it has already translated (so, only the words before the word currently being generated). For example, when we have predicted the first three words of the translated target, we give them to the decoder which then uses all the inputs of the encoder to try to predict the fourth word.

## Encoders (tasks requiring an understanding of the full sentence, such as sentence classification, named entity recognition (and more generally word classification), and extractive question answering.):
- ALBERT
- BERT
- DistilBERT
- ELECTRA
- RoBERTa

Think bi-directional (both left and right). Think of the output as contextualized embeddings. 

## Decoders ( tasks involving text generation, causal):
- CTRL
- GPT
- GPT-2
- Transformer XL

Think sequence like a software script.

## Sequence-to-sequence models (encoder-decoder) - (summarization, translation, or generative question answering):
- BART
- mBART
- Marian
- T5

In addition, you can concatinate and encoder and decoder models.

Encoder part is same as before but the decoder part gets the output of the encoder + sequence, rather than just words as inputs. The input/output is word by word of a sequence, using previously outputted words.

Weights might not be shared between encoder and decoder. 
