<h1><center>Day 30
<h1><center>Neural Netorks theory

### Application of Computer vision.
1. health care
2. Marketting
3. Facial Recognition 
4. Speech Recongnition

### Algorithm
Authomated instruction( formulas or method ).

# Artificial intelligence ( AI )
programs with the ability to mimic humans behaviors.

# Machine learning ( ML )
Algorithm with the ability to learn withoud being explicitly programmed to do so.

# Deep Learning
Subset for ML in which artificial neural networks adapt and learn from vast amount of data.

___
**Mnist** ( Modified national institute of standard and technology ) is a large database fo handwritten digits that is commonly used in machine learning and image processing.\
It his 
- 10 categories
- 70 k images
- 28 * 28 pixel in each image.
- it has another varient of fashion Mnist ( modern day most use )
- images are in greyscale
- each pixel can be between 0 to 255
- 28 * 28 = 784 bytes to store an image.

The amount of information is reduced for better proccessing.

```
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images, test_labels)
fmnist = fashion_mnist.load_data()

# every layer of  NN 
model = Keras.Sequential([
    keras.layers.Flatten(input(28,28))
    keras.layers.Dense(units= 128 , activation='relu' , metrics=['Accuracy'])
    keras.layers.Dense(10, activation='softmax')
])
```
--- IN the above code flaten convert the iamge to 1D for processing.(inut layer)
--- Dense create a hidden layer with relu activation function and have 128 neuron.
--- last Dense layer is output layer and has softmax activation function.

> What is tensor?
> A tensor is 3d structures or multidimentional array

> What is Sequential?
> Sequential is neural network architecture which have a linear stack of layers where you define a model by specifiying one layer at a time. It is the most simple and recommended for begginer.

