function initial(){
    $('.list-group-item').each(function(index, item){
        $.ajax({
            url: $(item).attr('href'),
            dataType: 'json'
        }).done(function(data){
            create_table($(item).attr('href'), data.fields, data.qs);
        });
    });
    var $first = $('.list-group-item').first();
    $first.addClass('active');
    $('#'+$first.attr('href')+'-table').show();
}

function create_table(model, fields, data){
    var $container = $('#'+model+'-table');
    var content = '<table class="table table-striped table-hover">';

    content += '<thead><tr>';
    $.each(fields, function(index, value){
        content += '<th>'+value+'</th>'
    });
    content += '</tr></thead>';

    content += '<tbody>';
    $.each(data, function(index, value){
        content += '<tr>';
        $.each(value, function(i, item){
            content += '<td>'+item+'</td>'
        });
        content += '</tr>';
    });
    content += '</tbody>';

    content += '</table>';
    $container.append(content);
}

function change_tab(){
    var $active = $('.list-group-item.active');
    $active.removeClass('active');
    $('#'+$active.attr('href')+'-table').hide();
    $(this).addClass('active');
    $('#'+$(this).attr('href')+'-table').show();
    return false;
}

$(function() {
    initial();

    $('.list-group-item').on('click', change_tab);
});