from transaction import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet, basename='contact'),
router.register(r'transaction', views.TransactionViewSet, basename='transaction'),
router.register(r'payment', views.PaymentViewSet, basename='payment'),



urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('transaction-history/', views.TransactionHistoryView.as_view(), name='transaction-history'),
    path('feedback/',views.FeedbackView.as_view(), name='feedback-list'),
    path('feedbacks/<int:pk>/', views.FeedbackResponseView.as_view(), name='feedback-response'),
    path('upload/excel/', views.ExcelUploadView.as_view(), name='excel-upload'),

]+ router.urls    