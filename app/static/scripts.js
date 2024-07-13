document.addEventListener('DOMContentLoaded', (event) => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('file');
    const uploadForm = document.getElementById('uploadForm');
    const preview = document.getElementById('preview');

    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropZone.classList.remove('dragover');

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            showPreview(files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (fileInput.files.length > 0) {
            showPreview(fileInput.files[0]);
        }
    });

    uploadForm.addEventListener('submit', (e) => {
        if (fileInput.files.length === 0) {
            alert('Please select a file first!');
            e.preventDefault();
        }
    });

    function showPreview(file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});
