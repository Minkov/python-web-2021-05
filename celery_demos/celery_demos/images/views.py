import os

from celery import current_app
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from celery_demos.images.forms import FileUploadForm
from celery_demos.images.tasks import make_thumbnails

class MyModelForm(....):

    def save(self, ...):
        obj = super().save(...)
        obj.pk


class HomeView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            file_path = os.path.join(settings.IMAGES_DIR, request.FILES['image_file'].name)
            with open(file_path, 'wb+') as fp:
                for chunk in request.FILES['image_file']:
                    fp.write(chunk)
            task = make_thumbnails.delay(file_path, thumbnails=[
                (128, 128),
                (1024, 1024),
            ])
            context['task_id'] = task.id
        context['form'] = form
        return render(request, 'home.html', context)


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {
            'task_status': task.status,
            'task_id': task.id
        }
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)
