from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Jitsu, Ninja, Photo

import uuid, boto3 
S3_BASE_URL ='https://s3-us-east-1.amazonaws.com/'
BUCKET='catcollector-avatar-466'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def ninjas_index(request):
  ninjas = Ninja.objects.all()
  return render(request, 'ninjas/index.html', { 'ninjas': ninjas })


def ninjas_detail(request, ninja_id):
  ninja = Ninja.objects.get(id=ninja_id)

  return render(request, 'ninjas/detail.html', {
    'ninja':ninja
  })



def assoc_jitsu(request, ninja_id, jitsu_id):
  # Note that you can pass a toy's id instead of the whole object
  Ninja.objects.get(id=ninja_id).jitsus.add(jitsu_id)
  return redirect('detail', ninja_id=ninja_id)


def add_photo(request, ninja_id):
  # attempt to collect the photo file data
  photo_file = request.FILES.get('photo-file', None)
  # use conditional logic to determine if file is present
  if photo_file:
  # if it's present, we will create a reference the the boto3 client
    s3 = boto3.client('s3')
    # create a unique id for each photo file
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # funny_cat.png = jdbw7f.png
    # upload the photo file to aws s3
    try:
    # if successful
      s3.upload_fileobj(photo_file, BUCKET, key)
      # take the exchanged url and save it to the database
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # 1) create photo instance with photo model and provide cat_id as foreign key val
      photo = Photo(url=url, ninja_id=ninja_id)
      # 2) save the photo instance to the database
      photo.save()
    except Exception as error:
      print("Error uploading photo: ", error)
      return redirect('detail', ninja_id=ninja_id)
    # print an error message
  return redirect('detail', ninja_id=ninja_id)
  # redirect the user to the origin 


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class NinjaCreate(CreateView):
  model = Ninja
  fields = ['name','village', 'description', 'age' ]
  success_url = '/ninjas/'

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

class NinjaUpdate(UpdateView):
  model = Ninja
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['village', 'description', 'age']

class NinjaDelete(DeleteView):
  model = Ninja
  success_url = '/ninjas/'

class JitsuList(ListView):
  model = Jitsu
  template_name = 'jitsus/index.html'

class JitsuDetail(DetailView):
  model = Jitsu
  template_name = 'jitsus/detail.html'

class JitsuCreate(CreateView):
    model = Jitsu
    fields = ['name', 'color', 'type']


class JitsuUpdate(UpdateView):
    model = Jitsu
    fields = ['name', 'color', 'type']


class JitsuDelete(DeleteView):
    model = Jitsu
    success_url = '/jitsus/'