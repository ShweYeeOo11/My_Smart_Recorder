# My_Smart_Recorder

A Python-based video recorder application built using OpenCV. It features real-time video preview, recording capabilities, and multiple image processing filters.

## 🎬 Demo Video
<video src="demo video" width="100%" controls></video>

## 🚀 Key Features
- **Real-time Preview**: Displays live camera feed with zero latency.
- **Video Recording**: Saves high-quality video as an `.mp4` file (using MP4V codec).
- **macOS Compatible**: Optimized for QuickTime Player and other native macOS tools.
- **Visual Indicators**: Displays a red circle and "REC" text while recording, and "PREVIEW" while idle.

## 🛠 Extra Features 
I have implemented three dynamic image processing modules:
1. **Horizontal Flip**: Instantly mirrors the video stream 
2. **Grayscale Filter**: Converts the feed into a classic black and white aesthetic 
3. **Gaussian Blur**: Applies a smoothing blur effect for privacy or artistic focus
   
##  Controls
| Key | Action |
|-----|--------|
| **SPACE** | Start / Stop Recording |
| **F** | Toggle Horizontal Flip |
| **G** | Toggle Grayscale Filter |
| **B** | Toggle Gaussian Blur |
| **ESC** | Exit Application |

## Technical Details
- **FPS**: 20.0
- **FourCC**: MP4V
- **Library**: OpenCV-Python

##  How to Run
1. Ensure you have Python and OpenCV installed:
   ```bash
   pip install opencv-python
