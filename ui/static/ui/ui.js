$(document).ready(function(){


 	var blogTemplate = $("#blog-li-template").html();
 	var createBlogTemplate = $('#create-blog-template').html();
 	var updateblogTemplate = $('#update-blog-template').html();


	var refreshBlog = function refreshBlog(){
		$.get('/api/posts', function(data){
			$('.blogList').empty();
			$.each(data.posts, function(index, post){
				addblog(post);
			});
		});
	};
 	var addblog = function addblog(blog) {
 		blog.created_at = moment(blog.created_at).fromNow()
 		$('.blogList').append(Mustache.render(blogTemplate, blog));
 		//blogTemplate looks for HTML within this class,
 		// blog then says insert data into blog when funciton called
 	}

	refreshBlog();

	$(".blogList").on('click', '.update-blog-button', function(event){
		var token = $.cookie('userToken');
 		$.get('/api/' + token + '/posts/' + $(this).data("pk"), function(data){
 			var template = updateblogTemplate;
 			console.log(data.posts[0])
			$('#form-display').html(Mustache.render(template, data.posts[0]));
		});
 		
 	});

	$('#form-display').on('submit', '#update_blog_form', function(event){
		event.preventDefault();
		var $updateblogForm = $(this);
		var inputs = $updateblogForm.find('input[name], textarea[name]');
		var data = {};
		

		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});

		var token = $.cookie('userToken');
		$.ajax({
			"method" : "PUT",
			"url" :'/api/' +  token + '/posts/' + data.pk, 
			"data" : JSON.stringify(data),
			success: function(data){
			console.log('server')
			window.location.pathname = "/";
		}});

	});



 	$('.create-blog-button').on('click', function(event){
 		var rendered = Mustache.render(createBlogTemplate);
 		$('#form-display').html(rendered);//Displaying data to user
 		//in html file

 	});



	$('#form-display').on('submit', '#create_blog_form', function(event){
 		event.preventDefault();
 		var formData = new FormData($(this)[0]);
 		var token = $.cookie('userToken');
 
 		$.ajax({
 	        url:"/api/" + token + "/post",
 	        type: 'POST',
 	        data: formData,
 	        contentType: false,
 	        processData: false,
 	        success: function(res){
 					addblog(res.post);
 			},
 			statusCode:{
 				422: function (data) {
 					data = JSON.parse(data.responseJSON.PostForm);
 					$('.errormessage').remove()
 					for(var key in data){
 						$('[name='+key+']').after('<p class="errormessage">' + data[key][0]['message'] + '</p>');
 					}
 				}
 			}
 
     	});
    });
    

    $(".blogList").on('submit', '#delete_post_form', function(event){
		event.preventDefault();
		var $deleteblogForm = $(this);
		var inputs = $deleteblogForm.find('input[name]');
		var data = {};
		

		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});

		var token = $.cookie('userToken');
		$.ajax({
			"method" : "DELETE",
			"url" :'/api/' +  token + '/posts/' + data.pk, 
			success: function(data){
			refreshBlog();
		}});

 	});

    refreshBlog();
});


