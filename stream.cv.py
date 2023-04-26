import cv2
video = cv2.VideoCapture(0)
while True:
    ref, image = video.read()
    cv2.putText(image, 'Awesome', (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (197, 200, 255), 5, cv2.LINE_AA)
    cv2.imshow('Live Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
