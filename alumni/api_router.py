from django.urls import path, include

app_name = "api"
# urlpatterns = router.urls
urlpatterns = [
    # Django API
    path('core/', include('core.urls')),
    path('students/', include('students.urls')),
    path('members/', include('members.urls')),
    # path('article/', include('article.urls')),
    # path('committee/', include('committee.urls')),
    # path('careers/', include('careers.urls')),
]
