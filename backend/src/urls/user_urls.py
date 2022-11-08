from django.urls import path
from src.views import user_views as views

urlpatterns=[
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/',views.getUserProfile,name="user-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('register/',views.registerUser,name='register')
]

