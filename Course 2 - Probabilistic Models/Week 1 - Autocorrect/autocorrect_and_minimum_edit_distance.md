## Autocorrect
How it works:
1. Identify a misspelled word:
- if word not in vocab: misspelled = True
2. Find strings n edit distance away:
- Operations performed on a string to change it
    - Insert a letter, Delete a letter, Replace or Switch a letter (swap 2 adjacent letters)
    - combining all possible options, gives you the space of all options
3. Filter candidates:
- Compare the candidates to actual words
4. Calculate word probabilities:
- Think of probability as frequency

### Algorithm for finding edit distances candidates:
- split using a list comprehension
splits_a = [(word[:i], word[i:]) for i in range(len(word) + 1)]

for i in splits_a:
    print(i)
- deletes a letter and produces a list of candidates
splits = splits_a
deletes = [L + R[1:] for L, R in splits if R]

### Minimum edit distance
- Think of edits having a different cost. For example, replace costing twice as much as delete. 

#### Minimum edit distance algorithm
- dynamic programming (see the visuals for reminder and think of different costs)
- Levenshtain distance - cost insert 1, delete 1, replace 2
- Backtrace is important - paths through the table
- the tabular method is the dynamic programming - solve a small problem and reuse the solution to solve a bigger problem.

### The End