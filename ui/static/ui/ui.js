$(document).ready(function(){


 	var blogTemplate = $("#blog-li-template").html();


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
});


