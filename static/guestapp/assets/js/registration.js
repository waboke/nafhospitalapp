
$(document).ready(function(){
    $("id_username").change(function(){
    var username = $(this).val();
    $.ajax({
        url:' {% url 'usernameValidation' %}',
        data:{
            'username':username
        },
        datatype: 'json',
        success: function(data){
            if (data.is_taken){
               console.log(data)
            }
        }
    });
});
});
