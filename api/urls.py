from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from . import transaction
from . import kyc
from . import aml
router = routers.DefaultRouter()
# router.register(r'swaps', views.SwapViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/worker/', include('django_rq.urls')),
    path('api/v1/kyc/tx/',kyc.insertKYCInfoToDb),
    path('api/v1/new/tx/',transaction.send_tx),
    path('api/v1/get/swaps/', transaction.get_swaps),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/aml/',aml.insertAMLInfo),
]