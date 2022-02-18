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

// login form handling 
const profileForm = document.getElementById("profile-form");
const updateButton = document.getElementById("profile-form-submit");
updateButton.addEventListener("click", (e) => 
{
	e.preventDefault();
    const fullname = profileForm.fullname.value;
    const address1 = profileForm.address1.value;
	const address2 = profileForm.address2.value;
	const city = profileForm.city.value;
	const state = profileForm.state.value;
	const zipcode = profileForm.zipcode.value;
	
	sessionStorage.setItem('address',address1 + ", " + city + ", " + state + ", " + zipcode);
})
