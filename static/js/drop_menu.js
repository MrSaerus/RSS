//Закрытие меню по клику на документ
$(document).click(function() {
    $('.hc_drop_menu').removeClass('active');
});
//Отмена закрытия по клику на выпадающее меню
$('.hc_body_drop').click(function(event){
    event.stopPropagation();
});
//Клик по кнопке меню
$('.hc_drop_menu').click(function(event){
    if($(this).hasClass('active')){
        $('.hc_drop_menu').removeClass('active');
    }else{
        $('.hc_drop_menu').removeClass('active');
        $(this).addClass('active');
    }
    event.stopPropagation();
});

