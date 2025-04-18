from django.http.response import HttpResponse

# TODO доделать добавление токенов в куки

class SetAccessAndRefreshTokensMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        response: HttpResponse = self.get_response(request)

        if hasattr(response, "data") and ('access' in response.data and 'refresh' in response.data):
            access, refresh = response.data.pop('access', None), response.data.pop("refresh", None)

            if access and refresh:

                request.session["access_token"] = access
                request.session["refresh_token"] = refresh

                response.set_cookie(
                    key="access_token",
                    value=access,
                    secure=True,
                    httponly=True,
                    samesite='lax',
                    max_age=60 
                )

                response.set_cookie(
                    key="refresh_token",
                    value=refresh,
                    secure=True,
                    httponly=True,
                    samesite='lax',
                    max_age=60*2
                )

        return response