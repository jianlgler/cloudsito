/////////////////////////////////////////////////////////////
///LOGIN NOT WORKING
/////////////////////////////////////////////////////////////


// Below function Executes on click of login button.
function studlogin() {
    var attempt = 10; // Variable to count number of attempts.
    var username = document.getElementById("studId").value;
    var email = document.getElementById("studEmail").value;
    var password = document.getElementById("studPwd").value;
    
    if (username == "username" && password == "password" && email == "email@gmail.com") {
        alert("Login successfully");
        document.location.href = "../studDashboard.html"; // Redirecting to other page.
        return false;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have left " + attempt + " attempt;");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}


// Below function Executes on click of login button.
function proflogin() {
    var attempt = 10; // Variable to count number of attempts.
    var name = document.getElementById("profName").value;
    var surname = document.getElementById("studSurname").value;
    var password = document.getElementById("profPwd").value;

    if (name == "name" && password == "password" && surname == "surname") {
        alert("Login successfully");
        window.location.href = "../profDashboard.html"; // Redirecting to other page.
        return false;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have left " + attempt + " attempt;");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("profName").disabled = true;
            document.getElementById("studSurname").disabled = true;
            document.getElementById("profPwd").disabled = true;
            return false;
        }
    }
}
