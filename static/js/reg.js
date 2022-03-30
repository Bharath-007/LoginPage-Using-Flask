function validateDetails() {
    var name = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var cpassword = document.getElementById('cpassword').value;
    if (!name.value.length >= 5) {
        alert("Name must be more than 4 characters");
        return false;
    }
    if (!email.matches(regex)) {

    }
    if (password != cpassword) {
        alert("Password not matches");
    }
    if (password.matches()) {

    }
    return true;
}

// function validateName() {
//     var name = document.getElementById('username').value;
//     if (name.length >= 5) {
//         return true;
//     } else {
//         alert("Name must be more than 4 characters");
//         return false;
//     }
// }