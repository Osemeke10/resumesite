from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
# from .form import ContactForm



def home(request):
	# form = ContactForm()
	if request.method=='POST':
		print(request.POST)
	context = {'form':form}


	return render(request,'home.html', context)
	# if request.method =='POST':

# def home(request):
# 	form =ContactForm()
# 	if request.method=='POST':
# 		print(request.POST)
# 	context = {'form':form}
# 	return render(request,'resume.html', context)

# some_variable_name=TemplateResponse(request,'resumesite.html',context)
#  return some_variable_name
		
	# 	name = request.POST['name']
	# 	email = request.POST['email']
	# 	phone = request.POST['phone']
	# 	message = request.POST['message']
	# 	print(name, email, phone,message)

	
	




# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             Name = form.cleaned_data['Name']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             phone = form.cleaned_data['phone']
#             try:
#                 resumesite(Name, message, from_email,phone, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "Home.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')















# Create your views here.
def home(request):
	if request.method =='POST':
		
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		print(name, email, phone,message)

	
	return render(request,'home.html',{})

# def contact(request):
# 	if request.method =='POST':
		
# 		name = request.POST('name')
# 		email = request.POST('email')
# 		phone = request.POST['phone']
# 		print('name, email, phone')
# 	return render(request, 'home.html')
