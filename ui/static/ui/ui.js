$(document).ready(function(){

	var createBlogTemplate = $('#create-blog-template').html();
 	var blogTemplate = $("#blog-li-template").html();
 	var deleteblogTemplate = $('#delte-blog-template').html();
 	var updateblogTemplate = $('#update-blog-template').html();
 	var commentsTemplate = $('#blog-li-comment').html();


	var refreshBlog = function refreshBlog(){
		$.get('/api/posts', function(data){
			$('.blogList').empty();
			$.each(data.posts, function(index, post){
				console.log('blog:', index, post)
				addblog(post);
			});
		});
	};
 	var addblog = function addblog(blog) {
 		blog.created_at = moment(blog.created_at).fromNow()
 		$('.blogList').append(Mustache.render(blogTemplate, blog));
 		refreshComment(blog.pk, "post");
 		//blogTemplate looks for HTML within this class,
 		// blog then says insert data into blog when funciton called
 	}


	var refreshComment = function refreshComment(pk, commentType){
		
		$.get('/api/' + commentType + 's/'+ pk + '/comments', function(data){
			console.log('comment server res:', data);
			// $('.commentList').empty();
			var rendered = Mustache.render(commentsTemplate, data)
			// console.log(rendered);
			$('.' + commentType + '-'+pk).find('.commentList').html(rendered);
			$.each(data.comments, function(index, comment){
			// 	console.log('comments:', index, comment)
				refreshComment(comment.pk, "comment");
			});
		});
	};
 	// var addcomment = function addcomment(comment, postPK) {
 	// 	console.log('comments for', comment)
 	// 	comment.created_at = moment(comment.created_at).fromNow()
 	// 	$('.post-'+postPK).find('.commentList').append(Mustache.render(Comment, comment));

 	// 	//blogTemplate looks for HTML within this class,
 	// 	// blog then says insert data into blog when funciton called
 	// }

	$('.blogList').on('submit', '.commentform', function(event){
		event.preventDefault();
		var $commentForm = $(this);
		var inputs = $commentForm.find('input[name]');
		var data = {};
		var commentType = $commentForm.data("comment-type");
		console.log(commentType)
		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});

		var item_pk = data.pk;
		$.ajax({
			"method" : "POST",
			"url" :'/api/' + (commentType === "comment" ? '/comments/':'/posts/') + data.pk + "/comments", 
			"data" : JSON.stringify(data),
			success: function(data){
			console.log('server')
			// window.location.pathname = "/";
			
			refreshComment(item_pk, commentType);
		}});

		console.log(data);
	});




 	$('.create-blog-button').on('click', function(event){
 		var rendered = Mustache.render(createBlogTemplate);
 		$('#form-display').html(rendered);//Displaying data to user
 		//in html file

 	});



	$('#form-display').on('submit', '#create_blog_form', function(event){
		event.preventDefault();
		var formData = new FormData($(this)[0]);
		var token = $.cookie('userToken')

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
					$('.error-message').remove()
					for(var key in data){
						$('[name='+key+']').after('<p class="error-message">' + data[key][0]['message'] + '</p>');
					}
				}
			}

    	});
    });

	// 	var $createblogForm = $(this);
	// 	var $content = $createblogForm.find('input[name="content"]');
	// 	var $title = $createblogForm.find('input[name="title"]');
	// 	var $image = $createblogForm.find('input[name="image"]');
	// 	var src = $image[0].value;
	// 	console.log(src);

	// 	$.post({
	// 		url: '/api/posts',
	// 		data: JSON.stringify({
	// 			token: $.cookie('userToken'),
	// 			title: $title.val(),
	// 			image: src,
	// 			content: $content.val()
	// 		}),
	// 		success: function(res){
	// 			addblog(res.post);
	// 			$content.val('');
	// 		},
	// 		statusCode:{
	// 			422: function (data) {
	// 				data = JSON.parse(data.responseJSON.PostForm);
	// 				$('.error-message').remove()
	// 				for(var key in data){
	// 					$('[name='+key+']').after('<p class="error-message">' + data[key][0]['message'] + '</p>');
	// 				}
	// 			}
	// 		}
	// 	});
	// });


	$(".blogList").on('click', '.update-blog-button', function(event){

 		$.get('/api/posts/' + $(this).data("pk"), function(data){
 			var template = updateblogTemplate;
 			console.log(data)
			$('#form-display').html(Mustache.render(template, data.posts[0]));
		});
 		
 	});

	$('#form-display').on('submit', '#update_blog_form', function(event){
		event.preventDefault();
		var $updateblogForm = $(this);
		var inputs = $updateblogForm.find('input[name]');
		var data = {};
		

		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});

		$.ajax({
			"method" : "PUT",
			"url" :'/api/posts/' + data.pk, 
			"data" : JSON.stringify(data),
			success: function(data){
			console.log('server')
			window.location.pathname = "/";
		}});

		console.log(data);
	});


	$(".blogList").on('submit', '#delete_blog_form', function(event){
		event.preventDefault();
		var $deleteblogForm = $(this);
		var inputs = $deleteblogForm.find('input[name]');
		var data = {};
		

		inputs.each(function(idx, element){
			data[element.name] = element.value; 
			// console.log(idx,element.name);
		});

		$.ajax({
			"method" : "DELETE",
			"url" :'/api/posts/' + data.pk, 
			success: function(data){
				refreshBlog();
			}
		});

		console.log(data);

 	});

	refreshBlog();
});


