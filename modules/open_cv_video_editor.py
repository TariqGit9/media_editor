# python modules
import cv2
import shutil
import os 
import time 
import zipfile

class VideoEditor:
    def __init__(self):
        self.output_file = 'resize_file.mp4'
        self.codec= "XVID"
        self.color_code = cv2.COLOR_BGR2GRAY


    def define_codec(self, codec):
        self.codec = cv2.VideoWriter_fourcc(*codec)

    def resize_video(self, input_path, output_width, output_height):
        cap = cv2.VideoCapture(input_path)
        output_width= int(output_width)
        output_height= int( output_height)

        fps = cap.get(cv2.CAP_PROP_FPS)
        codec = int(cap.get(cv2.CAP_PROP_FOURCC))
        self.output_file = 'static/result/'+str(int(time.time()))+'.mp4'
        out = cv2.VideoWriter(self.output_file,codec, fps, (output_width,output_height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            resized_frame = cv2.resize(frame, (output_width, output_height))
            out.write(resized_frame)

        cap.release()
        out.release()
        return self.output_file


    def flip_video(self, input_path):
        cap = cv2.VideoCapture(input_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        self.output_file = 'static/result/'+str(int(time.time()))+'.mp4'
        out = cv2.VideoWriter(self.output_file, self.codec, fps, (int(cap.get(3)), int(cap.get(4))))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            flipped_frame = cv2.flip(frame, 1)
            out.write(flipped_frame)

        cap.release()
        out.release()
        return self.output_file

    def add_text_to_video(self, input_path, text, color=(255, 255, 255),position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1,  thickness=2):

        cap = cv2.VideoCapture(input_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        self.output_file = 'static/result/'+str(int(time.time()))+'.mp4'
        out = cv2.VideoWriter(self.output_file, self.codec, fps, (int(cap.get(3)), int(cap.get(4))))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.putText(frame, text, position, font, font_scale, color, thickness)
            out.write(frame)

        cap.release()
        out.release()
        return self.output_file


    def join_videos(self, video_paths):
        video_captures = [cv2.VideoCapture(path) for path in video_paths]
        fps = int(video_captures[0].get(cv2.CAP_PROP_FPS))
        width = int(video_captures[0].get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_captures[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.output_file = 'static/result/'+str(int(time.time()))+'.mp4'
        fourcc = cv2.VideoWriter_fourcc(*self.codec)
        out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))

        audio_clips = []

        for cap in video_captures:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, (width, height))
                out.write(frame)


        for cap in video_captures:
            cap.release()
        out.release()
        return self.output_file

    def remove_audio(self,input_video):
        # Open the video file
        cap = cv2.VideoCapture(input_video)
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.output_file = 'static/result/'+str(int(time.time()))+'.mp4'
        out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height), isColor=True)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Write each frame to the output video
            out.write(frame)
        # Release video capture and writer objects
        cap.release()
        out.release()
        return self.output_file

    def extract_frames(self,input_video):
        # Open the video file
        cap = cv2.VideoCapture(input_video)
        output_folder = 'static/result/'+str(int(time.time()))
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Save the frame as an image in the output folder
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)

            frame_count += 1

        # Release the video capture object
        cap.release()

        folder_to_zip =output_folder
        zip_filename = 'static/result/'+str(int(time.time()))+'.zip'
        # Create a ZipFile object in write mode
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the folder and its subdirectories
            for foldername, subfolders, filenames in os.walk(folder_to_zip):
                for filename in filenames:
                    # Get the full path of the file
                    file_path = os.path.join(foldername, filename)
                    
                    # Define the name that the file will have in the zip file
                    # In this example, we strip the common prefix 'folder_to_zip/' from the filename
                    arcname = os.path.relpath(file_path, folder_to_zip)
                    
                    # Add the file to the zip file
                    zipf.write(file_path, arcname)
        try:
            shutil.rmtree(folder_to_zip)
            print(f'Folder "{folder_to_zip}" has been successfully deleted.')
        except OSError as e:
            print(f'Error deleting folder: {e}')
        return zip_filename
