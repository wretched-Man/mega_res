import os
import io
import cv2
import numpy as np
from django.conf import settings


def process(data):
    image = np.asarray(bytearray(data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    model_path = os.path.join(settings.BASE_DIR, 'ai_model', 'esrgan_64_64_x4.onnx')
    esrgan = cv2.dnn.readNetFromONNX(model_path)

    # Create blob from image
    blob = cv2.dnn.blobFromImage(
        image,
        1/255,
        swapRB=True
    )

    # set blob as input
    esrgan.setInput(blob)

    # processing result
    result = esrgan.forward()
    result = (np.transpose(result.squeeze().clip(0, 1), (1, 2, 0)) * 255).astype(int)[:, :, ::-1]
    
    result = cv2.imencode(".png", result)[1].data
    return_object = io.BytesIO(result)
    return return_object
