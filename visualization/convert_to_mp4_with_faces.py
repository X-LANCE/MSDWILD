import os
import cv2
import pandas as pd


original_mp4_file_path = 'original_mp4_files'
mp4_files_with_faces = 'mp4_files_with_faces'
csv_per_file_path = 'csv_per_file' # 0,face,0,725,181,795,276,0

for file_name in os.listdir(original_mp4_file_path):
    if not file_name.endswith('mp4'):
        continue
    file_name = file_name.split(".")[0]
    
    csv_path = os.path.join(csv_per_file_path, f'{file_name}.csv')
    ori_mp4_path = os.path.join(original_mp4_file_path, f'{file_name}.mp4')
    tmp_saved_mp4_path = os.path.join(mp4_files_with_faces, f'{file_name}.tmp.mp4')

    saved_mp4_path = os.path.join(mp4_files_with_faces, f'{file_name}.mp4')

    # Open the original MP4 file
    video_capture = cv2.VideoCapture(ori_mp4_path)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(tmp_saved_mp4_path, fourcc, fps, (frame_width, frame_height))

    # Read the CSV file containing the face bounding boxes without using pandas
    with open(csv_path, 'r') as file:
        face_data = file.readlines()

    # Process each frame
    frame_number = 0
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Draw the face bounding boxes for the current frame
        for line in face_data:
            frame_id, _, face_id, x1, y1, x2, y2, _ = line.strip().split(',')
            if int(frame_id) == frame_number:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'Face {face_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Write the frame with the drawn bounding boxes
        out.write(frame)
        frame_number += 1

    # Release everything when job is finished
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()
    
    # for fast loading purpose
    os.system(f'ffmpeg -i {tmp_saved_mp4_path} -vcodec libx264 -acodec aac -preset fast -movflags +faststart  {saved_mp4_path} -y')
    os.system(f'python audio_visual_visualized.py -rttm rttm_per_file/{file_name}.rttm -mp4_path mp4_files_with_faces/{file_name}.mp4 -via_json_result ./json_per_file/{file_name}.json')