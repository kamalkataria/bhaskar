/**
 * Created by gayas on 8/4/17.
 */
$(document).ready(function()
{
//$('#comments_section').scrollator();
$('#commentbtn').click(
    function()
    {
        var email=$('#email').val();
        var name=$('#password').val();
        var message=$('#message').val();
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
});
 $.ajax({
 type:"POST",
 async:true,
 url: "/fastfoods/usercomments/",
 data:
 {
 useremail:email,username:name,usermessage:message
 },
 error: function(xhr){
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
 },
 success:function(result){
$.iaoAlert({
  mode:"dark",
  msg: result,
  type: "notification",
  autoHide: true,
  alertTime: "6000",
  position: 'bottom-right',
  closeButton: true,
  closeOnClick: true,
  zIndex: '999',
  fadeTime: "500"




});
 }
});




});
});
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}