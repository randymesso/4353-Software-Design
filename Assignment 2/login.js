// function for validating whether the user/pssword combination is valid for an existing user for logging in 
function validUser(user,pssword)
{
	console.log(user + " " + pssword);
	return true;
}

// login form handling 
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
loginButton.addEventListener("click", (e) => 
{
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if(validUser(username,password)) 
	{
		sessionStorage.setItem('user',username);	
		sessionStorage.setItem('logged_in',"true");
		
		alert("You have successfully logged in.");
        location.reload();
    } 
	else 
        alert("Invalid Username/Password");
})
