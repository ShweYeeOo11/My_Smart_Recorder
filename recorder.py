import cv2 as cv

# 1. Open the default camera
cap = cv.VideoCapture(0)

# 2. Check if camera opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# 3. Get frame width and height from the camera
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# 4. Set video recording options
fps = 20.0
fourcc = cv.VideoWriter_fourcc(*'mp4v')
output_file = 'output.mp4'
writer = None

# 5. Flags for recording and filter features
recording = False
flip_mode = False   # Toggle with 'F'
gray_mode = False   # Toggle with 'G'
blur_mode = False   # Toggle with 'B' 

print("SPACE: Record/Stop | F: Flip | G: Gray | B: Blur | ESC: Quit")

while True:
    # 6. Read one frame from camera
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive frame")
        break

    # 7. Filter Functions 
    
    # 7.1 Flip Filter
    if flip_mode:
        frame = cv.flip(frame, 1)
        
    # 7.2 Grayscale Filter
    if gray_mode:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # 7.3 Blur Filter (Gaussian Blur)
    if blur_mode:
        
        frame = cv.GaussianBlur(frame, (15, 15), 0)

    display_frame = frame.copy()

    # 8. If recording mode, draw red circle and REC text
    if recording:
        cv.circle(display_frame, (30, 30), 10, (0, 0, 255), -1)
        cv.putText(display_frame, "REC", (50, 35), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # 9. Save frame to video file
        if writer is not None:
            writer.write(frame)
    else:
        cv.putText(display_frame, "PREVIEW", (20, 35), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 10. Show the frame
    cv.imshow("My_Smart_Recorder", display_frame)

    # 11. Read keyboard input
    key = cv.waitKey(1) & 0xFF

    # 12. ESC key to quit
    if key == 27:
        break

    # 13. SPACE key to toggle preview/record mode
    elif key == 32:
        recording = not recording
        if recording:
            writer = cv.VideoWriter(output_file, fourcc, fps, (width, height))
            print("Recording started.")
        else:
            if writer is not None:
                writer.release()
                writer = None
                print("Recording stopped. File saved.")

    # 14. Toggle Filter Functions
    elif key == ord('f'):
        flip_mode = not flip_mode
    elif key == ord('g'):
        gray_mode = not gray_mode
    elif key == ord('b'):
        blur_mode = not blur_mode
        print(f"Blur Mode: {'ON' if blur_mode else 'OFF'}")

# 15. Release resources
cap.release()
if writer is not None:
    writer.release()
cv.destroyAllWindows()