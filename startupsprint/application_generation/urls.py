from django.urls import path
from .views import (
    AllApplicationsView, ApplicationByUserView, ApplicationByIdView,
    DocumentByApplicationView, DocumentByUserView, ServeDocumentView
)

urlpatterns = [
    path('applications/', AllApplicationsView.as_view(), name='all_applications'),
    path('applications/user/<int:user_id>/', ApplicationByUserView.as_view(), name='application_by_user'),
    path('applications/<int:application_id>/', ApplicationByIdView.as_view(), name='application_by_id'),
    path('documents/application/<int:application_id>/', DocumentByApplicationView.as_view(), name='document_by_application'),
    path('documents/user/<int:user_id>/', DocumentByUserView.as_view(), name='document_by_user'),
    path('media/<path:file_path>/', ServeDocumentView.as_view(), name='serve_document'),
]
