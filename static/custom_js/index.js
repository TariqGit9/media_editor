// Get the current URL
var currentURL = window.location.href;
currentURL = currentURL.replace('#','');

$(document).ready(function() {
    // Initialize the color picker
    $("#colorPickerInput").spectrum({
        preferredFormat: "hex",
        showInput: true,
        showPalette: true,
        palette: [
            ["#ff0000", "#00ff00", "#0000ff"],
            ["#ffff00", "#ff00ff", "#00ffff"]
        ]
    });
    
    // When the "Apply" button is clicked, get the selected color
    $("#applyColor").click(function() {
        var selectedColor = $("#colorPickerInput").spectrum("get").toHexString();
        console.log("Selected Color: " + selectedColor);
    });
});

get_action_buttons()
function get_action_buttons(){
    var url = currentURL+"get_buttons"
    console.log(url)
    axios.get(url, {
    }).then(function(response) {
        if(response.data.result != ""){
            names= response.data.names
            urls= response.data.urls
            console.log(response.data.names.length)
            
            for(count = 0 ; count < names.length;count++){
                data= names[count]
                console.log(data.name)
                input_model= data.input_model
                html = '<div class="col-lg-4 mb-4"><div class="card action-buttons text-white shadow" input-modal="'+input_model+'"  data-name="'+data.name+'"  data-url="'+data.url+'"  id="button-'+count+'"><div class="card-body">';
                html+=data.name+'</div></div></div>'
                $('.add-buttons').append(html);
                var $divElement = $("#button-"+count);
                $divElement.css("background-color", getRandomDarkColor());
            }


        }
    });
}

// onclick events

$(document).on('click', '.upload-files', function() {

    if(upload_validations() == false){
        return
    }

    const uploadForm = document.getElementById('upload-form');
    const formData = new FormData(uploadForm)
    const progress = document.getElementById('progress');
    const progressBar = document.getElementById('upload-progress');
    const progressLabel = document.getElementById('progress-label');
    const messageDiv = document.getElementById('message');
    var url = currentURL+'upload';
    $('#unremovableModalLabel').text('Uploading Please wait...')

    axios.post(url,formData,{
        headers: {
            'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: function (progressEvent) {
            $('.spinner-loading').removeClass('d-none')

            $('.download-button').html('')
            $('#myModal').modal('hide');
            $('#uploadmodal').modal('show');

            $('.download-button').html()
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            progressBar.value = percentCompleted;
            progressLabel.innerText = percentCompleted + '%';
            $('.close-modal-progress').addClass('d-none')
            if(percentCompleted==100){
                $('#unremovableModalLabel').text('Processing Please wait...')
            }
        },
        timeout: 0, // Set a long timeout to accommodate large uploads
    
    }).then(function(response) {

        const data = response.data;
        link = '<a href="'+currentURL+response.data.path+'" download class="btn btn-sm btn-primary">Download File</a>'
        $('.download-button').append(link)
        $('.close-modal-progress').removeClass('d-none')
        $('#unremovableModalLabel').text('Done !!!')
        $('.spinner-loading').addClass('d-none')
        
        
    });
});


$(document).on('click', '.action-buttons', function() {
    removeoldData()

    var url = $(this).attr("data-url")
    var input_modal = $(this).attr("input-modal");
    var name = $(this).attr("data-name")
    $('.upload-title').text(name)
    if(input_modal== "files"){
        $('#files-input').attr('multiple', 'multiple');
        console.log("multiple files asked")
    }
    if(input_modal== "text"){
        $('.text-option').removeClass('d-none')
    }
    if(input_modal== "resize"){
        $('.resize-option').removeClass('d-none')
    }
    
    $("#function_name").val(url);
    $(".myuploadmodal").modal('show');

});

// Functions

function removeoldData(){
    $('#files-input').val('')
    $('#files-input').removeAttr('multiple');
    $('.text-option').addClass('d-none')
    $('.resize-option').addClass('d-none')
}


function upload_validations(){
    var fileValue = $('#files-input').val();
    if(! fileValue){
        alert("Select a file BC")
        return false
    }
    var function_name= $("#function_name").val()
    if(function_name == "resize_video"){
        if($("#vid-height").val()==0 || $("#vid-width").val()==0){
            alert("bc height and width should not be empty")
            return false
        }
    }else if(function_name == 'add_text_to_video'){
        if($("#video_text").val()==''){
            alert("bc text should not be empty")

            return false
        }
        if($("#colorPickerInput").val()==''){
            $("#colorPickerInput").val('#000000')
        }
    }
}
