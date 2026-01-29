from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class WatchlistPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10 
    
class WatchlistLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10  