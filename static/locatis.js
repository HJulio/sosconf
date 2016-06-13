window.fbAsyncInit = function() {
	FB.init({
		appId      : '480256485503823',
		xfbml      : true,
		version    : 'v2.5'
	});
};


//-- Login in the current user via Facebook and ask for email permission
function authUser() {

FB.getLoginStatus(function(response) {

		 if (response.status === 'connected') {
			 // connected
			 getProfileImage();

		 } else if (response.status === 'not_authorized') {
			 //app not_authorized
			 FB.login(function(response) {
					 if (response && response.status === 'connected') {
							 getProfileImage();
					 }
			 });

		 } else {
			 // not_logged_in to Facebook
			 FB.login(function(response) {
					 if (response && response.status === 'connected') {
							 getProfileImage();
					 }
			 });
		 }
});
}

function getProfileImage() {

var $photof = $('.fb-file'),
	 	$fbPhoto = $('img.fb-photo');


FB.api("/me/picture?width=600&height=600",  function(response) {

	 var profileImage = response.data.url.split('https://')[1];

	//remove if there and add image element to dom to show without refresh
	if( $fbPhoto.length ){
			$fbPhoto.remove();
	}
	$photof.val('http://' + profileImage +'');
});
}



(function(d, s, id){
	 var js, fjs = d.getElementsByTagName(s)[0];
	 if (d.getElementById(id)) {return;}
	 js = d.createElement(s); js.id = id;
	 js.src = "//connect.facebook.net/en_US/sdk.js";
	 fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));
