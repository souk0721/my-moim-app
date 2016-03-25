
#-*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from but_moim.forms import SignupForm
from django.core.urlresolvers import reverse
from but_moim.forms import User_Deposit,User_Info2
import json
from datetime import timedelta,date
from .models import *
from dateutil.relativedelta import relativedelta

from django.template import Context


def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        user_infor2_form = User_Info2()

        try:
            if User.objects.get(username=request.POST.get('username')):
                return render(
                    request,
                    'sign/sign.html',
                    {
                        'signupform' : signupform,
                        'user_infor2' : user_infor2_form,
                        'user_name' : request.POST.get('user_name'),
                        'tel' : request.POST.get('tel'),
                        'ID_error' : '아이디 중복 입니다..'
                    }
                )

        except :
            if signupform.is_valid():
                USer = signupform.save(commit=False)
                USer.email = signupform.cleaned_data['email'] #User Email 공간 저장
                USer.save()

                #User infor2 공간저장
                user = get_object_or_404(User, username=request.POST.get('username'))
                userinfo2 = user_info2(user = user,user_name=request.POST.get('user_name'),tel=request.POST.get('tel') )
                userinfo2.save()
                return HttpResponseRedirect(
                    reverse("login")
                )



            else:
                return render(request,
                              'sign/sign.html',
                              {
                                  'signupform' : signupform,
                                  'user_infor2' : user_infor2_form,
                                  'user_name' : request.POST.get('user_name'),
                                  'tel' : request.POST.get('tel'),
                                  'pass_error' : '패스워드가 맞지 않습니다.'
                              }
                              )

    elif request.method =='GET':

        signupform = SignupForm()
        user_infor22 = User_Info2()
        return render(request,
                      'sign/sign.html',
                      {
                          'signupform' : signupform,
                          'user_infor2' : user_infor22,
                      }
                      )


