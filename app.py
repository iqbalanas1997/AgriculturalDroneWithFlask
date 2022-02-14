# Live Streaming Code

from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture('rtsp://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream')  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# Live sttreaming code end






# #Import necessary libraries
# from flask import Flask, render_template, Response
# import cv2
# camera = cv2.VideoCapture(0)
# '''
# for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
# for local webcam use cv2.VideoCapture(0)
# '''


# #Initialize the Flask app
# app = Flask(__name__)

# # The ‘/video_feed’ route returns the streaming response. Because this stream returns the images that are to be displayed in the web page, the URL to this route is in the “src” attribute of the image tag (see ‘index.html’ below). 

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
 

# @app.route('/')
# def home():
#    return render_template('index.html')

# @app.route('/scan?pwd')
# def scan(pwd):
#       if pwd =="iqbal": 
#          return render_template('scan.html')
#       else:
#          return render_template('index.html')
      
# @app.route('/cover')
# def cover():
#    return render_template('cover.html')


# if __name__ == '__main__':
#    app.run(debug=True)


# def gen_frames():  
#     while True:
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
