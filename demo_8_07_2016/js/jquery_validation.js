	$(document).ready(function(){
	    $(".link1").click(function(){
	     // Initializing Variables With Form Element Values
		var firstname = $('#firstname').val();
		var lastname  = $('#lastname').val();
	    var phone     = $('#phone').val();
		var office    = $('#office').val();
		var email     = $('#email').val();
		var password  = $('#password').val();
		var confirm   = $('#Confirm').val();
		var year      = $('#year').val();
		var nameRegex   = /^[a-zA-Z]+$/;
		var emailRegex  = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
		var addRegex    = /^[0-9a-zA-Z]+$/;
		var phoneRegex  = /^[0-9]+$/;
		var passRegex   = /[0-9a-zA-Z]{8,10}$/;
		var currentDate = new Date();
		var currentYear = currentDate.getFullYear(); 
		var age = currentYear - year;
		var checkboxCount = 0;
		// To Check Empty Form Fields.
		if ( firstname.length == 0 ) {
			alert("Enter firstname"); // This Segment Displays The Validation Rule For All Fields
			$("#firstname").focus();
			return false;
		}
		// To Check Empty Form Fields For First Name.
		else if ( !firstname.match(nameRegex) || firstname.length == 0 ){
			alert("Enter first name in alphabet");
		}
		// To Check Empty Form Fields For Last Name
		if( !lastname.match(nameRegex) || lastname.length == 0 ){
			alert("Enter last name in alphabet");
	     	$("#lastname").focus();
		}
		// To Check Phone number is digit	
		if( !phone.match(phoneRegex) ){

			alert("Enter phone number in digit");
			$("#phone").focus();
		}
		if( phone.length!=10 ){
			alert("Enter phone number Length is not 10");
			$("#phone").focus();
		
		}
		// To Check office number is digit	
		if(!office.match(phoneRegex)){
			alert("Enter office number in digit");
			$("#office").focus();
		}
		// To Check Phone number is digit	
		if(!email.match(emailRegex)){
			alert("Enter proper email");
			$("#email").focus();
		}
		// To Check Password	
		if(!password.match(passRegex) || password.length <= 8 ){
			alert("Enter proper password");
			$("#password").focus();
		}
		// To Check Password	
		if (confirm.match(password) && confirm.length!=0){}
	
         else{

		alert(" Confirm password not same");
		}

		//setting age
		$("#age").val(age);

		for( i = 0 ; i < $('.checkbox').length ; i++ ){

			if( $('.checkbox')[i].checked == true ){

				checkboxCount++;

			}
		}
		if ( checkboxCount < 1 ){

			alert("please Check atleast one checkbox");

		}

    });
}); 
