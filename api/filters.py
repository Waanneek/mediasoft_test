from rest_framework.filters import SearchFilter


class ShopFilter(SearchFilter):

    search_param = ['name', 'city', 'street', 'open']

    def filter_queryset(self, request, queryset, view):

        my_queryset = super().filter_queryset(request, queryset, view)
        param_open = request.query_params.get('open')

        return my_queryset