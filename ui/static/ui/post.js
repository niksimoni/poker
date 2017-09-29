$(document).ready(function(){

 	var postTemplate = $("#post-template").html();

 	var searchParams = new URLSearchParams(window.location.search);
 	var pk = searchParams.get("pk");



	var refreshPost = function refreshPost(){
		$.get('/api/posts/' + pk, function(data){
			$('.post').empty();
			$.each(data.posts, function(index, post){
				addPost(post);
			});
		});
	};

 	var addPost = function addPost(post) {
 		post.created_at = moment(post.created_at).fromNow();
 		$('.post').append(Mustache.render(postTemplate, post));
 		//blogTemplate looks for HTML within this class,
 		// blog then says insert data into blog when funciton called
 	};

	refreshPost();
});
