// initialize function
function init()
{
	if(!sessionStorage.getItem('user'))
	{
		sessionStorage.setItem('user',"Not Logged In");
		sessionStorage.setItem('logged_in',"false");
		sessionStorage.setItem('address',"NA");
	}
	
	if(sessionStorage.getItem('logged_in') == "true")
	{
		document.getElementById("logged_nav").style.display = "inline";
		document.getElementById("no_log_nav").style.display = "none";	
	}
	else
	{
		document.getElementById("no_log_nav").style.display = "inline";
		document.getElementById("logged_nav").style.display = "none";
	}
	
	// display username if the user is logged in
	document.getElementById("logged_in_user").innerHTML = sessionStorage.getItem('user');
	document.getElementById("profile_address").innerHTML = sessionStorage.getItem('address');
}

function logout()
{
	sessionStorage.removeItem('user');
	sessionStorage.removeItem('logged_in');
	
	init();
}

// initialize 
init();