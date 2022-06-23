from starlette.datastructures import QueryParams


def get_filter(query_params: QueryParams) -> dict:
    filter = {}
    for key, value in query_params.multi_items():
        if key not in ['name', 'description']:
            key = f'params.{key}'
        filter[key] = value
    return filter
