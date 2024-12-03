function updateFileName() {
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");
    if (fileInput.files.length > 0) {
        fileNameDisplay.textContent = fileInput.files[0].name;
    } else {
        fileNameDisplay.textContent = "Supported formats: PDF, DOCX, TXT";
    }
}

// JavaScript for handling the upload progress and redirection after submission
document.getElementById('uploadForm').onsubmit = function(event) {
    event.preventDefault();

    var progressContainer = document.getElementById('progressContainer');
    var progressBar = document.getElementById('progressBar');
    progressContainer.style.display = 'block';

    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();

    xhr.upload.addEventListener('progress', function(event) {
        if (event.lengthComputable) {
            var percentComplete = (event.loaded / event.total) * 100;
            progressBar.style.width = percentComplete + '%';
            progressBar.textContent = Math.round(percentComplete) + '%';
        }
    });

    xhr.addEventListener('load', function() {
        if (xhr.status === 200) {
            progressBar.style.width = '100%';
            progressBar.textContent = 'Upload Complete';

            // Wait for 2 seconds before redirecting
            setTimeout(function() {
                window.location.href = '/web_developer';
            }, 2000); // 2000 milliseconds = 2 seconds
        } else {
            alert("Upload failed. Please try again.");
        }
    });

    xhr.open('POST', '/upload', true);
    xhr.send(formData);
};
