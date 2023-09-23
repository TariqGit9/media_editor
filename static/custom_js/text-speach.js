var currentURL = window.location.href;
currentURL = currentURL.replace('#','');
currentURL = currentURL.replace('image-editor','');



$(document).on('click', '.upload-files', function() {

    $('.loading-modal').removeClass('d-none')
    const uploadForm = document.getElementById('upload-form');
    const formData = new FormData(uploadForm)
    const fileInput = document.getElementById('audio-file');
    const audioFile = fileInput.files[0];
    $('#uploadmodal').modal('show');
    if (!audioFile) {
        alert('Please select an  file.');
        return;
    }

    formData.append('audio', audioFile);

    // Make an Axios POST request to your server
    axios.post('/upload-audio', formData, {
        headers: {
            'Content-Type': 'multipart/form-data', // Important for file uploads
        },
    })
    .then(function (response) {
        var text= response.data.result
        $('#customWidthTextArea').text(text)
        console.log(text)
        $('.loading-modal').addClass('d-none')
        $('#uploadmodal').modal('hide');
    })
})
