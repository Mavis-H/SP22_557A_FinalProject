import os
from MyMouseTrack import MyMouseTrack

vis_dir = "../vis"
for filename in os.listdir(vis_dir):
    f = os.path.join(vis_dir, filename)
    # checking if it is a file
    # TODO: check if file is a valid VIS image depends on final vis format
    if os.path.isfile(f) and filename.endswith(('.png', '.jpg', '.jpeg')):  
        tracking = MyMouseTrack(f)
        tracking.start_track()
        print(filename + ": " + tracking.get_data())