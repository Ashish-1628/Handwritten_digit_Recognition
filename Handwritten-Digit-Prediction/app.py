import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)

# Load trained model
model = load_model("model/mnist_cnn_model.h5")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_path = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(image_path)

            # Process image
            img = Image.open(image_path).convert("L")
            img = img.resize((28, 28))

            img_array = np.array(img)
            img_array = 255 - img_array  # invert
            img_array = img_array / 255.0
            img_array = img_array.reshape(1, 28, 28, 1)

            prediction = np.argmax(model.predict(img_array))

    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
