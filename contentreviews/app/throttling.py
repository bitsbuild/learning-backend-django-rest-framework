from rest_framework.throttling import UserRateThrottle
class ContentThrottle(UserRateThrottle):
    pass
class ReviewThrottle(UserRateThrottle):
    pass
class PlatformThrottle(UserRateThrottle):
    pass
class ArtistsThrottle(UserRateThrottle):
    pass