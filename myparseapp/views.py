from django.shortcuts import render,redirect
from docx import *
from .forms import StudentForm
as1=[]
def upload(request):
  if request.method== "POST":
    f=str(request.FILES['document']).split(".")
    if "docx" in f:
      document=Document(request.FILES['document'])
      l=[]
      for p in document.paragraphs:
        var=""
        line=(p.text).split()
        print(line)
        p=0
        for x in line:
          p+=1
          if(p>2):
            var+=x+ " "
        l.append(var)
      for i in l:
        as1.append(i)
        print(i)
      word={'fname':as1[0],'lname':as1[1],'mail':as1[2],'phno':as1[3],'address':as1[4],'dist':as1[5],'state':as1[6],'pin':as1[7],'education':as1[8],'wstatus':as1[9],'skill':as1[10],'exp':as1[11]}
      if len(as1[0])==0 or len(as1[1])==0 or len(as1[2])==0 or len(as1[3])==0 or len(as1[4])==0 or len(as1[5])==0 or len(as1[6])==0 or len(as1[7])==0 or len(as1[8])==0 or len(as1[9])==0 or len(as1[10])==0 or len(as1[11])==0:
        return render(request,"error.html")
      else:
        return render(request,"resume.html")
      form=StudentForm(word)
      if form.is_valid():
        form.save()
        return redirect("/upload")
    else:
      return render(request,"alertmsg.html")
  return render(request,'upload.html')