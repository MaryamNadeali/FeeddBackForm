from django.urls import path
from .views import FeedbackFormView, RegisterView, LoginView

app_name = 'Feedback'

urlpatterns = [
    
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("feedbackform/", FeedbackFormView.as_view(), name='feedbackform'),
]
