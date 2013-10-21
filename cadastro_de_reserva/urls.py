from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cadastro_de_reserva.views.home', name='home'),
    # url(r'^cadastro_de_reserva/', include('cadastro_de_reserva.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^cpf-form/$', 'reservas.views.cpf_form'),
    url(r'^cadastro/$', 'reservas.views.cadastro'),
)
