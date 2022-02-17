class profile
{
	fullname;
	address1;
	address2;
	city;
	state;
	zipcode;
	
	usrname;
	pssword;
	
	constructor(u,p)
	{
		this.usrname = u;
		this.pssword = p;
	}
}

// initialize function
function init()
{
	if(!sessionStorage.getItem('user'))
	{
		sessionStorage.setItem('user',"Not Logged In");
		sessionStorage.setItem('logged_in',"false");
	}
	
	if(sessionStorage.getItem('logged_in'))
	{
		document.getElementById("logged_nav").style.display = "inline";
		document.getElementById("no_log_nav").style.display = "none";	
	}
	else
	{
		document.getElementById("no_log_nav").style.display = "inline";
		document.getElementById("logged_nav").style.display = "none";
	}
}

function logout()
{
	sessionStorage.removeItem('user');
	sessionStorage.removeItem('logged_in');
}

// initialize 
init();

// display username if the user is logged in
document.getElementById("logged_in_user").innerHTML = sessionStorage.getItem('user');