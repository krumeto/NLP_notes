### Overview of translation

1. Start with word embeddings with both languages
2. Get the word embedding of a word in English and transform to French word vector space. Find a matrix for the transformation.
3. Get the transformed word vector and get the most similar word vector.

Transforming vectos = multiplication (np.dot) by matrix.
XR = Y
If you have two word matrices (language), you can learn R.
Solving for R:
Loop over:
- Loss = (||XR-Y||F)^2 - Frobenius norm - measuring the magnitude of a matrix, Easier to work with the squared Frobenius norm
- gradient = dLoss/dR
- R = R - a.gradient

Notes:
- The norm of the input vector is the same as the norm of the output vector. Rotations matrices do not modify the norm of the vector, only its directions.

### K-nearest neighbors

Some intuition - when thinking about buckets, think about hash tables.
Hash tables - think of each word being represented of just one number. Hash function takes a vector and assigns a value. 

#### Locality sensitive hashing

Think of plane as collection of all possible vectors. Normal vector is perpendicular to the plane. 
Then,take a dot product between the normal vector and vectors. If dot product is zero, the vector sits on the plane, and the sign speaks to where the dot product is located. 

Visualizing a dot product, imagine vector and the surface of the earth. Gravity pulls the vector to the earth. Where the rock falls is the magnitude of the vector, while the sign indicates the direction with respect to the normal vector (earch).

def side_of_plane(P,v):
    dotproduct = np.dot(P, v.T)
    sign_of_dot_product = np.sign(dotproduct)
    sign_of_dot_product_scaler = np.asscaler(sign_of_dot_product) 

    return sign_of_dot_product_scalar
##### Think of using many planes, getting multiple signals per plane. 

def hash_multiple_plane(P_l, v):
    hash_value = 0

    for i, P in enumerate(P_l):
    sign = side_of_plane(P,v)
    hash_i = 1 if sign >= 0 else 0
    hash_value += 2**i*hash_i

    return hash_value

##### Making a set of random planes
num_dimensions = 2 #300 in assigment
num_planes = 3 #10 in assignment

random_planes_matrix = np.random.normal(size=(num_planes, num_dimensions))

v = np.array([[2]])

def side_of_plane_matrix(P, v):
    dotproduct = np.dot(P, v.T)
    sign_of_dot_product = np.sign(dotproduct)
    return sign_of_dot_product

##### Document Search
Document representations