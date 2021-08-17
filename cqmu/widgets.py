from django.forms.widgets import ClearableFileInput


class FileFieldWidget(ClearableFileInput):
    template_name = 'file.html'
