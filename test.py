"""
Testing Edge TPU
"""
from edgetpu.classification.engine import ClassificationEngine
from PIL import Image

# open an Image
img = Image.open('img/sample_pants.jpg')

# init Edge TPU with the model
tpu = ClassificationEngine('/home/pi/model.tflite')

# do prediction
results = tpu.ClassifyWithImage(img, top_k=3)
print(results)

