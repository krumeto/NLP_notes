## Vector spaces notes

#### Preprocessing

The mind scheme is the following:
- Start with a dictionary of your text. All words get a dict number
- Encode the text against that dict.
- If sparce version, the space has n+1 columns, where n is the number of words.
- Generate counts of words

#### Logistic Regression

Given a word, how often does this word appear in each of the classes. 
- Helpful to imagine how the classes dictionaries look like.
    - Positive Frequency - how often does a word appear in the positive class
    - Negative Frequency - same as above for the negative class
    - in practice dictionary mapping to frequency

- Creating a matrix that corresponds to all features of the training example.
    - Per word, Vector of the following [Bias, Sum of positive frequencies, sum of negative frequencies]

Xm - [1, sum(freqs(w,1), sum(freqs(w, 0)))]

- Preprocessing:
    - Stop words + punctuation + handles + URLs
    - Stemming - transforming each word to each base stem "tuning -> tun"
    - Lowercasing



Implementation
freqs = build_freqs(tweets, labels) #Build frequencies dict
X = np.zeros((m, 3)) #Initialize matrix X

for i in range(m):
    p_tweet = process_tweet(tweets[i]) #Process tweet
    X[i,:] = extract_features(p_tweet, freqs) #Extract features