$(document).ready(function(){
	var $userform=$('#login_user_form'); 
	$userform.on('submit', function(event){
		event.preventDefault();
		var username = $("#username").val();
		var password = $("#password").val();
		// Checking for blank fields.
		// POST data to the sever
		data = {'username' : username , 'password': password}
		$.post({
			url: '/user/login',
			data: JSON.stringify(data),
			success: function(data){
				$.cookie('userToken', data['token']);
				window.location.pathname = "/";
			},
			error: function(data){
				alert('Qualcosa è andato storto');
			},
			statusCode:{
				401:function(data){
					$("#formError").text('Registrazione fallita a causa di informazioni errate');
					$("#password").focus().val('');
				}
			}
		})
		console.log(data);
	});	
});
 
