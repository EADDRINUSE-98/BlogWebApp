from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.cache import cache


class SimpleRateLimitor(MiddlewareMixin):
    def __init__(self):
        super().__init__()
        self.TIMEOUT_SEC = 60
        self.REQ_LIMIT = 100

    def get_response(self, request):
        """
        Rate limiting logic.
        """
        ip = self.__get_request_origin_ip(request)
        key = f"rate_limit:{ip}"
        req_count = cache.get(
            key, 0
        )  # 0 is default returned value if nothing is stored for that key.
        if req_count >= self.REQ_LIMIT:
            return JsonResponse({"error": "Request limit exceeded"}, status=429)
        cache.set(key, req_count + 1, timeout=self.TIMEOUT_SEC)

    def __get_request_origin_ip(self, request):
        """
        Extracts origin IP from XFF header.
        """
        xff_header = request.header.get("x-forwarded-for")
        if xff_header:
            ip_list = [ip.strip() for ip in xff_header.split(",")]
            return ip_list[0]
        return request.META.get("REMOTE_ADDR")
