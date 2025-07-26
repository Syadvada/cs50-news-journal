
document.addEventListener('DOMContentLoaded', function() {
    // This script ensure empty form is not submitted

    const form = document.querySelector("form");
    const urlInput = document.getElementById("url");

    if (form && urlInput) {    
        form.addEventListener("submit", function(event) {
            if (!urlInput.value.trim()) {
                event.preventDefault();
                alert("Please enter a URL");
            } else if ( !urlInput.value.match(/^https?:\/\/.+/i) ) {
                event.preventDefault();
                alert("Please enter a valid URL starting with http:// or https://");
            } else {
                console.log("Form submission:", urlInput.value);
            }
        });
    }

    // This script autofocuses on the input field when page is loaded

    const firstInput = document.querySelector("input");
    if (firstInput) {
        firstInput.focus();
    }

    // This script ensure notes are toggled for visibility when clicked

    const buttons = document.querySelectorAll(".toggle-notes");
    
    buttons.forEach(function (btn) {
        btn.addEventListener("click", function() {
            const note = this.previousElementSibling;
            
            if (!note) {
                return;
            }
            
            const isHidden = window.getComputedStyle(note).display === "none";

            if (isHidden) {
                note.style.display = "block";
                this.textContent = "Hide Notes";
            }
            else {
                note.style.display = "none";
                this.textContent = "Show Notes";
            }
        })
    })
});