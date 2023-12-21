from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import FormView
from .models import Content
from album.forms import ContentForm


def album_index(request):
    return render(request, "index.html")


# basic view to allow uploading photos/videos to the site.
# this will eventually be private to only certain roles.
class UploadFileView(FormView):
    form_class = ContentForm
    template_name = "upload.html"  # Replace with your template.
    success_url = "upload"  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["files_field"]
        for f in files:

            # get data
            owner = form.cleaned_data['owner_field']
            description = form.cleaned_data['description_field']
            create_date = form.cleaned_data['create_date_field']
            public = form.cleaned_data['public_field']

            # fill in and persist object
            content_object = Content()
            content_object.owner = owner
            content_object.description = description
            content_object.created_at = create_date
            content_object.document = f
            content_object.public = public
            content_object.save()

        return super().form_valid(form)
