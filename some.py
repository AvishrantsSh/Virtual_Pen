import cv2
BLUR_RADIUS = 21
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

class Some(object):
    def __init__(self, frame):
        self.gray_background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.gray_background = cv2.GaussianBlur(self.gray_background,(BLUR_RADIUS, BLUR_RADIUS), 0)

    def process(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame,(BLUR_RADIUS, BLUR_RADIUS), 0)

        diff = cv2.absdiff(self.gray_background, gray_frame)
        _, thresh = cv2.threshold(diff, 40, 255, cv2.THRESH_BINARY)
        cv2.erode(thresh, erode_kernel, thresh, iterations=2)
        cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)
        return thresh