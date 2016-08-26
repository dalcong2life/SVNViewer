(function () {

    // SVN Repository 등록
    $('button[name=new_repository]').click(function () {
        $('#repository_form').modal('show');
    });

    // SVN Repository 추가
    //$('button[name=repository_ok]').click(function () {
    //
    //    var data = {
    //        product: 'mf2',
    //        repository_url: 'test_repor',
    //        base_revision: '1212',
    //        description: 'test_reportest_repor',
    //        active: 1
    //    };
    //
    //    $.ajax({
    //        url: '/svn/repository',
    //        type: 'post',
    //        dataType: 'json',
    //        contentType: 'application/json;charset=utf-8',
    //        data: JSON.stringify(data)
    //    }).done(function (response) {
    //        console.log(response);
    //        bootbox.alert("dfdf");
    //
    //    }).fail(function (error) {
    //        console.log(error);
    //    });
    //
    //
    //    $('#repository_form').modal('hide');
    //
    //});
    //
    //$('button[name=repository_cancel]').click(function () {
    //
    //
    //    $('#repository_form').modal('hide');
    //
    //});


})();
