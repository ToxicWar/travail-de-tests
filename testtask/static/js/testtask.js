function initial(){
    $('.list-group-item').each(function(index, item){
        $.ajax({
            url: $(item).attr('href')+'/',
            dataType: 'json',
            async: false
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
            content += '<td class="field-data" data-id="'+value[value.length-1]+'" data-field="'+fields[i]+'">'+item+'</td>'
        });
        content += '</tr>';
    });
    content += '</tbody>';

    content += '</table>';
    $container.append(content);
}

function put_update_field(){
    var $input = $(this).find('input');
    $.ajax({
        type: "PUT",
        url: $('.list-group-item.active').attr('href')+'/',
        data: {
            field: $input.data('field'),
            id: $input.data('id'),
            data: $input.val()
        },
        dataType: 'json',
        async: false
    }).done(function(data){
        if (data['status'] == 'ok'){
            $input.parent().parent().text($input.val());
            $('#update-field').off('submit', put_update_field);
            $('.field-data').on('click', update_field);
        } else {
            alert(data['message']);
        }
    }).fail(function(error){
        alert("Что-то пошло не так");
    });
    return false;
}

function update_field(){
    $('.field-data').off('click', update_field);
    var $item = $(this);
    var html = '<form id="update-field">'+
        '<input data-id="'+$item.data('id')+'" data-field="'+$item.data('field')+'" type="text"/>'+
        '<button type="submit" class="btn btn-default">Изменить</button>'+
        '</form>';
    $item.html(html);
    $('#update-field').on('submit', put_update_field);
    return false;
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
    $('.field-data').on('click', update_field);
});