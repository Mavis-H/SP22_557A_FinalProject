import time
import cv2


class MyMouseTrack:

    # store mouse movement data
    def __init__(self, imageName):
        self.mouse_pos_per_second = []
        self.imageName = imageName

    def start_track(self):
        # read and display the image
        img = cv2.imread(self.imageName, 1)
        cv2.imshow('image', img)
    
        # setting mouse handler for the image and calling the move_event() function
        cv2.setMouseCallback('image', self.move_event)

        # 0: wait for a key to be pressed to exit
        # n: wait n milliseconds then exit
        cv2.waitKey(0)

        # close the window
        cv2.destroyAllWindows()

    # function to track the position of mouse on the image per second
    def move_event(self, event, x, y, flags, params):

        # checking for mouse movement
        if event == cv2.EVENT_MOUSEMOVE:
            self.mouse_pos_per_second.append((x,y))
        time.sleep(1)

    # get mouse track data
    def get_data(self):
        return self.mouse_pos_per_second