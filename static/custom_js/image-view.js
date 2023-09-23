// Get the current URL
var currentURL = window.location.href;
currentURL = currentURL.replace('#','');
currentURL = currentURL.replace('image-editor','');


get_action_buttons()
function get_action_buttons(){
    var url = currentURL+"image-buttons"
    console.log(url)
    axios.get(url, {
    }).then(function(response) {
        if(response.data.result != ""){
            names= response.data.names
            urls= response.data.urls
            
            for(count = 0 ; count < names.length;count++){
                data= names[count]
                html = '<div class="col-lg-4 mb-4"><div class="card action-buttons text-white shadow"   data-name="'+data.name+'"  data-url="'+data.url+'"  id="button-'+count+'"><div class="card-body">';
                html+=data.name+'</div></div></div>'
                $('.add-buttons').append(html);
                var $divElement = $("#button-"+count);
                $divElement.css("background-color", getRandomDarkColor());
            }


        }
    });
}


$(document).on('click', '.action-buttons', function() {
    $('.download-button').html('')
    $(".resize-option").addClass('d-none');
    var url = $(this).attr("data-url")
    var name = $(this).attr("data-name")

    $("#function_name").val(url);
    $('.upload-title').text(name)
    if(url == 'resized_image'){
        $(".resize-option").removeClass('d-none');
    }
    $(".myuploadmodal").modal('show');

});



$(document).on('click', '.upload-files', function() {


    const uploadForm = document.getElementById('upload-form');
    const formData = new FormData(uploadForm)
    const fileInput = document.getElementById('image-file');
    const imageFile = fileInput.files[0];

    if (!imageFile) {
        alert('Please select an image file.');
        return;
    }

    formData.append('image', imageFile);

    // Make an Axios POST request to your server
    axios.post('/upload-image', formData, {
        headers: {
            'Content-Type': 'multipart/form-data', // Important for file uploads
        },
    })
    .then(function (response) {
        $('#download-image').attr('src', currentURL+'static/result/'+response.data.file);
        $('#uploadmodal').modal('show');
        link = '<a href="'+currentURL+'static/result/'+response.data.file+'" download class="btn btn-sm btn-primary">Download File</a>'
        $('.download-button').append(link)
        // Handle the response from the server
        // document.getElementById('response').textContent = response.data;
    })
})





// function removeoldData(){
//     $('#files-input').val('')
//     $('#files-input').removeAttr('multiple');
//     $('.text-option').addClass('d-none')
//     $('.resize-option').addClass('d-none')
// }



// function upload_validations(){
//     var fileValue = $('#files-input').val();
//     if(! fileValue){
//         alert("Select a file BC")
//         return false
//     }
//     var function_name= $("#function_name").val()
//     if(function_name == "resize_video"){
//         if($("#vid-height").val()==0 || $("#vid-width").val()==0){
//             alert("bc height and width should not be empty")
//             return false
//         }
//     }else if(function_name == 'add_text_to_video'){
//         if($("#video_text").val()==''){
//             alert("bc text should not be empty")

//             return false
//         }
//         if($("#colorPickerInput").val()==''){
//             $("#colorPickerInput").val('#000000')
//         }
//     }
// }


// $(document).on('click', '.upload-files', function() {

//     if(upload_validations() == false){
//         return
//     }

//     const uploadForm = document.getElementById('upload-form');
//     const formData = new FormData(uploadForm)
//     const progress = document.getElementById('progress');
//     const progressBar = document.getElementById('upload-progress');
//     const progressLabel = document.getElementById('progress-label');
//     const messageDiv = document.getElementById('message');
//     var url = currentURL+'upload';
//     axios.post(url,formData,{
//         headers: {
//             'Content-Type': 'multipart/form-data',
//         },
//         onUploadProgress: function (progressEvent) {
//             $('#myModal').modal('hide');
//             $('#uploadmodal').modal('show');

//             $('.download-button').html()
//             const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
//             progressBar.value = percentCompleted;
//             progressLabel.innerText = percentCompleted + '%';
//             $('.close-modal-progress').addClass('d-none')
//         },
//         timeout: 0, // Set a long timeout to accommodate large uploads
    
//     }).then(function(response) {

//         const data = response.data;
//         link = '<a href="'+currentURL+response.data.path+'" download class="btn btn-sm btn-primary">Download File</a>'
//         $('.download-button').append(link)
//         $('.close-modal-progress').removeClass('d-none')
        
        
//     });
// });

