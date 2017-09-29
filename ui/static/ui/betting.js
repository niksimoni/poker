$(document).ready(function(){


 	var blogTemplate = $("#blog-li-template").html();

	var refreshBlog = function refreshBlog(){
		$.get('/api/fullbetting', function(data){
			$('.blogList').empty();
			$.each(data.posts, function(index, post){
				post.content = post.content.slice(0, 600) + '...';
				addblog(post)
			});
		});
	};

 	var addblog = function addblog(blog) {
 		$('.blogList').append(Mustache.render(blogTemplate, blog));

 	}

    refreshBlog();
});
