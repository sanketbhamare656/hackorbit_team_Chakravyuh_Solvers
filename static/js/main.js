function showLoadingSpinner() {
    var input = document.querySelector('input[name="url"]');
    var button = document.querySelector('button');
    if (input.value.trim() !== '') {
        button.style.display = 'none';
        var spinner = document.createElement('div');
        spinner.className = 'spinner';
        button.parentNode.appendChild(spinner);
    }
}


// Show Navbar Links on Mobile
function showNavbar() {
    document.querySelector('.navbar-links').classList.add('show');
}

// Hide Navbar Links
function hideNavbar() {
    document.querySelector('.navbar-links').classList.remove('show');
}

// Ensure event listeners are attached
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".menu-icon").addEventListener("click", showNavbar);
    document.querySelector(".close-btn").addEventListener("click", hideNavbar);
});


function showNavbar() {
    document.getElementById('navbar-links').classList.add('show');
}

function hideNavbar() {
    document.getElementById('navbar-links').classList.remove('show');
}
