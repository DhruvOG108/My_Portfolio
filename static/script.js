// Function to open the modal
function openModal(element) {
    var modal = document.getElementById("imageModal");
    var modalImg = document.getElementById("img01");
    
    modal.style.display = "block";
    modalImg.src = element.src;
}

// Function to close the modal
function closeModal() {
    var modal = document.getElementById("imageModal");
    modal.style.display = "none";
}

// Close modal if user presses ESC key
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        closeModal();
    }
});