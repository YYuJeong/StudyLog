def solution(cacheSize, cities):
    cache = []
    runtime = 0
    for city in cities:
        city = city.lower()
        if city in cache:  # cache hit
            runtime += 1
            cache.remove(city)
            cache.append(city)
        else:  # cache miss
            runtime += 5
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache.append(city)
                cache.pop(0)

    return runtime
