from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('frontend/', views.front, name="front"),
    path('backend/', views.back, name="back"),
    path('design/', views.design, name="design"),
    path('other/', views.other, name="other"),
    path('create_article/', views.create_article, name="creatArticle"),
    path('pass_recovery/', views.pass_recovery, name="pass_recovery"),
    path('sich/', views.sich, name="sich"),
    path('lyt/', views.lyt, name="lyt"),
    path('ber/', views.ber, name="ber"),
    path('kvt/', views.kvt, name="kvt"),
    path('trv/', views.trv, name="trv"),
    path('chrv/', views.chrv, name="chrv"),
    path('lpn/', views.lpn, name="lpn"),
    path('srp/', views.srp, name="srp"),
    path('vrs/', views.vrs, name="vrs"),
    path('zhvt/', views.zhvt, name="zhvt"),
    path('lst/', views.lst, name="lst"),
    path('grd/', views.grd, name="grd"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

