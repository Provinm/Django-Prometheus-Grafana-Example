from prometheus_client import Counter

req_counter = Counter("total_req", "total requests number")
