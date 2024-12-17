# Megares
Megares is a web application written in python.

It allows the user to load in an image and uses a GAN model (ESRGAN, there's also a repo for the same)
in the background to scale it up to **X4**.

It uses:
* OpenCV(for model inference and image preprocessing),
* celery (for offloading the model inference)
* redis (message scheduler for django) 
* django (backend)

Javascript fetch() method is used to query the backend for the complete celery task.

The web-application is responsive for different viewport sizes.

## NOTE
As mentioned in the main section, the ONNX model used for image upscaling is in its own [repo](https://github.com/wretched-Man/Real-ESRGAN).

I saved the model as an ONNX file. All the model processing is carried out in the `process_image.py` file. In this file, point to the location of the appropriate model or provide a file `esrgan_64_64_x4.onnx` in the same directory.

## TODO
1. Dockerize the web-app
2. Provide working links for the header and footer elements (about, help, terms-of-service, login  etc...)
3. Implement authorization (login and registration)
4. Implement tokens for users' - controlling the number of requests to be made.
