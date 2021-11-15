from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User, Group, Permission
from django.views.decorators.csrf import csrf_exempt
from my_chat.models import Chat_Groups
from django.shortcuts import redirect
from my_chat.views import *

# Decorators
from common_utils.decorators import if_log_then_go, my_permission_chk
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import authenticate, login, logout

# http://127.0.0.1:8000/accounts/logout/
# http://127.0.0.1:8000/accounts/login/


class Login_Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Home_Login.html'

    def get(self, request, format=None):
        context = {'Text': 'Home Login View'}
        return Response(context)

@method_decorator(login_required(login_url='Home_Login'), name='dispatch')
class Log_Out(APIView):
    def get(self, request, format=None):
        # del request.session['user']
        # request.user.auth_token.delete()
        logout(request)

        return redirect('Home_Login')

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

@method_decorator(login_required(login_url='Home_Login'), name='dispatch')
class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Home.html'

    def get(self, request, format=None):
        try:
            print('User : ', request.user, request.user.id,
                  request.user.email, request.user.username)
        except:
            print('User : ', request.user)

        my_user = User.objects.all()
        context = {'Text': 'Home', 'my_user': my_user}
        return Response(context)
        #return render(request, 'Home.html', context)

    def post(self, request, format=None):
        print('----------------------------------------------- > Post', request.POST.keys(),
              request.POST.get('user_id'), request.POST.get('Do'))

        current_user = request.user.id
        friend_user = int(request.POST.get('user_id'))
        group_name = '_chat_'

        if current_user != friend_user:
            if current_user > friend_user:
                group_name = str(
                    friend_user) + group_name + str(current_user)
            else:
                group_name = str(current_user) + group_name + str(friend_user)
            print(group_name)

        if group_name != '_chat_':
            try:
                chat_group = Chat_Groups.objects.get(name=group_name)
            except:
                chat_group = Chat_Groups(name=group_name)
                chat_group.user_a = current_user
                chat_group.user_b = friend_user
                chat_group.save()
                chat_group = Chat_Groups.objects.get(name=group_name)

            print(
                '------------------------------------------Chat Group Name : ', chat_group.name, type(chat_group.name))

        all_my_user = User.objects.all()

        my_user = []
        for i in all_my_user:
            my_user.append(str(i))
        
        context = {'Text': 'Chat Room', 'room_name':chat_group.name,'my_user':my_user}
        return JsonResponse(context, status=200)
        #response = redirect('/chat/'+chat_group.name)
        #return response
        #return render(response, 'chat_ui.html')
        #return render(request, 'chat_group.html', context)
        # return render(request, 'chat_group.html', context)
        #return redirect('chat_room', room_name=str(chat_group.name)) # W
        # return HttpResponseRedirect(reverse('chat_room', args=[str(chat_group.name)]))  # W
        # context = {'Text': 'Home', 'my_user': my_user}
        #return Response(context)
