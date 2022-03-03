from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Answer
import json
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'research_site/user_info.html')


def user_info(request):
    # request.session['page'] = 1
    # page = request.session['page']+1
    page = 1
    '''
    user_name = request.POST.get('user_name')
    user_grade = request.POST.get('user_grade')
    user_age = request.POST.get('user_age')

    if user_grade == "grade_h":
        grade = 1
    elif user_grade == "grade_m":
        grade = 2
    elif user_grade == "grade_l":
        grade = 3

    #user = User(name=user_name, grade=grade, age=int(user_age))
    #user.save()

    session_id=request.session.session_key
    page=request.session['page']
    #request.session['user_id'] = user.id
'''
    context = {'page': page}

    return render(request, 'research_site/keyword_survey.html', context)


def next_survey(request, page):
    # page+=1
    context = {'page': page}
    return render(request, 'research_site/keyword_survey.html', context)


def prev_survey(request, page):
    # page = request.session['page']
    # page -= 1
    # request.session['page'] = page

    context = {'page': page}
    return render(request, 'research_site/keyword_survey.html', context)

@csrf_exempt
def submit_survey(request):
    # page+=1
    final_data = json.loads(request.POST.get('final_data'))
    print(final_data)
    print(type(final_data))

    user=User()
    user.name=final_data["name"]
    user.age=final_data["age"]
    user.grade=final_data["grade"]
    user.phone=final_data["phone"]
    user.save()


    del(final_data["name"])
    del(final_data["age"])
    del(final_data["grade"])
    del(final_data["phone"])

    font_data=Answer()
    font_data.user=user
    font_data.font_answer=final_data
    font_data.save()

    return render(request, 'research_site/final.html')
