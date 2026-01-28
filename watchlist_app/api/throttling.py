from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
    # rate = '1/day'

    
    
class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'
    # rate = '5/day'
