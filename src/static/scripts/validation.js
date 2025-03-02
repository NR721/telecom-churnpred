document.addEventListener("DOMContentLoaded", function () {
    let inputs = document.querySelectorAll("input, select");
    let progressBar = document.getElementById("progressBar");
    let progressContainer = document.getElementById("progress-container");

    function updateProgress() {
        let filled = [...inputs].filter((input) => 
            input.value.trim() !== "" && input.value !== "0"
        ).length;
        let progress = (filled / inputs.length) * 100;
        progressBar.value = progress;
    }

    // Listen for changes in input fields & dropdowns
    inputs.forEach(input => {
        input.addEventListener("input", updateProgress);
        input.addEventListener("change", updateProgress);
    });

    // Prevent Negative Numbers
    let numberInputs = document.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.addEventListener("input", function () {
            if (this.value < 0) {
                this.value = ""; // Clear invalid input
                this.classList.add("error");
                showTooltip(this, "Value cannot be negative");
            } else {
                this.classList.remove("error");
                hideTooltip(this);
            }
        });
    });

    // Function to show tooltip
    function showTooltip(element, message) {
        let tooltip = element.parentNode.querySelector(".error-message");
        if (!tooltip) { // Prevent duplicate messages
            tooltip = document.createElement("small");
            tooltip.className = "error-message";
            tooltip.innerText = message;
            element.parentNode.appendChild(tooltip);
        }
    }

    // Function to hide tooltip
    function hideTooltip(element) {
        let tooltip = element.parentNode.querySelector(".error-message");
        if (tooltip) tooltip.remove();
    }

    // Ensure the Progress Bar remains sticky
    window.addEventListener("scroll", function () {
        if (window.scrollY > 10) {
            progressContainer.classList.add("sticky");
        } else {
            progressContainer.classList.remove("sticky");
        }
    });
});
