$(document).ready(function(){
 	var $userform=$('#create_user_form'); 
	$userform.on('submit', function(event){
		event.preventDefault();


		var inputs = $userform.find('input[name]');
		var data = {};
		

		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});
			//Learn AJAX
		$.post({
			url: '/user/createuser',
			data: JSON.stringify(data), 
			success: function(data){
				console.log('server')
				$.cookie('userToken', data['token']); //Where is data defined
				window.location.pathname = "/login";
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
		});

	});
});