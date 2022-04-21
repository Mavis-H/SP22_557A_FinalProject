import os
from MyMouseTrack import MyMouseTrack

vis_dir = "../vis"
data_dir = "../data"
for filename in os.listdir(vis_dir):
    f = os.path.join(vis_dir, filename)
    # checking if it is a file
    # TODO: check if file is a valid VIS image depends on final vis format
    if os.path.isfile(f) and filename.endswith(('.png', '.jpg', '.jpeg')): 
        tracking = MyMouseTrack(f)
        tracking.start_track()

        # store each vis data to its own dirctory
        directory = os.path.join(data_dir, filename.split('.')[0])
        if not os.path.isdir(directory):
            os.mkdir(directory)

        # count current result data file number
        path, dirs, files = next(os.walk(directory))
        file_count = len(files)

        # write to txt file
        txtfilepath = os.path.join(directory, str(file_count) + '.txt')
        with open(txtfilepath, 'w') as f:
            f.writelines('\n'.join(tracking.get_pos_data()))
            f.close()