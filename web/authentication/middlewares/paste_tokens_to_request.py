from django.utils.deprecation import MiddlewareMixin


class GetAccessAndRefreshTokensFromCookies(MiddlewareMixin):
    def process_request(self, request) -> None:
        access = request.COOKIES.get("access_token")
        refresh = request.COOKIES.get("refresh_token")

        if not access and not refresh:
            access = request.session.get("access_token")
            refresh = request.session.get("refresh_token")

        if access and refresh:
            request.access_token = access
            request.refresh_token = refresh
        elif access:
            request.access_token = access
        elif refresh:
            request.refresh_token = refresh
        else:
            pass