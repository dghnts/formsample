from django.shortcuts import render,redirect
from django.views import View

from .models import Message
from .form import MessageForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        messages = Message.objects.all()
        context = {"messages":messages}
        
        return render(request, "index.html",context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        
        if not form.is_valid():
            print("バリデーションNG")
            errors = form.errors
            print(errors)
            
            #errorsを変数としてtemolateで受け取るためにrenderを使用した
            return render(request, 'index.html', {"error": errors})
        
        print("バリデーションOK")
        form.save()
        
        return redirect('message:index')
    
index = IndexView.as_view()