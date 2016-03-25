/**
 * Created by noh on 2016-02-26.
 */
/**
 * Created by noh on 2016-02-26.
 */
$(function(){

    $("#year_plus").click(function(){
        var year_to_number = Number($("#year_val").text());
        var year_val = year_to_number +1
        $("#year_val").text(year_val)

    });

    $("#year_minus").click(function(){
        var year_to_number = Number($("#year_val").text());
        var year_val = year_to_number - 1
        $("#year_val").text(year_val)

    });

    $("#month_minus").click(function(){
        var month_to_number = Number($("#month_val").text());
        var month_val = month_to_number - 1


        if(month_val <10){
            $("#month_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#month_val").text(month_val)
        }

        if(month_val <1 ){
            $("#month_val").text('12')
        }

    });

    $("#month_plus").click(function(){
        var month_to_number = Number($("#month_val").text());
        var month_val = month_to_number + 1
        $("#month_val").text('0' + month_val)
        if(month_val <10){
            $("#month_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#month_val").text(month_val)
        }

        if(month_val >12 ){
            $("#month_val").text('01')
        }
    });

    //////////////////////nabu click//////////////////
    $("#mod_year_plus").click(function(){
        var year_to_number = Number($("#mod_year_val").text());
        var year_val = year_to_number +1
        $("#mod_year_val").text(year_val)

    });

    $("#mod_year_minus").click(function(){
        var year_to_number = Number($("#mod_year_val").text());
        var year_val = year_to_number - 1
        $("#mod_year_val").text(year_val)

    });

    $("#mod_month_minus").click(function(){
        var month_to_number = Number($("#mod_month_val").text());
        var month_val = month_to_number - 1


        if(month_val <10){
            $("#mod_month_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#mod_month_val").text(month_val)
        }

        if(month_val <1 ){
            $("#mod_month_val").text('12')
        }

    });


    $("#mod_month_plus").click(function(){
        var month_to_number = Number($("#mod_month_val").text());
        var month_val = month_to_number + 1
        $("#mod_month_val").text('0' + month_val)
        if(month_val <10){
            $("#mod_month_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#mod_month_val").text(month_val)
        }

        if(month_val >12 ){
            $("#mod_month_val").text('01')
        }
    });

    $("#mod_day_minus").click(function(){
        var month_to_number = Number($("#mod_day_val").text());
        var month_val = month_to_number - 1


        if(month_val <10){
            $("#mod_day_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#mod_day_val").text(month_val)
        }

        if(month_val <1 ){
            $("#mod_day_val").text('31')
        }

    });


    $("#mod_day_plus").click(function(){
        var month_to_number = Number($("#mod_day_val").text());
        var month_val = month_to_number + 1
        $("#mod_day_val").text('0' + month_val)
        if(month_val <10){
            $("#mod_day_val").text('0' + month_val)
        }
        else if(month_val >=10){
            $("#mod_day_val").text(month_val)
        }

        if(month_val >31 ){
            $("#mod_day_val").text('01')
        }
    });

    $('#save_change').click(function(){ //save 클릭
        var year_val = $("#year_val").text();
        var month_val = $("#month_val").text();
        var todayM = year_val +'-'+ month_val;
        $('#post_arrow').val('--');
        $('#post_TodayM').val(todayM);
        $('#post_form').submit();

    });

});



