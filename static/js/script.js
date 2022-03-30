// function getDetails() {
//     var uname = document.getElementById('username').value;
//     var passwd = document.getElementById('password').value;
//     console.log(uname.test(reg_uname));
//     var reg_uname = "[^0-9a-zA-Z]+";
//     var pass2 = "Bharath@123"
//     if (uname.matches(reg_uname)) {
//         alert("Enter username");
//         document.getElementsByName("form1").username.focus;
//         uname.push("wrong");
//         return false;
//     } else {
//         uname.push("wrong");
//         return false;
//     }
//     if (passwd == pass2) {
//         alert("Enter password");
//         document.getElementsByName("form1").password.focus;
//         return false;
//     }
//     if (!uname.test("[^0-9a-zA-Z]+")) {
//         alert("User should not contain any special characters");
//         document.getElementsByName("form1").username.focus;
//         return false;
//     }

// }
$(document).ready(function() {
    $("form").attr("autocomplete", "off");
});

function getDetails() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    // if (username == "admin" && password == "user") {
    //     alert("login successful");
    //     return false;
    // } else {
    //     alert("login failed");
    // }
}