// Get the current URL
var currentURL = window.location.href;
currentURL = currentURL.replace('#','');
currentURL = currentURL.replace('image-editor','');

get_action_buttons()

// Eventlistners 

// Eventlistner on action button

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


// Eventlistner for uploading file 
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

// get action buttons from the server to show on template 

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
