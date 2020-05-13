//Criando janela de confirmação antes da deleção de uma tarefa.
$(document).ready(function () {

   //var baseUrl = 'http://0.0.0.0:80/';
    var baseUrl = 'http://127.0.0.1:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var filter2 = $('#filter2');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();


        var delLink = $(this).attr('href');
        var result = confirm('Deseja realmente excuir a tarefa?');

        if (result) {
            window.location.href = delLink;
        }

    });


//    
    $(searchBtn).on('click', function() {
        searchForm.submit();

    });

    $(filter).change(function(){

        var filter = $(this).val();
        // console.log(filter);
        
        window.location.href = baseUrl + '?filter=' + filter;
    });
    
    // $(filter2).change(function(){

    //     var filter2 = $(this).val();
    //     // console.log(filter2);
        
    //     window.location.href = baseUrl + '?filter=' + filter2;
    // });
});

