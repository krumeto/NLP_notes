## Vector spaces notes
Mental note - vector spaces are helpful when answers are W- questions?

"You shall know a word by the company it keeps"

### Word by word / word by doc
word by word - co-occurance of two of words is the number of times they occur together within a certain distance k. k is "two words away", for example. 

word by doc co-occurence - the number of times a word occurs within a certain category of the corpus.

### Vector space:
Representation of the above - see the picture

### Similarity function - Euclidean distance

Think of vectors in space starting with the origin (or dots). Euclidean distance is the hypotenuse.
For n-dimensional vectors, get the differences per dimension, square them up, sum them and get the square root of the results.

Problem - the distance can be large when the number of words is different, leading to smaller difference even when two corpora are more different. 

### Similarity function - Cosine similarity

If the angle between vector representations is small, the cosine will be close to 1, and as the angle approaches 90 degrees, the cosine approaches zero.

cos_sim = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

### Manipulating word vectors

Think of getting the capital of Russia, based on the vector spaces for USA, Washington and Russia. 
1) cap_dist = Washington - USA
2) guess = Russia + cap_dist
3) Similarity function(guess, neighboring points) - get the closest to the result.

### PCA
Logic - Original space -> Most uncorrelated features -> Dimension reduction

Eigenvector - give direction of uncorrelated features for the data
Eigenvalue - the amount of information retained by each feature (the variance of the new feature)
Dot product gives the projection on uncorrelated features
