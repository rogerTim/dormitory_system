# -*- coding: utf-8 -*-
from django.shortcuts import render
from dormitory.models import User_answer, DorArrange, Dormitory, User, Question
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
# Create your views here.


def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects, default=json_serial)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = json.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator


@json_response
def student_login(request):
    """ 学生登录接口
        方式:
            POST
        传参:
            schId: 学号
            pwd: 密码
        返回:
            status: 登录情况 成功返回1 失败返回0
            username: 姓名 失败则不返回
    """
    schId = request.POST.get('schId')
    pwd = request.POST.get('pwd')
    try:
        if pwd == User.objects.get(id=schId).pwd:
            name = User.objects.get(id=schId).name
            # return JsonResponse({'status': 1, 'username': name})
            return {'status': 1, 'username': name}
        else:
            return {'status': 0}
            # return JsonResponse({'status': 0})
    except:
        return {'status': 0}
        # return JsonResponse({'status': 0})


def get_question(request):
    """ 问卷题目
        方式:
            GET
        传参:
        返回:
            status: 1
            data: [{id: 问题编号,question: 内容, options: [选项1, 选项2, ...]},...]
    """
    data = []
    # 将问卷内容全部导出并存在text_dict中
    for each in Question.objects.all():
        question = {}
        question['id'] = each.id
        question['question'] = each.content
        question['options'] = []
        for option in each.option.split('||'):
            option.replace('$', '.')
            question['options'].append(option)
        data.append(question)
    return JsonResponse({'status': 1, 'data': data})


def save_answer(request):
    """ 问卷提交接口
        方式:
            POST
        传参:
            schID: 学号
            answer: 学生提交的问卷, [{id: ?, answer: ?}, ...] answer直接提交选项的内容
        返回:
            status: 提交状态 成功返回1, 错误返回0
    """
    if request.POST.get('schID') and request.POST.get('answer'):
        schID = request.POST['schID']
        answers = request.POST['answer']
        ans = ''
        for answer in answers:
            ans += u'%s$%s||' % (answer['id'], answer['answer'])
        ans.rstrip('||')
        User_answer.object.create(user_id=schID, answer=ans)
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def get_result(request):
    """ 学生查看宿舍分配结果接口
        方式:
            get
        传参:
            schId: 学号
        返回:
            status: 1
            data: {dormitory: 宿舍名,
                   roomates: [{schId: 学号, name: 姓名, major: 专业, hometown: 生源地}, ...]
            }
    """
    if request.GET['schId'] and DorArrange.objects.get('schId'):
        # 学生基本信息
        user_id = request.GET.get('schId')
        dor_id = DorArrange.objects.get(user_id=user_id)

        # 获取所在宿舍
        dor = Dormitory.objects.get(dor_id=dor_id)

        data = {}
        data['dormitory'] = dor.name
        # 获取室友信息
        data['roomates'] = []
        roomates = DorArrange.objects.filter(dor_id=dor_id).exclude(user_id=user_id)
        for mate in roomates:
            mate_id = mate.user_id
            mate = User.objects.get(id=mate_id)
            mate_dict = {}
            mate_dict['schId'] = mate_id
            mate_dict['name'] = mate.name
            mate_dict['major'] = mate.major
            mate_dict['hometown'] = mate.source
            data['roomates'].append(mate_dict)
        return JsonResponse({'status': 1, 'data': data})
    return JsonResponse({'status': 1})


def admin_login(request):
    """ 管理员登录接口
        方式:
            Post
        传参:
            adminId: 管理员id
            pwd: 密码
        返回:
            status: 登录情况 成功返回1, 失败返回0
            username: 用户名 失败则不返回
    """
    if request.POST.get('adminId') and request.POST.get('pwd'):
        admin = User.objects.get(id=request.POST['adminId'])
        if admin and request.POST['pwd'] == admin.pwd and admin.authority:
            return JsonResponse({'status': 1, 'username': admin.name})
        else:
            return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 0})


def percentage(request):
    """ 获取男生填写率和女生填写率(精度为0.1)
        方法:
            GET
        传参:
        返回数据:
            status: '1'
            data:{
                  man: 男生填写率
                  women: 女生填写率
            }
    """
    Users = User.objects.all()
    User_answers = User_answer.objects
    # 男生总数和女生总数
    man_sum = 0
    women_sum = 0
    # 男生填写数和女生填写数
    man_ans = 0
    women_ans = 0

    # 统计数量
    for each in User.objects.all():
        if each.sex == 1:
            man_sum += 1
            if User_answers.get(user_id=each.id):
                man_ans += 1
        else:
            women_sum += 1
            if User_answers.get(user_id=each.id):
                women_ans += 1

    # 计算男生填写率和女生填写率
    man_per = int('%.2f' % (1.0*man_ans/man_sum))
    women_per = int('%.2f' % (1.0*women_ans/women_sum))
    return JsonResponse({'status': 1, 'data': {'man': man_per, 'women': women_per}})


def output_all(request):
    """ 管理员界面导出全部宿舍的接口
        方式:
            GET
        传参:
        返回:
            data:[
                   {id:宿舍编号,dormitory:宿舍名称,roommates:[{schId: id, name: 姓名, major: 专业, hometown: 生源地 },...]}, ...
                 ]
    """
    data = []
    dormitorys = Dormitory.objects
    users = User.objects
    for dormitory in dormitorys:
        room = {}
        room['id'] = dormitory.get('dor_id')
        room['dormitory'] = dormitory.get('name')
        room['roommates'] = []
        for each in [each.user_id for each in DorArrange.objects.fliter(dor_id=room['id'])]:
             roommate = users.get(id=each)
             roommate_dict = {}
             roommate_dict['schId'] = each
             roommate_dict['name'] = roommate.name
             roommate_dict['major'] = roommate.major
             roommate_dict['hometown'] = roommate.source
             room['roommates'].append(roommate)
        data.append(room)
    return JsonResponse({'data': data})


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial[:10]