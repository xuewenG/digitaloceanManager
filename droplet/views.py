from django.http import JsonResponse, HttpResponse
from django.conf import settings
import requests
# Create your views here.

url = 'https://api.digitalocean.com/v2/droplets'
headers = {
    "Content - Type": "application / json",
    "Authorization": "Bearer " + settings.DO_TOKEN,
}


def get_droplet(request):
    res = requests.get(url, headers=headers)
    return JsonResponse(res.json())


def create_droplet(request):
    payload = {
        "name": "example",
        "region": "sgp1",
        "size": "s-1vcpu-1gb",
        "image": "centos-7-x64",
        "ssh_keys": [settings.SSH_KEY]
    }
    res = requests.post(url, json=payload, headers=headers)
    return JsonResponse(res.json())


def delete_droplet(request):
    tag = request.GET.get('tag')
    if tag is None:
        return HttpResponse('need tag')
    payload = {
        "tag_name": tag,
    }
    res = requests.delete(url, data=payload, headers=headers)
    print(res.headers)
    print(res.status_code)
    return HttpResponse(res.text)
