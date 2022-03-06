
// function for setting up new account 
function registerAccount(username)
{
}

// register form handling 
const registerForm = document.getElementById("register-form");
const registerButton = document.getElementById("register-form-submit");
registerButton.addEventListener("click", (e) => 
{
	if(sessionStorage.getItem('logged_in') == "false")
	{
		e.preventDefault();
		const username = registerForm.username.value;
		const password = registerForm.password.value;
	
		console.log(username);
		registerAccount(username);
		location.reload();
	}
})