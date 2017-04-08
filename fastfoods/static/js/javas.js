/**
 * Created by gayas on 8/4/17.
 */
$(document).ready(function(){
$('#commentbtn').click(
    function(){
        var email=$('#email').val();
        var name=$('#password').val();
        var message=$('#message').val();
        $.get("/fastfoods/usercomments/",
            {useremail:email,username:name,usermessage:message},
            function(data){
            alert(data);
            });



    }
    
);

});