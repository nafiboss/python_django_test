$(function() {
   $('.topic_title').click(function(){
       $('.change_title').toggle();
       $('#title').val($('.topic_title').html().trim())
   })

   $('#title').keypress(function(){
       $('.topic_title').html($(this).val())
   })

    $('#title').blur(function(){
        $('.topic_title').html($(this).val())
    })

    $('#topic_update_form').submit(function() {
        var form_data = $(this).serialize();
        $.get('/newscred/edit_topic/?'+form_data,
            function(data) {
            alert(data);
        });
        $('.change_title').toggle();
        return false;
    });
});
