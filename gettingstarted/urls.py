from django.conf.urls import include, url

from django.contrib import admin,auth
admin.autodiscover()

import hello.views
import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registercoder', hello.views.registerCoder, name='registercoder'),
    url(r'^registerhelper', hello.views.registerHelper, name='registerhelper'),
    url(r'^login', hello.views.user_login, name='user_login'),
    url(r'^home', hello.views.post_login, name='post_login'),
    url(r'^invalidlogin', hello.views.invalidLogin, name='invalidLogin'),
    url(r'^skill', hello.views.skill, name='skill'),
    url(r'^viewhelpers', hello.views.viewhelpers, name='viewhelpers'),
    url(r'^helperprofile', hello.views.helperProfile, name='helperProfile'),
    url(r'^editprofile', hello.views.editHelperProfile, name='editHelperProfile'),
    url(r'^test', hello.views.test, name='test'),
    url(r'^sms', hello.views.sms, name='sms'),
    url(r'^msg', hello.views.message, name='message'),
    url(r'^compose', hello.views.compose_message, name='compose_message'),
    url(r'^inbox', hello.views.inbox, name='inbox'),
    url(r'^alreadysent', hello.views.msgsent, name='msgsent'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

