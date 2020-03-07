$(document).ready(function(){
    var deleteBtn = $('.delete-btn');

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function(event){

        event.preventDefault;

        var delLink = $(this).attr('href');
        var result = confirm('Pretende apagar esta tarefa?');

        if(result){
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });
});
