from django.shortcuts import render,redirect
from django.views import View

from .models import Message
from .form import MessageForm
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        
        if not form.is_valid():
            print("バリデーションNG")
            errors = form.errors
            print(errors)
            
            return render(request, 'index.html', {"error": errors})
        
        print("バリデーションOK")
        form.save()
        
        return redirect('message:index')
    
index = IndexView.as_view()