$(document).ready(function(){


 	var blogTemplate = $("#blog-li-template").html();


 	var searchParams = new URLSearchParams(window.location.search);
 	var subject = searchParams.get("subject");


	var refreshBlog = function refreshBlog(){
		if (subject === 'poker') {
			$.get('/api/poker', function(data){
				$('.blogList').empty();
				$.each(data.posts, function(index, post){
					addblog(post);
				});
			});
		} else if (subject === 'betting') {
			$.get('/api/betting', function(data){
				$('.blogList').empty();
				$.each(data.posts, function(index, post){
					addblog(post);
				});
			});
		} else if (subject === 'trading') {
			$.get('/api/trading', function(data){
				$('.blogList').empty();
				$.each(data.posts, function(index, post){
					addblog(post);
				});
			});
		}
	};
	
 	var addblog = function addblog(blog) {
 		blog.created_at = moment(blog.created_at).fromNow()
 		$('.blogList').append(Mustache.render(blogTemplate, blog));
 		//blogTemplate looks for HTML within this class,
 		// blog then says insert data into blog when funciton called
 	}

	refreshBlog();

	
});


