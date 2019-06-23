"""
Testing Edge TPU
"""
from edgetpu.classification.engine import ClassificationEngine
from PIL import Image

img = Image.open('img/sample_poloshirt.jpg')
tpu = ClassificationEngine('/home/pi/model.tflite')
results = tpu.ClassifyWithImage(img, top_k=3)
print(results)
