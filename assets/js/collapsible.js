document.addEventListener('DOMContentLoaded', function() {
    // Add click event listeners to all BibTeX toggle buttons
    const toggleButtons = document.querySelectorAll('.papercite_toggle');
    
    toggleButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Find the corresponding BibTeX content
            const content = this.nextElementSibling;
            
            // Toggle the visibility
            if (content.classList.contains('show')) {
                content.classList.remove('show');
            } else {
                content.classList.add('show');
            }
        });
    });
}); 