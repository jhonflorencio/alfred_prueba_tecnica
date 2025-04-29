from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, Http404):
            response.data = {'detail': 'El elemento que buscas no se encuentra.'}
            response.status_code = status.HTTP_404_NOT_FOUND

    return response