from django.shortcuts import render,redirect
from django.views import View

from django.contrib import messages
from .models import Message
from .form import MessageForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        messages = Message.objects.all()
        context = {"comments":messages}
        
        return render(request, "index.html",context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        
        if not form.is_valid():
            print("バリデーションNG")
            errors = form.errors
            print(errors)
            
            messages.error(request, errors)
            #errorsを変数としてtemolateで受け取るためにrenderを使用した
            return redirect("message:index")
        
        print("バリデーションOK")
        form.save()
        
        return redirect('message:index')
    
index = IndexView.as_view()