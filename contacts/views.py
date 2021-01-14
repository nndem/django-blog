from django.shortcuts import render

# Create your views here.
def my_contacts(request):
	return render(request, 'contacts/my_contacts.html')