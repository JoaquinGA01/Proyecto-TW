"""System module."""
from bson.objectid import ObjectId

async def paggination(
		collection: str, skip: int = 0, limit: int = 20, filter_query: dict = None,
		url_for: str = '', params_next = '', return_id: bool = False, return_cursor:bool = False,
		sort_key: str = '', sort_direction: int = -1):
    """A dummy docstring."""
    if '_id' in filter_query:
        filter_query['_id'] = ObjectId(filter_query['_id'])

    if filter_query is None:
        filter_query = {}
    count = await collection.count_documents(filter_query)

    if return_id:
        cursor = collection.find(filter_query).skip(skip).limit(limit)
    else:
        cursor = collection.find(filter_query, {'_id': 0}).skip(skip).limit(limit)

    if sort_key != '':
        cursor = cursor.sort(sort_key, sort_direction)

    next_url = None
    if count > (limit + skip):
        next_url = f'{url_for}?skip={skip + limit}&limit={limit}{params_next}'

    metadata = {
		'count': count,
		'skip': skip,
		'limit': limit,
		'next': next_url
	}
    if not return_cursor:
        query_res = []
        async for obj in cursor:
            query_res.append(obj)
        
        return query_res, metadata

    return cursor, metadata
