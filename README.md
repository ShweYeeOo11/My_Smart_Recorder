# My_Smart_Recorder

A Python-based video recorder application built using OpenCV. This project was developed as part of Homework 1 for the Computer Vision course. It features real-time video preview, recording capabilities, and multiple image processing filters.

## 📸 Screenshots
![Program Screenshot](screenshot.png)
> *Note: Please replace 'screenshot.png' with your actual screenshot file name. Make sure to capture the "REC" mode with the red circle visible.*

##  Key Features
- **Real-time Preview**: Displays live camera feed.
- **Video Recording**: Saves the video as an `.avi` file using XVID codec.
- **Visual Indicators**: Displays a red circle and "REC" text while recording.
- **Interactive Controls**: Toggle recording and filters using keyboard hotkeys.

## Extra Features (Bonus Points)
I have implemented three additional image processing filters to enhance the recorder:
1. **Horizontal Flip**: Mirrors the video stream (useful for webcam use).
2. **Grayscale Filter**: Converts the video feed into classic black and white.
3. **Gaussian Blur**: Applies a smoothing blur effect to the video.

##  Controls
| Key | Action |
|-----|--------|
| **SPACE** | Start / Stop Recording |
| **F** | Toggle Horizontal Flip |
| **G** | Toggle Grayscale Filter |
| **B** | Toggle Gaussian Blur |
| **ESC** | Exit Application |

##  Technical Details
- **FPS**: 20.0
- **FourCC**: XVID (AVI container)
- **Library**: OpenCV-Python

##  How to Run
1. Ensure you have Python and OpenCV installed:
   ```bash
   pip install opencv-python
