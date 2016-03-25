/**
 * Created by noh on 2016-02-22.
 */

$(document).ready(function(){
    var now = new Date();
    var year= now.getFullYear();
    var mon = (now.getMonth()+1)>9 ? ''+(now.getMonth()+1) : '0'+(now.getMonth()+1);
    var day = now.getDate()>9 ? ''+now.getDate() : '0'+now.getDate();

    var chan_val = year + '-' + mon + '-' + day;
    var chan_val2 = year + '-' + mon;
    var chan_val3 = year+mon;
    $("#BtnDate").text(chan_val2);

});



$(function(){
    $('#BtnDateMinus').click(function(){
        var date = $('#BtnDate').html()
        $.ajax({

            url : "/moim_detail/" + $('#moim_name').html(),
            type : "GET",
            data : {"arrow" : "<<","date":date},

            success : function(data){
                var success_year = data.year;
                var success_month = data.month;
                $('#BtnDate').html(success_year + "-" + success_month)
            }
        });
    });

});


$(function(){



    $('#BtnDatePlus').click(function(){
        var date = $('#BtnDate').text()
        $.ajax({

            url : "/moim_detail/" + $('#moim_name').text(),
            type : "GET",
            data : {"arrow" : ">>","date":date},


            success : function(data){
                var success_year = data.year;
                var success_month = data.month;
                $('#BtnDate').text(success_year + "-" + success_month)
                var dateAJ = (function() {
                    var privateVar = $('#BtnDate').text(success_year + "-" + success_month).text();
                    return {
                        date : privateVar
                    };
                }());
            }
        });
    });
});




$(function(){
    $("#BtnDate").click(function(){
        alert('클릭');
    });
});

