 $(document).ready(function(){
   $(".cart_quantity_up").on('click', function(){

     var id=$(this).data("cart_add");
     console.log(id)
     $.ajax({
            url: '/add/'+id ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                $("#feature").html(response)


                    }
            });
      });

    $(".cart_quantity_down").on('click', function(){
        var id=$(this).data("cart_remove");
     $.ajax({
            url: '/remove/'+id ,
            dataType: 'html',
            type:'get',
            success: function(response) {
                $("#feature").html(response)


                    }
            });

    });

 });
