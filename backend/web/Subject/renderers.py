import json
from rest_framework import renderers


class UserJSONRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        token = data['token']

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode()
        
        return json.dumps({
            "user": data
        })