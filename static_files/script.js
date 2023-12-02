// Function to validate password requirements
function validatePassword(password) {
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+,\-.\/:;<=>?@[\\\]^_`{|}~]).{8,}$/;
    return passwordRegex.test(password);
}

// Function to save changes to local storage
function saveChanges() {
    const nameInput = document.getElementById('name');
    const genderSelect = document.getElementById('gender');
    const birthdayInput = document.getElementById('birthday');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    // Validate password
    if (!validatePassword(passwordInput.value)) {
        alert('Password does not meet the requirements.');
        return;
    }

    // Ask for confirmation
    const isConfirmed = confirm('Are you sure you want to change your password?');
    if (!isConfirmed) {
        return;
    }

    // Save data to local storage
    localStorage.setItem('name', nameInput.value);
    localStorage.setItem('gender', genderSelect.value);
    localStorage.setItem('birthday', birthdayInput.value);
    localStorage.setItem('email', emailInput.value);
    localStorage.setItem('password', passwordInput.value);

    alert('Changes saved!');
}

// Function to discard changes and load data from local storage
function discardChanges() {
    // Load data from local storage
    document.getElementById('name').value = localStorage.getItem('name') || '';
    document.getElementById('gender').value = localStorage.getItem('gender') || 'male';
    document.getElementById('birthday').value = localStorage.getItem('birthday') || '';
    document.getElementById('email').value = localStorage.getItem('email') || '';
    document.getElementById('password').value = localStorage.getItem('password') || '';

    alert('Changes discarded.');
}

// Load data from local storage on page load
window.onload = function () {
    document.getElementById('name').value = localStorage.getItem('name') || '';
    document.getElementById('gender').value = localStorage.getItem('gender') || 'male';
    document.getElementById('birthday').value = localStorage.getItem('birthday') || '';
    document.getElementById('email').value = localStorage.getItem('email') || '';
    document.getElementById('password').value = localStorage.getItem('password') || '';
};