@login_required()
def moim_list(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        user = get_object_or_404(User, username=request.user)

        try:
            Moim_info_all = moim_info.objects.all()
            User_info_all = user_info.objects.all()
            User_info2_all = user_info2.objects.get(user=request.user)
            User_info = user_info.objects.filter(user = request.user)

        except:
            print("nono")
            User_info2_all = ""
            User_info =""

            #Moim_list = User_info.moim_name.filter(user=request.user)
            #moim_list = Moim_list.get().moim_name
    return render(
        request,
        'moim_list.html',
        {
            #'form': edit_form,
            'moim_info':Moim_info_all,
            'moim_name': User_info_all,
            'user_infor2_all': User_info2_all,
            'user_name': user,
            'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )





def moim_detail(request,moim_name):

    today = str(date.today())
    todayM = today[0:7]
    request_year = todayM[0:4]
    request_month = todayM[5:]
    year = request_year
    month = request_month

    manager = ""
    user = ""
    notuser =""

    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        try:
            try:
                user_info_object_moim = user_info.objects.filter(moim_name__moim_name = moim_name)
                for user_info_object_moim_for in user_info_object_moim:
                    try:
                        deposit_info.objects.get(user__username=user_info_object_moim_for.user,moim_name__moim_name = moim_name,deposit_date=todayM)

                    except:
                        moim_object = moim_info.objects.get(moim_name = moim_name)
                        User_object = User.objects.get(username = user_info_object_moim_for.user)
                        User_Info2_object = user_info2.objects.get(user__username = User_object.username)
                        depositinfo = deposit_info(user=User_object,moim_name = moim_object,user_name=User_Info2_object,deposit_yse_no=False,
                                               deposit_date=todayM,deposit_date_Day=today,deposit_amount=moim_object.deposit_amount)
                        depositinfo.save()

                deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)

            except:
               deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)


            Notice_info = notice.objects.filter(moim_name__moim_name=moim_name).exclude(notice_date=None).order_by('-pk')
            Moim_Info = moim_info.objects.get(moim_name=moim_name) #잘못된 모임이름이 들어왔을 때 오류

            Deposit_information = user_info.objects.filter(moim_name__moim_name=moim_name)
            ###################################금액 조정##############################################################
            moim_money_oj = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=True)
            moim_money_oj_month = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=True, deposit_date=todayM)#돈계산
            moim_money_oj_month_no_money_count_filter = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=False, deposit_date=todayM)

            moim_money_oj_add_month = add_money.objects.filter(moim_name__moim_name=moim_name, add_money_date=todayM)#돈계산
            moim_money_oj_add_month_total = add_money.objects.filter(moim_name__moim_name=moim_name)

            moim_money_oj_consume_month = withdraw_info.objects.filter(moim_name__moim_name=moim_name, withdraw_date=todayM)#돈계산
            moim_money_oj_consume_month_total = withdraw_info.objects.filter(moim_name__moim_name=moim_name)

            add_money_count = moim_money_oj_add_month.count()
            consume_money_count = moim_money_oj_consume_month.count()
            no_money_count = moim_money_oj_month_no_money_count_filter.count()


            total_money = Moim_Info.moim_total_money
            month_money = 0
            month_add_money = 0
            month_consume_money = 0
            total_month_money_plus_add_money = 0

            for moim_money in moim_money_oj:
                total_money = total_money + moim_money.deposit_amount

            for moim_money_month_add_total in moim_money_oj_add_month_total:
                total_money = total_money + moim_money_month_add_total.add_money

            for moim_money_month_consume_total in moim_money_oj_consume_month_total:
                total_money = total_money - moim_money_month_consume_total.withdraw_money

            for moim_money_month in moim_money_oj_month:
                month_money = month_money + moim_money_month.deposit_amount

            for moim_money_month_add in moim_money_oj_add_month:
                month_add_money = month_add_money + moim_money_month_add.add_money

            for moim_money_month_consume in moim_money_oj_consume_month:
                month_consume_money = month_consume_money + moim_money_month_consume.withdraw_money

            Moim_Info.moim_total_money2 = total_money
            Moim_Info.save()
            total_month_money_plus_add_money = (month_money + month_add_money)-month_consume_money

            #########################################################################################


            user_deposit_info = deposit_info.objects.filter(moim_name__moim_name=moim_name,
                                                            deposit_date=todayM)
            user_deposit_info2 = deposit_info.objects.filter(moim_name__moim_name=moim_name)
            User_info = user_info.objects.filter(moim_name__moim_name=moim_name) #모임이름으로 필터링
            User_info_user = user_info.objects.filter(user=request.user)

            ############################추가수입등록####################################################
            try:
                add_money_object = add_money.objects.filter(moim_name__moim_name=moim_name,add_money_date=todayM).order_by('-pk')
            except:
                return HttpResponse('추가수입등록ex')
                add_money_object = ''
                #return HttpResponse('add_money_no_object')
            #############################add_money####################################################


            ############################지출관련####################################################
            try:
                consume_money_object = withdraw_info.objects.filter(moim_name__moim_name=moim_name,withdraw_date=todayM).order_by('-pk')
            except:
                return HttpResponse('추가수입등록ex')
                consume_money_object = ''
                #return HttpResponse('add_money_no_object')
            #######################################################################################

            for user_Info_for in User_info:
                if user_Info_for.manager == True and user_Info_for.user == request.user:
                    manager = 'True'

                elif user_Info_for.user == request.user:
                    user = 'True'

                elif user_Info_for.user != request.user:
                    notuser = 'True'


        except:
            return render(
                request,
                'error.html',
                {
                    'error':'잘못된 모임 이름입니다.'
                }

            )

    if request.is_ajax():
        arrow = request.GET['arrow']
        request_date = request.GET['date']
        request_year = request_date[0:4]
        request_month = request_date[5:]
        year = int(request_year)
        month = int(request_month)


        #month = request.GET['month']
        #day = request.GET['day']

        if arrow == "<<":
            year = year
            month = month -1
            if month == 0:
                year = year -1
                month = 12
            elif month < 10:
                month = "0" + str(month)

        if arrow == ">>":
            year = year
            month = month +1
            if month == 13:
                year = year +1
                month = "01"

            elif month < 10:
                month = "0" + str(month)


        response_data = {}
        response_data['year'] = str(year)
        response_data['month'] = str(month)


        jsonData = json.dumps(response_data)
        return HttpResponse(jsonData,content_type="application/json")



        #Moim_list = User_info.moim_name.filter(user=request.user)
        #moim_list = Moim_list.get().moim_name
    return render(
        request,
        'moim_detail.html',
        {
            #'form': edit_form,
            #'total_money' :total_money,
            'month_consume_money':month_consume_money,
            'no_money_count':no_money_count,
            'consume_money_count':consume_money_count,
            'add_money_count':add_money_count,
            'consume_money_object':consume_money_object,
            'month_plus_add_money':total_month_money_plus_add_money,
            'add_money_month':month_add_money,
            'add_moeny_object':add_money_object,
            'deposit_infor':deposit_info_object,
            'month_money' : month_money,
            'notice_info':Notice_info,
            'moim_info':Moim_Info,
            'TodayM':todayM,
            'year' : year,
            'month' : month,
            'user_deposit_info2':user_deposit_info2,
            'user_deposit_info' : user_deposit_info,
            'Manager' : manager,
            'User' : user,
            'NotUser' : notuser,
            'moim_name': moim_name,
            'user_info': User_info,
            'deposit_amount':Moim_Info,

            #'moim_name' :Moim_list,
        }
    )


