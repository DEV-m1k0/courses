from django.utils.deprecation import MiddlewareMixin


class GetAccessAndRefreshTokensFromCookies(MiddlewareMixin):
    # def process_request(self, request) -> None:
    #     access = request.COOKIES.get("access_token")
    #     refresh = request.COOKIES.get("refresh_token")

    #     if not access and not refresh:
    #         access = request.session.get("access_token")
    #         refresh = request.session.get("refresh_token")

    #     if access and refresh:
    #         request.access_token = access
    #         request.refresh_token = refresh
    #     elif access:
    #         request.access_token = access
    #     elif refresh:
    #         request.refresh_token = refresh
    #     else:
    #         pass

    def __init__(self, get_response):
        # super().__init__(get_response)

        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        access_token = response.cookies.get("access_token", None)
        refresh_token = response.cookies.get("refresh_token", None)

        if access_token and refresh_token:
            request.session['access_token'] = access_token
            request.session["refresh_token"] = refresh_token
        elif refresh_token:
            request.session["refresh_token"] = refresh_token
        elif access_token:
            request.session['access_token'] = access_token
        else:
            pass

        # print("tokens were added to request")

        return response
