# from django.core.paginator import Paginator
# from django.shortcuts import render
# from contact.models import Visitor
#
# import pygeoip
# import socket
# import requests
#
# gip = pygeoip.GeoIP('GeoLiteCity.dat')
#
#
# # Create your views here.
# def get_client_ip(request):
#     hostname = socket.gethostname()
#     ip_request = requests.get('https://get.geojs.io/v1/ip.json')
#     my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
#     res = gip.record_by_addr(my_ip)
#     try:
#         get_ip = Visitor()
#         get_ip.ip_address = my_ip
#         get_ip.longitude = res.get("longitude")
#         get_ip.latitude = res.get("latitude")
#         get_ip.visitor_name = hostname
#         get_ip.save()
#         return None
#     except:
#         return None
#
#
# def index(request):
#     get_client_ip(request)
#     return render(request, "index.html")
#
#
# def contact_person_view(request):
#     data = Visitor.objects.all()
#     paginator = Paginator(data, 20)
#     page = request.GET.get('page')
#     data = paginator.get_page(page)
#
#     context = {
#         'objects': data
#
#     }
#
#     return render(request, "contact_person_form.html", context)

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Visitor
import pygeoip
import socket
import requests
from .utils import get_client_ip

gip = pygeoip.GeoIP('GeoLiteCity.dat')



# def get_client_ips(request):
#     ip_request = requests.get('https://get.geojs.io/v1/ip.json')
#     my_ip = ip_request.json()['ip']
#     res = gip.record_by_addr(my_ip)
#     get_ip = Visitor()
#     get_ip.ip_address = my_ip
#     get_ip.dma_code = res.get("dma_code")
#     get_ip.area_code = res.get("area_code")
#     get_ip.metro_code = res.get("metro_code")
#     get_ip.postal_code = res.get("postal_code")
#     get_ip.country_code = res.get("country_code")
#     get_ip.country_code3 = res.get("country_code3")
#     get_ip.country_name = res.get("country_name")
#     get_ip.continent = res.get("continent")
#     get_ip.region_code = res.get("region_code")
#     get_ip.city = res.get("city")
#     get_ip.longitude = res.get("longitude")
#     get_ip.latitude = res.get("latitude")
#     get_ip.time_zone = res.get("time_zone")
#     get_ip.save()
#     print(res)
#     return None


def index(request):

    try:
        my_ip = get_client_ip(request)
        get_ip = Visitor()
        get_ip.ip_address = my_ip
        res = gip.record_by_addr(my_ip)
        get_ip.dma_code = res.get("dma_code")
        get_ip.area_code = res.get("area_code")
        get_ip.metro_code = res.get("metro_code")
        get_ip.postal_code = res.get("postal_code")
        get_ip.country_code = res.get("country_code")
        get_ip.country_code3 = res.get("country_code3")
        get_ip.country_name = res.get("country_name")
        get_ip.continent = res.get("continent")
        get_ip.region_code = res.get("region_code")
        get_ip.city = res.get("city")
        get_ip.longitude = res.get("longitude")
        get_ip.latitude = res.get("latitude")
        get_ip.time_zone = res.get("time_zone")
        get_ip.save()
        return render(request, "index.html")
    except:
        return render(request, "index.html")


def contact_person_view(request):
    data = Visitor.objects.all()

    paginator = Paginator(data, 20)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    context = {
        'objects': data

    }

    return render(request, "contact_person_form.html", context)
