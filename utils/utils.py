def allowed_file(app ,filename):
    """
        Check if a file has an allowed extension.

        Args:
            filename (str): The name of the file to check.
            app (flask app): Flask application instence.

        Returns:
            bool: True if the file has an allowed extension, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def call_video_function(editor,function_name,filepath , colorPickerInput ='', video_text='', width=50 ,height=50):
    """
        Call a video processing function dynamically based on function_name.

        Args:
            editor: The video editor object.
            function_name (str): The name of the video processing function to call.
            filepath (str or list): The file path(s) to the video(s) to process.
            video_text (str, optional): Text to add to the video (for 'add_text_to_video' function).
            width (int, optional): Width for resizing the video (for 'resize_video' function).
            height (int, optional): Height for resizing the video (for 'resize_video' function).

        Returns:
            Result of the specified video processing function.
    """
    if(function_name== 'add_text_to_video'):
        editor.define_codec("XVID")
        colorPickerInput = hex_to_rgb(colorPickerInput)
        result = getattr(editor, function_name)(filepath[0],video_text,colorPickerInput)
    elif(function_name== 'resize_video'):
        editor.define_codec("XVID")
        result = getattr(editor, function_name)(filepath[0],width,height)  
    else:
        if(function_name== 'join_videos'):   
            result = getattr(editor, function_name)(filepath)
        else:
            editor.define_codec("XVID")
            result = getattr(editor, function_name)(filepath[0])
    return result



def hex_to_rgb(hex_color):
    """
        Convert a hexadecimal color code to an RGB tuple.

        Args:
            hex_color (str): The hexadecimal color code (e.g., "#RRGGBB").

        Returns:
            tuple: A tuple containing the RGB components as integers in the format (blue, green, red).
    """
    # Remove the '#' character if present
    hex_color = hex_color.lstrip('#')
    # Extract the individual RGB components
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    
    return  blue, green,red

