import time
import cv2


class MyMouseTrack:

    # store mouse movement data
    def __init__(self, image_name):
        self.mouse_pos_per_second = []
        # self.clicks = []
        self.image_name = image_name
        self.time_start = time.time()

    def start_track(self):
        # read and display the image
        img = cv2.imread(self.image_name, 1)
        cv2.imshow('image', img)
    
        # setting mouse handler for the image and calling the move_event() function
        cv2.setMouseCallback('image', self.move_event)

        # 0: wait for a key to be pressed to exit
        # n: wait n milliseconds then exit
        cv2.waitKey(0)

        # close the window
        cv2.destroyAllWindows()

    # function to track the position of mouse on the image the 
    def move_event(self, event, x, y, flags, params):
        time_now = time.time()
        time_past = round(time_now - self.time_start, 3) # past time since program start
        # checking for mouse movement
        if event == cv2.EVENT_MOUSEMOVE:
            self.mouse_pos_per_second.append(' '.join((str(x), str(y), str(time_past))))
        
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     self.clicks.append((x, y, time_past))

    # get mouse track data
    def get_pos_data(self):
        return self.mouse_pos_per_second