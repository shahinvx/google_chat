from functools import wraps
from django.shortcuts import redirect

def usertype_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        print("request.user----------------->",request.user)
        return func(*args, **kwargs)
    return wrapper

def if_log_then_go(my_view):
    def check_authenticate(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return my_view(request, *args, **kwargs)
    return check_authenticate

def my_permission_chk(prem_str):
    def view_para(my_view):
        def check_permission(request, *args, **kwargs):
            if request.user.has_perm(prem_str):
                return my_view(request, *args, **kwargs)
            else:
                print("\t\t\t\t ",request.user," No Permission")
                #def list(self, request, *args, **kwargs):
                #    return Response({"error":"You has no Permission."})
                return redirect('User Log-In') # worked
                #def get(self):
                #    return Response({"error":"You has no Permission."})
        return check_permission
    return view_para
