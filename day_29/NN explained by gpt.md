<h1><center>Day 29
<h1><center>Deep learning with comoputer vision in tensorflow

---

### **Index and Visualization**
```python
index = 9000

# set number of character per row when printing
np.set_printoptions(linewidth=320)

# print the label and the image
print(f"label : {train_labels[index]}")
print(f"\nIMG PIXEL ARRAY :\n {train_img[index]}")

# visualize the image
plt.imshow(train_img[index])
```
1. **Index and Data Inspection**:
   - The variable `index` points to the 9000th image and label in the dataset (`train_img` and `train_labels`).
   - The `np.set_printoptions(linewidth=320)` ensures that when printing arrays, long lines are not wrapped into multiple rows.

2. **Visualization**:
   - The `print` statements output the label and pixel values of the image at index 9000.
   - `plt.imshow()` visualizes the image using Matplotlib.

---

### **Normalization**
```python
train_img = train_img / 255.0
test_img = test_img / 255.0
```
3. **Normalization**:
   - Dividing pixel values by 255 scales them to a range of [0, 1], which helps the neural network converge faster during training. This is a common preprocessing step.

---

### **Model Building**
```python
model = tf.keras.models.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```
4. **Defining the Neural Network**:
   - **Sequential Model**: A stack of layers where each layer’s output is the next layer's input.
   - **Flatten Layer**: Converts a 2D image (e.g., 28x28 pixels) into a 1D array to feed into the Dense layers.
   - **Dense Layer (Hidden Layer)**:
     - Contains 128 neurons with the ReLU activation function.
     - ReLU (Rectified Linear Unit): Introduces non-linearity and helps the model learn complex patterns.
   - **Dense Layer (Output Layer)**:
     - Contains 10 neurons (one for each class) with the Softmax activation function. This outputs probabilities for each class.

---

### **Softmax Activation Function**
```python
inputs = np.array([[-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]])
inputs = tf.convert_to_tensor(inputs)
print(f'input to softmax function {inputs.numpy()}')

outputs = tf.keras.activations.softmax(inputs)
print(f'output of softmax function : {outputs.numpy()}')

sum = tf.reduce_sum(outputs)
print(f'sum of outputs : {sum}')

prediction = np.argmax(outputs)
print(f'class with highest probability : {prediction}')
```
5. **Softmax Example**:
   - A tensor `inputs` is created containing some sample values.
   - The **Softmax function** converts these values into probabilities, ensuring they sum to 1.
   - The **highest probability index** is determined using `np.argmax`.

---

### **Compiling the Model**
```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```
6. **Compilation**:
   - **Optimizer**: Adam optimizer adjusts weights to minimize the loss.
   - **Loss Function**: `sparse_categorical_crossentropy` is used because the labels are integers (not one-hot encoded).
   - **Metric**: Accuracy is used to evaluate the model's performance during training and testing.

---

### **Training the Model**
```python
model.fit(train_img, train_labels, epochs=5)
```
7. **Training**:
   - The model is trained on the training images (`train_img`) and their labels (`train_labels`) for 5 epochs.
   - Each epoch involves a forward pass (prediction) and a backward pass (updating weights).

---

### **Evaluation**
```python
model.evaluate(test_img, test_labels)
```
8. **Testing**:
   - The model's performance is evaluated on a separate test dataset (`test_img` and `test_labels`).
   - The evaluation prints the loss and accuracy metrics for the test set.

---

### **What This Does Overall**
- Visualizes and pre-processes image data.
- Defines and trains a simple neural network for image classification.
- Tests the model's performance on unseen data.
- Demonstrates how softmax works to calculate probabilities.