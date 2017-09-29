
$(document).ready(function(){
        var $userform=$('#contact_form'); 
        $userform.on('submit', function(event){
                event.preventDefault();
                var name = $("#name").val();
                var email = $("#email").val();
                var subject = $("#subject").val();
                var message = $("#message").val();
                console.log(name, email, subject, message)

                data = {'name' : name , 'email': email, 'subject' : subject , 'message': message}
                $.ajax({
                        url: '/api/messages',
                        type: 'POST',
                        data: JSON.stringify(data),
                        success: function(data){
                                $('#sendmessage').css('display', 'block');

                        },
                        error: function(data){
                                alert('Qualcosa è andato storto');
                        },
                })

        });     
});
