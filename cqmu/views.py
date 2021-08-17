from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from .models import *


def file_list(request):
    topic_category = TopicCategory.objects.all()
    grade = Grade.objects.all()
    file_category = FileCategory.objects.all()
    if request.GET.get('at', None):
        active_topic = TopicCategory.objects.get(pk=int(request.GET['at']))
        file_upload_list = FileUpload.objects.filter(topic_category=active_topic)[:1]
    else:
        active_topic = None
        file_upload_list = FileUpload.objects.all()[:1]
    context = {
        'file_upload_list': file_upload_list,
        'grade': grade,
        'file_category': file_category,
        'topic_category': topic_category,
        'active_topic': active_topic
    }
    return render(request, 'cqmu/file_list.html', context)


def file_detail(request, file_upload_id):
    topic_category = TopicCategory.objects.all()
    file = get_object_or_404(FileUpload, pk=file_upload_id)
    if request.method == 'POST':
        Comment.objects.create(
            label=request.POST.get('label', None),
            nickname=request.POST['nickname'],
            scoring=request.POST['scoring'],
            file_upload=file
        )
    comments = Comment.objects.filter(file_upload=file_upload_id, label__isnull=False)[:10]
    context = {
        'file': file,
        'form': file.file_category.form,
        'comments': comments,
        'scoring': Comment.Scoring,
        'topic_category': topic_category,
        'active_topic': file.topic_category
    }
    return render(request, 'cqmu/file_detail.html', context)


def params_decorator(function):
    def wrap(*args, **kwargs):
        request = args[0]
        try:
            int(request.GET.get('page', 1))
        except Exception as e:
            return JsonResponse(status=400, data={'error': str(e)})
        result = function(*args, **kwargs)
        return result
    return wrap


def calc_pages(request, file_upload_list):
    cp = settings.COP
    p = int(request.GET.get('page', 1))
    sp = cp * (p-1)
    ep = sp + cp
    pages = (file_upload_list.count()/cp) + 1
    return sp, ep, pages


@params_decorator
def file_list_json(request):
    file_upload_list = FileUpload.objects.all()
    kwargs_dict = {}
    key_filter = {
        'at': 'topic_category',
        'grade': 'grade',
        'file_category': 'file_category',
        'date_min': 'release_date__gte',
        'date_max': 'release_date__lte'
    }
    for g in request.GET:
        if request.GET.get(g, None) and g in ['at', 'grade', 'file_category', 'date_min', 'date_max']:
            kwargs_dict[key_filter[g]] = request.GET.get(g)
    if request.GET.get('search_field', None) and request.GET.get('search_field_value', None):
        kwargs_dict['{}__contains'.format(request.GET.get('search_field'))] = request.GET.get('search_field_value')
    file_upload_list = file_upload_list.filter(**kwargs_dict)
    sp, ep, pages = calc_pages(request, file_upload_list)
    file_upload_list = file_upload_list[sp:ep]
    file_list_data = []
    for f in file_upload_list:
        fd = {
            'label': f.label,
            'author': f.author,
            'presenter': f.presenter,
            'description': f.description,
            'data_source': f.data_source,
            'comment_scoring': str(f.comment_scoring),
            'downloads': f.downloads,
            'file': f.file.name,
            'file_category': f.file_category.icon,
            'grade': f.grade.label,
            'recommended_tag': f.recommended_tag,
            'release_date': f.release_date,
            'topic_category': f.topic_category.label,
            'url': f.url,
            'visits': f.visits,
            'id': f.id
        }
        file_list_data.append(fd)
    data = {
        'pages': pages,
        'data': file_list_data,
    }
    return JsonResponse(data)
