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


### Logistic Regression
Refresh:
- Given features X and labels Y, you use a function with parameters Theta (sigmoid for logreg) to produce outout Yhat. Then, you use minimize Cost function to compare Yhat and Y, after which the parameters are updated and the process is repeated.
- The sigmoid approaches 0 as Theta Transposed * x approaches -infinity
- The usual threshold is 0.5.

#### NLP context
1. Start with a tweet >> preprocess >> list of words/tokens >> x vector of frequencies [1, 3471, 245], [bias, positive freq, negative freq]

#### Log reg algorithm:
1. Initialize theta >> Classify/Predict Yhat >> Get gradient = 1/m*X^T*(h-y) >> Update theta Theta -= a.Grad >> Calculate the cost and return to classify step

2. Cost function reminder:
    J(Theta) = -1/m*sum((abs(y.log(h)) + abs((1-y),log(1-h))))

    as the log of anything between zero and one, the minus sign makes the overall positive.
    
