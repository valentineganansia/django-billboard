
$('document').ready(function(){
   $('.post-new-cont').hide();
   $('.create-new-cont.font-cont').hide();

// On click "+" I WANT THE BOX "container post-new-cont" TO APPEAR AND TO HIDE THE "+" BUTTON

    $(".btn.btn-add").click(function(){
    console.log("'+' button")
    $('.btn.btn-add').hide();
    $('.create-new-cont.font-cont').show();
    $('.post-new-cont').show();
        });

// On click "x" I want my page to reload and to come back to the begin with the "+" button
    $(".btn.btn-times") .click(function(){
      console.log("'x' button ")
        $('.post-new-cont').hide();
        $('.create-new-cont.font-cont').hide();
        $('.btn.btn-add').show();
    });
});
