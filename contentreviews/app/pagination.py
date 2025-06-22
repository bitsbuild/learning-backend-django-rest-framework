from rest_framework.pagination import PageNumberPagination
class ContentsPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p' instead of page= we do p= in url to access page
    page_size_query_param = 'size'
    max_page_size = 30
    last_page_strings = 'end'
    invalid_page_message = 'Invalid Page Selected'
    display_page_controls = True