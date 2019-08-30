$(function(){
    $('#cbox').click(function(){
        var cb = $('#cbox').is(':checked');
        $('#e_date').prop('disabled', cb);
    });
});