$(function(){
    var name = [];
    var mod_money = [];
    var mod_date = [];
    var mod_pk = [];
    var date_val = $('#BtnDate').text();

    var allData = {"name":name, "mod_money" : mod_money, "mod_date" : mod_date,"mod_pk" : mod_pk};

   // $('.amount_span').each(function(index) { //입금액 없을때
   //     var money = $(this).text()
   //     alert(money)
   //     var money_int = Number(money)
    //    var money_String = money_int.toString()

     //   if (money_String == "0"){
    //        $(this).text('미납')
//
      //  }
 //   });

    $(".name").each(function(i) {
        name.push($(this).text());
    });

    $(".amount_date_val").each(function(i) {
        mod_date.push($(this).val());
    });

    $(".amount_span_val").each(function(i) {
        mod_money.push($(this).val());
    });

    $(".mod_pk_val").each(function(i) {
        mod_pk.push($(this).val());
    });





    $('#dangwol').click(function() { //당월 클릭
        var now = new Date();
        var year= now.getFullYear();
        var mon = (now.getMonth()+1)>9 ? ''+(now.getMonth()+1) : '0'+(now.getMonth()+1);
        var day = now.getDate()>9 ? ''+now.getDate() : '0'+now.getDate();
        $("#year_val").text(year);
        $("#month_val").text(mon);
        //var chan_val = year + '-' + mon + '-' + day;



    });

    // $('#notice_reg_btn').click(function() { //A02 공지사항 등록 버튼 클릭시
    //     $('#Btn_notice_modal').unblockUI();

    // });

    $('#Btn_Notice_Delete').click(function(){
      //  var pk = $('#mod_pk_input').val()
        $('#mod_arrow2').val('notice_reg_del')
       // var arrow = $('#mod_arrow').val()
      //  alert(arrow)df
        $('#notice_reg_form2').submit()
    });

    $('#Notice_Save_reg_Btn').click(function(){
        $('#notice_reg_form2').submit()
    });





/////////////////////////////////////////공지사항 리스트/////////////////////////////
    $('.notice_toggle_div').each(function(index) { //A02 공지사항 리스트 버튼 클릭시
        $(this).children('textarea').hide() //숨기기
        var context = $(this).find('textarea').text()
        var title = $(this).find('#mod_title').text()
        var pk = $(this).find('#mod_pk').text()

        $(this).children('#mod').click(function(){ //A02 공지사항 수정 버튼 클릭시
            $('#notice_reg_title_mod_input_id').val(title)
            $('#notice_reg_paticle_mod_textarea_id').val(context)
            $('#mod_pk_input').val(pk)//pk값확인
        });

        $(this).children('a').click(function(){
            //   a =   $(this).children('a').text()
            $(this).parent(1).children('textarea').toggle() // 보였다 숨겼다.
            // alert(a)
        });
    });

     $('#Notice_Save_Btn').click(function() { //공지사항 리스트 세이브버튼 클릭
        alert('A02')
    });
/////////////////////////////////////////공지사항 리스트/////////////////////////////



/////////////////////////////////////////추가수입 리스트/////////////////////////////
    $('.add_money_list_toggle').each(function(index){
        $(this).children('textarea').hide() //숨기기
        var context = $(this).find('textarea').text()
        var title = $(this).find('#add_money_title').text()
        var pk = $(this).find('#add_moeny_pk').text()
        var money = $(this).find('#add_moeny_money').text()


       $(this).children('#add_money_mod').click(function(){
            $('#add_money_reg_title_mod_input_id').val(title)
            $('#add_money_reg_paticle_mod_textarea_id').val(context)
            $('#add_money_reg_money_mod_input_id').val(money)//pk값확인
            $('#add_money_mod_pk_input').val(pk)//pk값확인

        });

        $(this).children('a').click(function(){
            //   a =   $(this).children('a').text()
            $(this).parent(1).children('textarea').toggle() // 보였다 숨겼다.
            // alert(a)
        });
    })

    $('#add_moeny_Save_reg_Btn').click(function(){
       $('#add_money_mod_reg_form2').submit()

    });

    $('#add_money_Delete').click(function(){
      //  var pk = $('#mod_pk_input').val()
        $('#add_money_reg_mod_arrow').val('add_money_reg_del')
       // var arrow = $('#mod_arrow').val()
      //  alert(arrow)df
        $('#add_money_mod_reg_form2').submit()
    });


//////////////////////////////////////////////////////////////////

/////////////////////////////////////////지출관련////////////////////////////
    $('.consume_money_list_toggle').each(function(index){
        $(this).children('div').hide() //숨기기
        var context = $(this).find('textarea').text()
        var title = $(this).find('#consume_money_title').text()
        var pk = $(this).find('#consume_moeny_pk').text()
        var money = $(this).find('#consume_moeny_money').text()


       $(this).children('#consume_money_mod').click(function(){
            $('#consume_money_reg_title_mod_input_id').val(title)
            $('#consume_money_reg_paticle_mod_textarea_id').val(context)
            $('#consume_money_reg_money_mod_input_id').val(money)//pk값확인
            $('#consume_money_mod_pk_input').val(pk)//pk값확인

        });

        $(this).children('a').click(function(){
            //   a =   $(this).children('a').text()
            $(this).parent(1).children('div').toggle() // 보였다 숨겼다.
            // alert(a)
        });
    })

    $('#consume_moeny_Save_reg_Btn').click(function(){
       $('#consume_money_mod_reg_form2').submit()

    });

    $('#consume_money_Delete').click(function(){
      //  var pk = $('#mod_pk_input').val()
        $('#consume_money_reg_mod_arrow').val('consume_money_reg_del')
       // var arrow = $('#mod_arrow').val()
      //  alert(arrow)df
        $('#consume_money_mod_reg_form2').submit()
    });
/////////////////////////////////////////////////////////////////////


    $('.amount_date_span').each(function(index) { // 입금날짜 없을때
        var str = $(this).text()
        var n  = str.indexOf("2");
        if (n == "-1"){
            $(this).text('X')
        }

    });


    $('#mod_save_change').click(function() { //A02 공지사항 리스트 버튼 클릭시
        var year_val = $('#mod_year_val').text()
        var month_val = $('#mod_month_val').text()
        var day_val = $('#mod_day_val').text()
        $('#mod_day').val(year_val + '-' + month_val + '-' + day_val)
        $('#mod_form').submit();
    });

    $('#mod_del').click(function() { //A02 공지사항 리스트 버튼 클릭시
        $('#mod_arrow').val('mod_arrow_del')
        $('#mod_form').submit();
    });


    $('.amount_button').each(function(index) { // 입금날짜 없을때
        var str = $(this).text();
        var n  = str.indexOf("수");
        if (n == "-1"){
            $(this).click(function(){

                var year_val = $("#year_val").text();
                var month_val = $("#month_val").text();
                var todayM = year_val +'-'+ month_val;
                var name = allData.name[index];
                $('#post_name').val(name);
                $('#post_arrow').val('nabu');
                $('#post_TodayM').val(todayM);
                $('#post_form').submit();

            });
        }
        else{ // 납부 버튼이  수정일 때 클릭 이벤트
            $(this).click(function() {
                var now = new Date();
                var year= now.getFullYear();
                var month = (now.getMonth()+1)>9 ? ''+(now.getMonth()+1) : '0'+(now.getMonth()+1);
                var day = now.getDate()>9 ? ''+now.getDate() : '0'+now.getDate();
                //////////////////////날짜계산/////////////////////////////////

                var todayM = year_val +'-'+ month_val;
                var name = allData.name[index];
                var mod_money = allData.mod_money[index];
                var mod_date = allData.mod_date[index];
                var mod_pk = allData.mod_pk[index];

                $('#mod_year_val').text(year);
                $('#mod_month_val').text(month);
                $('#mod_day_val').text(day);

                $('#mod_amount_input_id').val(mod_money);
                $('#mod_pk_id').val(mod_pk);
                $('#mod_name').val(name);
                $('.nabusujung').text(name + ': 납부 수정')


                ////////////////현재날짜 셋팅////////////
                // alert(mod_money + mod_date + 'pk' + mod_pk) // 값확인
                //   $('#post_arrow').val('cancellation');
                //   $('#post_form').submit();
            });

        }


    });

});

