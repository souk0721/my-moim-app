


$(function(){
    $("#moim_name").click(function(){ //월 클릭 변화
        location.replace('/moim_list/')

    });

    $('#btn').click(function() {
        $.blockUI({ message: $('#Btn_notice_see')
             ,onOverlayClick: $.unblockUI //모달 외부클릭시 닫기

            });
    });



});

