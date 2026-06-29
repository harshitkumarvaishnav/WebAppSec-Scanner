from backend.scanner.common.request_handler import get_response

response = get_response("https://owasp.org")

print(response.status_code)
print(response.url)
print(response.headers.get("Server"))