from django.utils import translation
from rest_framework import exceptions, request


class LanguageVersionMixin:
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        language_code = request.query_params.get('language')
        if language_code:
            try:
                translation.activate(language_code)
                request.LANGUAGE_CODE = translation.get_language()
            except Exception as e:
                raise exceptions.ValidationError(f"Invalid language code: {e}")




