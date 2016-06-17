from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ice_cream/home_page.html')),
    url(r'^order/$', views.OrderView.as_view(template_name='ice_cream/order.html')),
    url(r'^order/success/$', TemplateView.as_view(template_name='ice_cream/success.html')),
    url(r'^options/flavors/$', views.FlavorView.as_view(), name='flavor_view'),
    url(r'^options/toppings/$', views.ToppingView.as_view(), name='topping_view'),
    url(r'^options/containers/$', views.ContainerView.as_view(), name='container_view'),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



