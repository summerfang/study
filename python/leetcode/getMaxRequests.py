import sys

def getMaxRequests(bandwidth, request, total_bandwidth):
    endpoints = [(bandwidth[i], request[i]) for i in range(len(bandwidth))]
    endpoints.sort(key=lambda x: x[1], reverse=True)
    
    total_requests = 0
    used_bandwidth = 0
    
    for endpoint in endpoints:
        if used_bandwidth + endpoint[0] <= total_bandwidth:
            used_bandwidth += endpoint[0]
            total_requests += endpoint[1]
    
    return total_requests

print(sys.argv)

bw = [200, 100, 350, 50,100]
req = [270, 142, 450, 124, 189]

print(getMaxRequests(bw, req, 500))