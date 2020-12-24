"""Demo script."""


class MyAPIClient():
    """Simple api class."""

    def get_user_list(self):
        """Simple get_user_list method."""
        return ["user_id1", "user_id2"]


class View:
    """Simple View class."""

    @classmethod
    def as_view(cls, **initkwargs):
        """Simple as_view method."""
        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            return self.dispatch(request, *args, **kwargs)
        return view

    def dispatch(self, request, *args, **kwargs):
        """Simple dispatch method."""
        handler = getattr(self, "get")
        return handler(request, *args, **kwargs)


class APIView(View):
    """Simple APIView method."""

    @classmethod
    def as_view(cls, **initkwargs):
        """Simple as_view method."""
        view = super().as_view(**initkwargs)
        return view


class MyAPIView(APIView):
    """Sample class."""

    def get(self, request):
        """Get method."""
        my_api_client = MyAPIClient()
        result = my_api_client.get_user_list()
        return result


response = MyAPIView.as_view()
print(type(response))
print(response("some request"))
