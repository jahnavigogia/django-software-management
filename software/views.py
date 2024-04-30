from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Software
from .forms import SoftwareForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import hashlib
import logging
from django.db import connection


# Example usage of hashlib for hashing
def hash_data(data):
    # Create a hash object
    hash_object = hashlib.sha256()

    # Update the hash object with data
    hash_object.update(data)

    # Get the hexadecimal digest of the hash
    hash_digest = hash_object.hexdigest()

    return hash_digest


from django.http import JsonResponse
import hashlib


def hash_data_view(request):
    if request.method == 'POST':
        # Assume data is sent in the POST request
        data_to_hash = request.POST.get( 'data', '' )

        # Hash the data
        hashed_data = hash_data( data_to_hash.encode('utf-8'))  # Encode to bytes before hashing

        # Return the hashed data in JSON response
        return JsonResponse( {'hashed_data': hashed_data} )
    else:
        # Method not allowed for other request methods
        return JsonResponse( {'error': 'Method not allowed'}, status=405 )


# Example usage of hash_data function
data_to_hash = b'Hello, world!'  # Data to hash, encoded as bytes
hashed_data = hash_data(data_to_hash)
print("Hashed data:", hashed_data)


def software_list(request):
    software_list = Software.objects.all()
    return render(request, 'software_list.html', {'software_list': software_list})


def add_software(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = SoftwareForm()
    return render(request, 'add_software.html', {'form': form})


def delete_software(request):
    if request.method == 'POST':
        licensee = request.POST.get('license')

        # Query the database to find the software by license number
        try:
            software = Software.objects.get(licensee)
            # Delete the software entry
            software.delete()
            return redirect('software_list')  # Redirect to software list page after deletion
        except Software.DoesNotExist:
            error_message = "Software with license number '{}' does not exist.".format(licensee)
            return render(request, 'del_software.html', {'error_message': error_message})

    return render(request, 'del_software.html')


@login_required
def software_detail(request, name):
    software = get_object_or_404(Software, pk=name)
    if software.is_accessible_by_all or request.user in software.allowed_users.all():
        return render(request, 'software_detail.html', {'software': software})
    else:
        # Return a response indicating permission denied
        return render(request, 'permission_denied.html')


"""def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list.html')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
"""


def home(request):
    return render(request, 'home.html')


def index(request):
    return HttpResponse("Welcome to software management system!")


#def Encryp_tion(request):
    # Create an instance of MyModel with encrypted data
 #   instance = Encryption.objects.create(encrypted_field="Sensitive data")

    # Retrieve the instance and access the decrypted data
  #  decrypted_data = instance.encrypted_field
   # print(decrypted_data)  # Output: Sensitive data

    #return render(request, 'software_list.html')


@login_required
def my_protected_view(request):
    # Your view logic here
    return render(request, 'my_protected_view.html')


class MyProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'my_protected_view.html'


class User_LoginView(LoginView):
    template_name = 'registration/login.html'  # Path to your login template
    authentication_form = AuthenticationForm  # You can use a custom authentication form if needed
    redirect_authenticated_user = True  # Redirects authenticated users to the success_url
    success_url = reverse_lazy('software_list')  # URL to redirect to after successful login


class User_LogoutView(LogoutView):
    class CustomLogoutView(LogoutView):
        next_page = reverse_lazy('home')  # URL to redirect to after logout


class My_Protected_View(LoginRequiredMixin, TemplateView):
    template_name = 'my_protected_view.html'


@login_required
def profile(request):
    # Retrieve user information from the request object
    user = request.user

    # You can pass additional context data if needed
    context = {
        'user': user,
        # Add more context data as needed
    }

    return render(request, 'profile.html', context)


def csrf_failure_view(request, reason=""):
    return HttpResponseForbidden('CSRF verification failed. Please try again.')


logger = logging.getLogger(__name__)


def log(request):
    # Log a specific query
    logger.debug("Executing query: %s", 'SELECT * FROM software_software')

    # Example of using connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM software_software")
        rows = cursor.fetchall()

    return render(request, 'x.html', {'data': rows})


def check_active_connections():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table)



