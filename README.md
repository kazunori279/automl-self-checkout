# automl-self-checkout
Self-checkout demo for AutoML Vision + Edge TPU 

## Requirements
- Raspberry Pi 3
- [Coral USB accelerator](https://coral.withgoogle.com/products/accelerator)
- .tflite model file trained with [Cloud AutoML Vision Edge](https://cloud.google.com/vision/automl/docs/edge-quickstart)

## Install required software

### Set screen resolution
> sudo vi /boot/config.txt

Uncomment the following lines and edit the width and height.

```
framebuffer_width=1024
framebuffer_height=600
```

### Install Edge TPU SDK
See https://coral.withgoogle.com/docs/accelerator/get-started/#set-up-on-linux-or-raspberry-pi

### Install OpenCV
> pip3 install opencv-python 

> sudo apt-get install -y libcblas-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev  libqtgui4  libqt4-test

### Install ImageTk
> sudo apt-get install python3-pil.imagetk

### Disable screen saver
> sudo apt-get install xscreensaver

> sudo reboot

On the desktop, change the screen saver setting as follows:

```
Menu > Preferences > Screensaver > [Display Modes] > Mode: Disable Screen Saver
```
### Place your TF Lite model as readable with the following path

> /home/pi/model.tflite

