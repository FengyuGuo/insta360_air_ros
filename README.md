# ROS Wrapper for insta360 air  

This package is a wrapper to read image from insta360 air camera and publish by ros.

## Usage

1. install ros package usb_cam

    sudo apt-get install ros-$ROS_DISTRO-usb-cam

2. check the device name of insta360 air if you have multiple cameras on your computer. Check the device name by vlc -> media -> open capture device -> video device name -> play. Open the device and check if you can see the image.

3. goto insta360.launch and modify device name.

4. launch and check the image in ros  

    roslaunch ./insta360.launch

5. split the image by  
    python split.py <path_to_your_bag>