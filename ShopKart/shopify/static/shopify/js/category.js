$(document).ready(function(){
    $(".first").on('click', function(){

        var id=$(this).data("category");
        $.ajax({
            url: '/list/'+id ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                console.log(response)
                $("#feature").html(response)
                }
         });
    });

        $.ajax({
            url: '/categories/' ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                console.log(response)
                $("#feature").html(response)
                    }
             });

      $(".second").on('click', function(){

        var id=$(this).data("sub_category");
        $.ajax({
            url: '/subcategories/'+id ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                console.log(response)
                $("#feature").html(response)
                }
         });
    });

      $(".product").on('click', function(){


         $.ajax({
            url: '/categories/' ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                console.log(response)
                $("#feature").html(response)
                    }
             });
    });

     $(".brands").on('click', function(){

     var id=$(this).data("brands");
     $.ajax({
        url: '/brands/'+id ,
        dataType: 'html',
        type:'get',
        success: function(response) {
            console.log(response)
            $("#feature").html(response)
                }
         });
    });



  });

