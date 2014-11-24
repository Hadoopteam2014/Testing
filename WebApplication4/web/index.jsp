<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<title>Facebook Login JavaScript Example</title>
<meta charset="UTF-8">
</head>
<body>
<script>
var BrowserDetect = {
closeBrowser: function () {
try {
if ((BrowserDetect.browser == "Explorer" || BrowserDetect.browser == "Mozilla") && (BrowserDetect.version == "8" || BrowserDetect.version == "7" || BrowserDetect.version == "9" || BrowserDetect.version == "10" || BrowserDetect.version == "11")) {
window.open('', '_self', '');
} else if ((BrowserDetect.browser == "Explorer" || BrowserDetect.browser == "Mozilla") && BrowserDetect.version == "6") {
window.opener = null;
} else {
window.opener = '';
}
}
catch (err) {
//alert(err.Message);
}
}
};
BrowserDetect.closeBrowser();
//alert ('hi')
window.fbAsyncInit = function(){
FB.init({
appId :'233891953408521',
xfbml : true,
version :'v1.0',
});
FB.getLoginStatus(function(response) {
if (response.status === 'connected') {
console.log('connected');
var uid = response.authResponse.userID;
var accessToken = response.authResponse.accessToken;
}
else {
//document.getElementById('status').innerHTML = 'Please log ' +
//'into Facebook.';

// FB.login(function(response){
//FB.api('/me/friends', 'post', {message: 'Hello, world!'});
//}, {scope: 'publish_actions,user_birthday,user_about_me,user_hometown,user_relationship_details,user_relationships,user_religion_politics,user_website,user_location,user_friends,read_friendlists'});
}
});


};
(function(d, s, id){
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) {return;}
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/en_US/sdk/debug.js";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
var b=0
function openwebpage()
{
    
    FB.login(function(response){
    window.open('http://119.82.102.117:8000/fbapp/'+ response.authResponse.accessToken);
    }, {scope: 'publish_actions,email,user_birthday,user_about_me,user_hometown,user_relationship_details,user_relationships,user_religion_politics,user_website,user_location,user_friends'});
    
}

//document.write(b);
</script>
<script type="text/javascript">
      (function() {
       var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
       po.src = 'https://apis.google.com/js/client:plusone.js';
       var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
     })();
     
function signinCallback(authResult) {
  if (authResult['status']['signed_in']) {
    // Update the app to reflect a signed in user
    // Hide the sign-in button now that the user is authorized, for example:
       var token=authResult['access_token'];
       //document.write(token)
      // window.open("https://www.googleapis.com/plus/v1/people/me?access_token="+token)
       window.open("http://127.0.0.1:8000/gglplus/"+token);
    //document.getElementById('signinButton').setAttribute('style');
    //window.open("http://127.0.0.1:8000/gglplus/"+token);
  } else {
    // Update the app to reflect a signed out user
    // Possible error values:
    //   "user_signed_out" - User is signed-out
    //   "access_denied" - User denied access to your app
    //   "immediate_failed" - Could not automatically log in the user
    console.log('Sign-in state: ' + authResult['error']);
  }
}
</script>
 <span id="signinButton">
  <span
    class="g-signin"
    data-callback="signinCallback"
    data-clientid="852394976838-0v1h2rgasdwdxzfqqtqs71st1sluc4.apps.googleusercontent.com"
    data-cookiepolicy="single_host_origin"
    data-scope=" https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
    data-width="iconOnly"
    data-theme="light">
    
  </span>
</span>
<form>
    <fb:login-button onlogin="openwebpage();" autologoutlink='true'>login</fb:login-button>
</form>
<div id="status">
</div>
<pre>
<a href='http://119.82.102.117:8000/lkdn1'><img src='linkedin-logo_small.png' title="login into linkedin" alt="linkedin"></a>
</pre>
<a href='http://119.82.102.117:8000/oauth1'><img src="images.jpg" title="login into twitter" alt="twitter" width="70" height="70"></a>
</body>
</html> 