🖊️ Handwritten Digit Recognition using CNN
An end-to-end Deep Learning project that classifies handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The project also includes a Flask-based web application for real-time digit prediction through image upload.


📌 Project Overview
Handwritten digit recognition is a fundamental problem in computer vision. This project uses a Convolutional Neural Network (CNN) to accurately classify grayscale images of handwritten digits.

The trained model is deployed using Flask, allowing users to upload a handwritten digit image and get instant predictions through a simple web interface.


🚀 Features
Data preprocessing and normalization
CNN-based deep learning model
Dropout regularization to prevent overfitting
Model evaluation with ~98% accuracy
Image preprocessing for real-world digit input
Flask web application for live predictions
Clean and responsive UI


🧠 Machine Learning Workflow

Data Collection

Dataset: MNIST Handwritten Digits Dataset  
60,000 training images  
10,000 testing images  
Image size: 28x28 grayscale

Data Preprocessing

Normalization (pixel values scaled 0–1)

Reshaping to (28, 28, 1) for CNN input

Inverting uploaded images to match MNIST format

Model Building

Convolutional Layers (Conv2D)

MaxPooling Layers

Fully Connected Dense Layers

Dropout for regularization

Softmax output layer (10 classes)

Model Deployment

Flask-based web app

User uploads image → Image preprocessing → Model prediction → Display digit



🛠️ Tech Stack

Programming Language: Python

Deep Learning Framework: TensorFlow / Keras

Libraries: NumPy, Matplotlib, Pillow

Web Framework: Flask

Frontend: HTML, CSS

Tools: Google Colab, VS Code



📊 Input

Handwritten digit image (PNG/JPG format)  
28x28 grayscale (auto-resized in backend)


📈 Output

Predicted digit (0–9)



▶️ How to Run the Project

1️⃣ Clone the repository

git clone https://github.com/your-username/handwritten-digit-recognition.git  
cd handwritten-digit-recognition  

2️⃣ Install dependencies

pip install -r requirements.txt  

3️⃣ Run the Flask app

python app.py  

4️⃣ Open in browser

http://127.0.0.1:5000  



📸 Screenshots

<p align="center"><b>Flask Web App – Digit Recognition</b></p>
<img width="700" alt="Flask UI" src="ADD_YOUR_SCREENSHOT_LINK_HERE" />
<br><br>

<p align="center"><b>Prediction Output</b></p>
<img width="700" alt="Prediction Result" src="ADD_YOUR_OUTPUT_SCREENSHOT_LINK_HERE" />



🎯 Future Enhancements

Add confidence percentage display
Implement drawing canvas input
Deploy on Render / AWS
Add confusion matrix visualization
Convert into REST API



👤 Author

Ashish Deswal  
MCA | Machine Learning Enthusiast  
📫 GitHub: https://github.com/Ashish-1628  


⭐ If you find this project useful, feel free to star the repository!