def moim_detail_post(request):
    today = str(date.today())
    manager = ""
    user = ""
    notuser =""
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)


    if request.method == 'POST':
        Notice_info = ''
        arrow = request.POST.get('arrow')
        todayM = request.POST.get('TodayM')
        name = request.POST.get('name')
        request_year = todayM[0:4]
        request_month = todayM[5:]
        year = int(request_year)
        month = int(request_month)
        moim_name = request.POST.get('moim_name')
        Moim_Info = moim_info.objects.get(moim_name=moim_name)

        if arrow == "<<":
            year = year
            month = month -1
            todayM = str(year)+'-'+str(month)
            if month == 0:
                year = year -1
                month = 12
                todayM = str(year)+'-'+str(month)
            elif month < 10:
                month = "0" + str(month)
                todayM = str(year)+'-'+str(month)

            try:
                user_info_object_moim = user_info.objects.filter(moim_name__moim_name = moim_name)
                for user_info_object_moim_for in user_info_object_moim:
                    try:
                        deposit_info.objects.get(user__username=user_info_object_moim_for.user,moim_name__moim_name = moim_name,deposit_date=todayM)

                    except:
                        moim_object = moim_info.objects.get(moim_name = moim_name)
                        User_object = User.objects.get(username = user_info_object_moim_for.user)
                        User_Info2_object = user_info2.objects.get(user__username = User_object.username)
                        depositinfo = deposit_info(user=User_object,moim_name = moim_object,user_name=User_Info2_object,deposit_yse_no=False,
                                               deposit_date=todayM,deposit_date_Day=today,deposit_amount=moim_object.deposit_amount)
                        depositinfo.save()

                deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)

            except:
               deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)

        elif arrow == ">>":
            year = year
            month = month +1
            todayM = str(year)+'-'+str(month)
            if month == 13:
                year = year +1
                month = "01"
                todayM = str(year)+'-'+str(month)

            elif month < 10:
                month = "0" + str(month)
                todayM = str(year)+'-'+str(month)

            try:
                user_info_object_moim = user_info.objects.filter(moim_name__moim_name = moim_name)
                for user_info_object_moim_for in user_info_object_moim:
                    try:
                        deposit_info.objects.get(user__username=user_info_object_moim_for.user,moim_name__moim_name = moim_name,deposit_date=todayM)

                    except:
                        moim_object = moim_info.objects.get(moim_name = moim_name)
                        User_object = User.objects.get(username = user_info_object_moim_for.user)
                        User_Info2_object = user_info2.objects.get(user__username = User_object.username)
                        depositinfo = deposit_info(user=User_object,moim_name = moim_object,user_name=User_Info2_object,deposit_yse_no=False,
                                               deposit_date=todayM,deposit_date_Day=today,deposit_amount=moim_object.deposit_amount)
                        depositinfo.save()

                deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)

            except:
               deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)




        elif arrow == "--":
            year = year
            month = month
            todayM = str(year)+'-'+str(month)
            if month == 13:
                year = year +1
                month = "01"
                todayM = str(year)+'-'+str(month)

            elif month < 10:
                month = "0" + str(month)
                todayM = str(year)+'-'+str(month)

            try:
                user_info_object_moim = user_info.objects.filter(moim_name__moim_name = moim_name)
                for user_info_object_moim_for in user_info_object_moim:
                    try:
                        deposit_info.objects.get(user__username=user_info_object_moim_for.user,moim_name__moim_name = moim_name,deposit_date=todayM)

                    except:
                        moim_object = moim_info.objects.get(moim_name = moim_name)
                        User_object = User.objects.get(username = user_info_object_moim_for.user)
                        User_Info2_object = user_info2.objects.get(user__username = User_object.username)
                        depositinfo = deposit_info(user=User_object,moim_name = moim_object,user_name=User_Info2_object,deposit_yse_no=False,
                                               deposit_date=todayM,deposit_date_Day=today,deposit_amount=moim_object.deposit_amount)
                        depositinfo.save()

                deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)
            except:
               deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)




        elif arrow == "nabu":
            try:
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

                user_deposit_info = deposit_info.objects.get(moim_name__moim_name=moim_name,
                                                             user_name__user_name=name,
                                                             deposit_date=todayM,
                                                             deposit_yse_no=False,
                                                             account_yse_no=False,)
                user_deposit_info.deposit_yse_no=True
                user_deposit_info.save()


            except:
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

                user_name = user_info2.objects.get(user_name=name)
                User_id = User.objects.get(username=user_name.user)
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                deposit_amount = Moim_Name.deposit_amount
                depositinfo = deposit_info(user=User_id,moim_name = Moim_Name,user_name=user_name,deposit_yse_no=True,
                                           deposit_date=todayM,deposit_date_Day=today,deposit_amount=deposit_amount)

                depositinfo.save()

        elif arrow == "cancellation":
            try:
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)
                user_deposit_info = deposit_info.objects.filter(moim_name__moim_name=moim_name,
                                                                user_name__user_name=name,
                                                                deposit_date=todayM,
                                                                deposit_yse_no=True,
                                                                account_yse_no=False).update(deposit_yse_no=False)

            except:
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

                user_name = user_info2.objects.get(user_name=name)
                User_id = User.objects.get(username=user_name.user)
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                deposit_amount = Moim_Name.deposit_amount
                depositinfo = deposit_info(user=User_id,moim_name = Moim_Name,user_name=user_name,deposit_yse_no=True,
                                           deposit_date=todayM,deposit_date_Day=today,deposit_amount=deposit_amount)
                # depositinfo.save()

        elif arrow == "notice_reg": #A02
            try:
                today = str(date.today())
                title_val = request.POST.get('notice_reg_title_input')
                textarea_val = request.POST.get('notice_reg_paticle_textarea')
                user_id = request.user
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                #return HttpResponse(textarea_val + title_val) 확인
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

                User_id = User.objects.get(username=request.user)
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                notices = notice(user_id=User_id,moim_name = Moim_Name,notice_title=title_val,notice_textarea=textarea_val,
                                 notice_date=todayM)
                notices.save()

            except:

                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

        #######################################add_money 추가수입###########################
        elif arrow == "add_moeny_reg": #추가수입 등록
            try:
                title_val = request.POST.get('add_moeny_reg_title_input')
                textarea_val = request.POST.get('add_money_reg_paticle_textarea')
                add_money_val_str = request.POST.get('add_money_reg_money_input')
                add_money_val = int(add_money_val_str)
                #return HttpResponse(textarea_val + title_val) 확인
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                add_money_object_create = add_money(moim_name = Moim_Name,add_money_title=title_val,add_money_textarea=textarea_val,
                                                    add_money_date=todayM,
                                                    add_money = add_money_val)
                add_money_object_create.save()

            except:
                    todayM = str(year)+'-'+str(month)

        elif arrow == "add_money_reg_mod": #추가수입 수정
            try:
                pk1 = request.POST.get('pk')
                title_val = request.POST.get('add_money_reg_mod_title_input')
                textarea_val = request.POST.get('add_money_reg_mod_paticle_textarea')
                money_val = int(request.POST.get('add_money_reg_mod_money_input'))

                add_money.objects.filter(pk=pk1).update(add_money=money_val,add_money_title=title_val,add_money_textarea=textarea_val)

            except:
                return HttpResponse('notice_reg_mod error')

        elif arrow == 'add_money_reg_del': #추가수입 삭제
            try:
                pk1 = request.POST.get('pk')
                add_money.objects.filter(pk=pk1).delete()
                #return HttpResponse(pk1 + "추가수입 삭제 성공")

            except:
                return  HttpResponse('공지삭제 익셉트')
        ###############################################################################################

        #######################################consume_money 지출관련###########################
        elif arrow == "consume_moeny_reg":
            try:
                title_val = request.POST.get('consume_moeny_reg_title_input')
                textarea_val = request.POST.get('consume_money_reg_paticle_textarea')
                img_val = request.FILES['consume_money_reg_img_input']
                add_money_val_str = request.POST.get('consume_money_reg_money_input')
                add_money_val = int(add_money_val_str)
                #return HttpResponse(textarea_val + title_val) 확인
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                consume_money_object_create = withdraw_info(moim_name = Moim_Name,withdraw_title=title_val,withdraw_textarea=textarea_val,
                                                            withdraw_date=todayM,
                                                            withdraw_money = add_money_val,
                                                            receipt_img= img_val)
                consume_money_object_create.save()

            except:
                title_val = request.POST.get('consume_moeny_reg_title_input')
                textarea_val = request.POST.get('consume_money_reg_paticle_textarea')
                add_money_val_str = request.POST.get('consume_money_reg_money_input')
                add_money_val = int(add_money_val_str)
                #return HttpResponse(textarea_val + title_val) 확인
                Moim_Name = moim_info.objects.get(moim_name=moim_name) #모임이름
                consume_money_object_create = withdraw_info(moim_name = Moim_Name,withdraw_title=title_val,withdraw_textarea=textarea_val,
                                                            withdraw_date=todayM,
                                                            withdraw_money = add_money_val,
                                                            receipt_img= None)
                consume_money_object_create.save()


        elif arrow == "consume_money_reg_mod": #추가수입 수정
            try:
                pk1 = request.POST.get('pk')
                title_val = request.POST.get('consume_money_reg_mod_title_input')
                textarea_val = request.POST.get('consume_money_reg_mod_paticle_textarea')
                money_val = int(request.POST.get('consume_money_reg_mod_money_input'))

                withdraw_info.objects.filter(pk=pk1).update(withdraw_money=money_val,withdraw_title=title_val,withdraw_textarea=textarea_val)

            except:
                return HttpResponse('consume_reg_mod error')

        elif arrow == 'consume_money_reg_del': #추가수입 삭제
            try:
                pk1 = request.POST.get('pk')
                withdraw_info.objects.filter(pk=pk1).delete()
                #return HttpResponse(pk1 + "추가수입 삭제 성공")

            except:
                return  HttpResponse('지출삭제 익셉트')
        ###############################################################################################

        ####################################공지사항############################
        elif arrow == "notice_reg_mod": #공지사항 수정
            try:
                pk1 = request.POST.get('pk')
                title_val = request.POST.get('notice_reg_mod_title_input')
                textarea_val = request.POST.get('notice_reg_mod_paticle_textarea')
                notice.objects.filter(pk=pk1).update(notice_title=title_val,notice_textarea=textarea_val)

            except:
                return HttpResponse('notice_reg_mod error')

        elif arrow == 'notice_reg_del': #공지사항 삭제
            try:
                pk1 = request.POST.get('pk')
                notice.objects.filter(pk=pk1).delete()
                #return HttpResponse(pk1 + "공지삭제 성공")

            except:
                return  HttpResponse('공지삭제 익셉트')
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)
        ####################################공지사항############################


        ####################################입금액/입금날짜 수정##################
        elif arrow == "mod_arrow": #수정
            try:
                pk1 = request.POST.get('mod_pk')
                mod_day = request.POST.get('mod_day')
                mod_amount_input = request.POST.get('mod_amount_input')
                deposit_info.objects.filter(pk=pk1).update(deposit_date_Day = mod_day,deposit_amount=mod_amount_input)

            except:

                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)

        elif arrow == "mod_arrow_del": #삭제
            try:
                pk1 = request.POST.get('mod_pk')
                deposit_info.objects.filter(pk=pk1).update(deposit_yse_no=False)

            except:
                return HttpResponse('dd')
                year = year
                month = month
                todayM = str(year)+'-'+str(month)
                if month == 13:
                    year = year +1
                    month = "01"
                    todayM = str(year)+'-'+str(month)

                elif month < 10:
                    month = "0" + str(month)
                    todayM = str(year)+'-'+str(month)
        ####################################입금액/입금날짜 수정##################


        try:
            ############################수입관련####################################################
            try:
                add_money_object = add_money.objects.filter(moim_name__moim_name=moim_name,add_money_date=todayM).order_by('-pk')
            except:
                add_money_object = ''
            #######################################################################################

            ############################지출관련####################################################
            try:
                consume_money_object = withdraw_info.objects.filter(moim_name__moim_name=moim_name,withdraw_date=todayM).order_by('-pk')
            except:
                return HttpResponse('추가수입등록ex')
                consume_money_object = ''
                #return HttpResponse('add_money_no_object')
            #######################################################################################


            deposit_info_object = deposit_info.objects.filter(moim_name__moim_name = moim_name, deposit_date = todayM)
            moim_info00 = moim_info.objects.get(moim_name=moim_name) #잘못된 모임이름이 들어왔을 때 오류
            Notice_info = notice.objects.filter(moim_name__moim_name=moim_name).exclude(notice_date=None).order_by('-pk')
            ###############################################금액리스트#########################################
            moim_money_oj = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=True)
            moim_money_oj_month = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=True, deposit_date=todayM)#돈계산
            moim_money_oj_month_no_money_count_filter = deposit_info.objects.filter(moim_name__moim_name=moim_name, deposit_yse_no=False, deposit_date=todayM)

            moim_money_oj_add_month = add_money.objects.filter(moim_name__moim_name=moim_name, add_money_date=todayM)#돈계산
            moim_money_oj_add_month_total = add_money.objects.filter(moim_name__moim_name=moim_name)

            moim_money_oj_consume_month = withdraw_info.objects.filter(moim_name__moim_name=moim_name, withdraw_date=todayM)#돈계산
            moim_money_oj_consume_month_total = withdraw_info.objects.filter(moim_name__moim_name=moim_name)

            add_money_count = moim_money_oj_add_month.count()
            consume_money_count = moim_money_oj_consume_month.count()
            no_money_count = moim_money_oj_month_no_money_count_filter.count()


            total_money = Moim_Info.moim_total_money
            month_money = 0
            month_add_money = 0
            month_consume_money = 0
            total_month_money_plus_add_money = 0

            for moim_money in moim_money_oj:
                total_money = total_money + moim_money.deposit_amount

            for moim_money_month_add_total in moim_money_oj_add_month_total:
                total_money = total_money + moim_money_month_add_total.add_money

            for moim_money_month_consume_total in moim_money_oj_consume_month_total:
                total_money = total_money - moim_money_month_consume_total.withdraw_money

            for moim_money_month in moim_money_oj_month:
                month_money = month_money + moim_money_month.deposit_amount

            for moim_money_month_add in moim_money_oj_add_month:
                month_add_money = month_add_money + moim_money_month_add.add_money

            for moim_money_month_consume in moim_money_oj_consume_month:
                month_consume_money = month_consume_money + moim_money_month_consume.withdraw_money

            Moim_Info.moim_total_money2 = total_money
            Moim_Info.save()
            total_month_money_plus_add_money = (month_money + month_add_money)-month_consume_money

            ########################################################################################


            user_deposit_info = deposit_info.objects.filter(moim_name__moim_name=moim_name,deposit_date=todayM)
            user_deposit_info2 = deposit_info.objects.filter(moim_name__moim_name=moim_name)
            User_info = user_info.objects.filter(moim_name__moim_name=moim_name) #모임이름으로 필터링
            User_info_user = user_info.objects.filter(user=request.user)
            for user_Info_for in User_info:
                if user_Info_for.manager == True and user_Info_for.user == request.user:
                    manager = 'True'

                elif user_Info_for.user == request.user:
                    user = 'True'

                elif user_Info_for.user != request.user:
                    notuser = 'True'


        except:
            Notice_info = ''




    return render(
        request,
        'moim_detail.html',
        {
            #'form': edit_form,
            #    'total_money':total_money,
            'month_consume_money':month_consume_money,
            'no_money_count':no_money_count,
            'consume_money_count':consume_money_count,
            'add_money_count':add_money_count,
            'consume_money_object':consume_money_object,
            'month_plus_add_money':total_month_money_plus_add_money,
            'add_money_month':month_add_money,
            'add_moeny_object':add_money_object,
            'deposit_infor':deposit_info_object,
            'month_money':month_money,
            'deposit_amount':moim_info00,
            'notice_info' : Notice_info,
            'moim_info':Moim_Info,
            'TodayM':todayM,
            'year' : year,
            'month' : month,
            'user_deposit_info2':user_deposit_info2,
            'user_deposit_info' : user_deposit_info,
            'Manager' : manager,
            'User' : user,
            'NotUser' : notuser,
            'moim_name': moim_name,
            'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )


def user_deposit(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == 'GET':

        a = request.GET.get('detail_user')
        b = request.GET.get('detail_user_name')
        c = request.GET.get('detail_moim_name')
        edit_form = User_Deposit()

    elif request.method =="POST":

        # a = request.POST.get('detail_user')
        b = request.POST.get('detail_user_name')
        # c = request.POST.get('detail_moim_name')
        # edit_form = User_Deposit({'deposit_name' : b,'deposit_amount':40000})

    return render(
        request,
        'user_deposit.html',
        {
            'form' : edit_form,
            'detail_user':a,
            'detail_user_name':b,
            'detail_moim_name':c,

        }
    )


from but_moim.forms import Moim_join_Form
def moim_join(request): #모임등록
    today = str(date.today())
    todayM = today[0:7]
    request_year = todayM[0:4]
    request_month = todayM[5:]
    year = request_year
    month = request_month
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        currunt_user = request.user
        edit_form = Moim_join_Form()


    elif request.method =="POST":

        try:
            Moim_symbol = request.FILES.get('moim_symbol')
        except:
            Moim_symbol = None

        edit_form = Moim_join_Form(request.POST, request.FILES)

        if edit_form.is_valid():
            User_info = user_info.objects.filter(user = request.user)
            new_moim = edit_form.save(commit=False)
            new_moim.user = request.user
            new_moim.save()

            user = get_object_or_404(User, username=request.user)
            User_info2 =user_info2.objects.get(user=request.user)
            #tel = user_info.objects.get(user=request.user)
            Moim_Name = moim_info.objects.get(moim_name=new_moim.moim_name) # 중요 fk의경우 상위모델의 인스턴스를 만들고 그 변수를 사용한다.
            moim_info.objects.filter(moim_name=new_moim.moim_name).update(moim_symbol = Moim_symbol)
            userinfo = user_info(moim_name = Moim_Name,user_name=User_info2.user_name,tel=User_info2.tel,user=request.user,manager=True)
            depositinfo = deposit_info(moim_name = Moim_Name,user_name=User_info2,user=request.user,
                                       account_yse_no=False,
                                       deposit_date=todayM,
                                       deposit_date_Day=today,
                                       deposit_yse_no=False,
                                       deposit_amount=Moim_Name.deposit_amount)
            notice_info = notice(moim_name = Moim_Name,user_id=request.user,notice_title='신규모임default')#신규 모임 생성시 공지사항 오브젝트 생성
            userinfo.save()
            depositinfo.save()
            notice_info.save()

            try:
                Moim_info = moim_info.objects.all()
                User_info_all = user_info.objects.all()
                User_info2_all = user_info2.objects.get(user=request.user)
                User_info = user_info.objects.filter(user = request.user)

                return render(
                    request,
                    'moim_list.html',
                    {
                        #'form': edit_form,
                        'moim_info': Moim_info,
                        'moim_name': User_info_all,
                        'user_infor2_all': User_info2_all,
                        'user_name': user,
                        'user_info': User_info,
                        #'moim_name' :Moim_list,
                    }

                )

            except:
                print("nono")

    return render(
        request,
        'moim_join.html',
        {
            'form': edit_form,
        }

    )


from but_moim.forms import MoimSearchForm
def moim_search(request): #모임검색
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        edit_form = MoimSearchForm()

    elif request.method =="POST":
        edit_form = MoimSearchForm(request.POST)

        if edit_form.is_valid():
            search_form = edit_form.cleaned_data['search_name']
            search = moim_info.objects.filter(moim_name__contains=search_form)
            return render(
                request,
                'moim_search.html',
                {
                    'search': search,
                    'form': edit_form,
                    #'moim_name': moim_name,
                    #'user_info': User_info,
                    #'moim_name' :Moim_list,
                }
            )
    return render(
        request,
        'moim_search.html',
        {
            'form': edit_form,
            #'moim_name': moim_name,
            #'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )

def moim_search_join(request,moim_name): #모임검색 등록 여기
    today = str(date.today())
    todayM = today[0:7]
    request_year = todayM[0:4]
    request_month = todayM[5:]
    year = request_year
    month = request_month

    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        Moim_info = moim_info.objects.get(moim_name=moim_name)
        User_info = user_info.objects.filter(moim_name__moim_name=moim_name)

        for user in User_info:

            if user.user == request.user:
                return HttpResponse('<p>이미 가입되어있습니다.</p>'
                                    "<a href ='/moim_list/'>리스트로</a>")

        user = get_object_or_404(User, username=request.user)
        User_info2 = user_info2.objects.get(user=request.user)
        Moim_Name = moim_info.objects.get(moim_name=moim_name)
        userinfo = user_info(moim_name = Moim_Name,user_name=User_info2.user_name,tel=User_info2.tel,
                             user=request.user)
        depositinfo = deposit_info(moim_name = Moim_Name,user_name=User_info2,
                                   user=request.user,
                                   deposit_yse_no=False,
                                   account_yse_no=False,
                                   deposit_date=todayM,
                                   deposit_date_Day=today,
                                   deposit_amount = Moim_Name.deposit_amount)
        a = moim_info.objects.get(moim_name = moim_name)
        b = a.moim_person_count
        moim_info.objects.filter(moim_name=moim_name).update(moim_person_count = b + 1)
        #moiminfo.save()
        userinfo.save()
        depositinfo.save()


        #Moim_list = User_info.moim_name.filter(user=request.user)
        #moim_list = Moim_list.get().moim_name
    return HttpResponseRedirect(
        reverse("moim_list")
    )







