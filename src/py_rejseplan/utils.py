from requests.models import PreparedRequest

def dump_prepared_request(prepared_request: PreparedRequest):
    # Print the request line
    print(" REQUEST LINE ".center(50, "-"))
    print(f"{prepared_request.method} {prepared_request.url} HTTP/1.1")
    
    # Print the headers
    print(" HEADER ".center(50, "-"))
    for header, value in prepared_request.headers.items():
        print(f"{header}: {value}")
    
    # Print the body if it exists
    print(" BODY ".center(50, "-"))
    if prepared_request.body:
        print(f"\n{prepared_request.body}")
    print("-".center(50, "-"))