## Probability and Bayes' Rule

Think of probabilty as 'how frequently do things happen'
P(pos) = Npos/N.

### Conditional probability
Think of only the corpus containing given word, not the entire one.

P(A|B) = P(Positive|'happy') 3/4
P(B|A) = P('happy'|Positive) 3/13

P(X|Y) = P(Y|X)*P(X)/P(Y)

### Naive Bayes

Same pipeline -> get words -> get pos and neg counts -> get frequencies (think of probability given a class -> P(w|class)) 

-> Smooth probability function to account for words which do not appear in both classes (think "because" -> not great sentiment value, but only proba for one of the clasess) -> you do the smoothing by adding 1 to the numerator and the number of unique words in the denominator (think when you add up the ones, and devide by the unique words, you need to get 1)

To predict:
    Get the product of all P(w|pos)/P(W|neg) -> think what zero proba will do:
    I am happy today

    (0.2/0.2)*(0.2/0.2)*(0.14/0.1)*(0.1/0.1)

#### Laplace Smoothing
adding 1 to the numerator and the number of unique words in the denominator (think when you add up the ones, and devide by the unique words, you need to get 1)

#### Log Likelihood
Logarithms of the probabilities - helpful for conveniens
Think of a table of probas and ratio, having 1 being neutral, positive larger than one, negative smaller than one. 

#### Train Naive Bayes

Step 0: Collect and annotate corpus (label into positive and negative)
Step 1: Preprocess (lowercase, remove punctuations, etc..., remove stop words, stemming, tokenize)
Step 2: Compute vocabulary -> frequency table
Step 3: get Conditional proba P(word|class) + Laplace Smooting
Step 4: Get Lambda (the log of P(w|pos)/P(w|neg))
Step 5: Get the log prio = log(Number of positive tweets/Number of negative tweets)

#### Testing Naive Bayes

Sum the lambdas + logprior(). > 0 is positive.

#### Naive in the Naive Bayes - Assumptions

1. Independence between features
    "It is sunny and hot in the Sahara desert." - sunny and hot come frequently together, but Naive B. assumes they are. Does not take context into account

2. Relative frequencies in corpus - train corpus vs. real-live corpus distribution might lead to very optimistic or pessimistic model.

#### Sources of error:
1. Adversarial attacks (sarcasm, irony, euphemism)
2. Removing punctuation.
3. Word order changing meaning.

