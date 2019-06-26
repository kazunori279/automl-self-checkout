# automl-self-checkout
Self-checkout demo for AutoML Vision + Edge TPU 

## Requirements
- Raspberry Pi 3
- [Touch screen monitor for RasPi](https://www.amazon.com/UPERFECT-Monitor-Resolution-1024%C3%97600-Raspberry/dp/B07L62H6YR/)
- [Document camera with USB](https://www.amazon.com/Ipevo-Ziggi-HD-High-Definition-Document-Camera/dp/B01530XGMA/)
- [Coral USB accelerator](https://coral.withgoogle.com/products/accelerator)
- Model file: this repo doesn't include the model file. You need to collect training images with labels and create your own .tflite file. See [Cloud AutoML Vision Edge doc](https://cloud.google.com/vision/automl/docs/edge-quickstart) to learn the model creation process.
- This demo doesn't require any internet connection while working.

## Install required software

### Set screen resolution
> sudo vi /boot/config.txt

Uncomment the following lines and edit the width and height:

```
framebuffer_width=1024
framebuffer_height=600
```

### Install OpenCV

Install OpenCV for USB camera capture.

> pip3 install opencv-python 

Uninstall numpy to avoid version confliction with Edge TPU SDK.

> pip3 uninstall numpy

### Install ImageTk

Install ImageTk as UI lib.

> sudo apt-get install -y libcblas-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev  libqtgui4  libqt4-test

> sudo apt-get install python3-pil.imagetk

### Disable screen saver

> sudo apt-get install xscreensaver

> sudo reboot

On the desktop, change the screen saver setting as follows:

```
Menu > Preferences > Screensaver > [Display Modes] > Mode: Disable Screen Saver
```

### Install Edge TPU SDK
See: https://coral.withgoogle.com/docs/accelerator/get-started/#set-up-on-linux-or-raspberry-pi

### Place your TF Lite model on the following path

> /home/pi/model.tflite

### Test the model with Edge TPU

> cd automl-self-checkout

> python3 test.py

This should return something like:

> [(18, 0.84765625), (0, 0.1015625)]

that means the model recognizes the sample polo shirt image at score of 84.7%.

### Configure the labels, prices and images

Edit `labels` and `prices` definition in `main.py`, and the image files and their names in `/img` folder, according to your model definition.

### (Optional) Auto start setting

If you want to set up an auto start of the demo, use the following:

Add a service file:

> sudo vi /etc/systemd/system/automl-self-checkout.service

```
[Unit]
Description=automl-self-checkout demo

[Service]
User=pi
ExecStart=/usr/bin/python3 /home/pi/automl-self-checkout/main.py
WorkingDirectory=/home/pi/automl-self-checkout
Environment=DISPLAY=:0.0

[Install]
WantedBy=graphical.target
```

Reload systemd:

> sudo systemctl daemon-reload

Enable and check the status:

> sudo systemctl enable automl-self-checkout.service

> sudo systemctl status automl-self-checkout.service

Confirm the service would start:

> sudo systemctl start automl-self-checkout.service

## Run 

To run the app:

> cd automl-self-checkout

> python3 main.py

To stop the app, type `<Alt>+F4` on the UI, or: 

> killall python3

## Known issues

- UI response slows down when you runs the app over some hours: the `ui_updates()` function slows down due to unknow reason. Restarting the app solve this.

