"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # admin을 제외한 나머지는 blog.urls로 가도록 하라.
    # include뒤에 작성하는 것은 모듈명을 뜻하는 것, 즉 blog라는 패키지 안에 들어있는 urls 모델을 사용하라.
    # 여기서 include는 blog.urls로 그대로 들어가 blog.urls에 있는 정규표현식을 적용한다.
    url(r'', include('blog.urls'))
]