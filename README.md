# Vector Embeddings
An embedding is data, like words that have been converted into an array of numbers known as a vector that contains patterns or relationships. The combination of these numbers that make up the vector
act as a multidimensional map to measure similarity.
# Example 
Let me describe a 2D graph. The words 'dog' and 'puppy' are used in similar situations. So, in a word embedding they would be represented by vectors that are close together. In reality the vector in hand has
hundreds of dimensions that cover the rich multidimensional relationships between words.

![example](/dog-puppy.png) 

Images can also be turned to vectors. That's how Google does similar image searches. How ? The image sections are broken down into arrays allowing you to find patterns of similarity for those with closely 
resembling vectors.

Once an embedding is created, it can be stored in a database.
So a database which is full of these embeddings is called a **vector database**. 
Uses of a vector database : 
- searching : where results are ranked by relevance to a query string
- clustering : where text strings are grouped by similarity
- recommendations : where items with related text strings are recommended.
- classifications : where text strings are classified by their most similar label.


The strength of embeddings is where you chunk large bits of information together such as paragraphs. 
The model 'ada-002' allows for maximum input of 8000 tokens.
