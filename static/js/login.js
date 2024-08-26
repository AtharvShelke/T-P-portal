
const emailField = document.querySelector('.email-field');
const passwordField = document.querySelector('.password-field');
const popUp = document.querySelector('.popup-overlay')

const emailLabel = document.querySelector('#email-label');

emailLabel.addEventListener('click', () => {
    emailField.style.display = 'flex'
})

const passwordLabel = document.querySelector('#password-label');

passwordLabel.addEventListener('click', () => {
    passwordField.style.display = 'flex'
});

const closePopup = () => {
    popUp.style.display = 'none'
}

const passwordToggle = document.querySelector('.toggle-password')
passwordToggle.addEventListener('click', function (e) {
    var passwordInput = document.getElementById('password');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        e.target.classList.remove('fa-eye');
        e.target.classList.add('fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        e.target.classList.remove('fa-eye-slash');
        e.target.classList.add('fa-eye');
    }
});
document.getElementById('registerLink').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('termsPopup').style.display = 'flex';
});

document.getElementById('agreeBtn').addEventListener('click', function() {
    document.getElementById('termsPopup').style.display = 'none';
    
});

// Close the pop-up if clicked outside of the content
window.addEventListener('click', function(event) {
    const popup = document.getElementById('termsPopup');
    if (event.target === popup) {
        popup.style.display = 'none';
    }
});