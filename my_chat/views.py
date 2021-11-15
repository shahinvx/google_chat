from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User, Group, Permission
# Decorators
from common_utils.decorators import if_log_then_go, my_permission_chk
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import authenticate, login, logout

# http://127.0.0.1:8000/chat/
@method_decorator(login_required(login_url='Home_Login'), name='dispatch')
class Chat_Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_home.html'

    def get(self, request, format=None):
        context = {'Text': 'Chat Home'}
        return Response(context)


# http://127.0.0.1:8000/chat/room_name
@method_decorator(login_required(login_url='Home_Login'), name='dispatch')
class Chat_Room(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_ui.html' #'chat_group.html'

    def get(self, request, *args, **kwargs):
        my_user = User.objects.all()
        context = {'Text': 'Chat Room', 'room_name':kwargs['room_name'],'my_user':my_user}
        return Response(context)

# http://127.0.0.1:8000/chat/ui/chat_ui
class Chat_Ui(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_ui.html'

    def get(self, request, format=None):
        
        context = {'Text': 'Chat Home'}
        return Response(context)

# def Chat_Room(request, room_name):
#     return render(request, 'chat_group.html',{
#         'Text':'Chat Room',
#         'room_name':room_name,
#     })
