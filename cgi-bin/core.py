#!/usr/bin/env python3
import cgi
import requests
import webbrowser

form = cgi.FieldStorage()
query = form.getfirst("query", "none")
request = requests.session()
request.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
get_request = request.get('https://www.google.ru/search?q={}'.format(query), timeout= 21)
text_request = get_request.text
find_url = text_request.find('<div class="r"', 0)
start_request = find_url + 24
end_request = text_request.find('"', start_request)
url = text_request[start_request:end_request]
webbrowser.open(url, new="2")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
		</head>
		<body>
		<script language="JavaScript" type="text/javascript">
			window.location = "http://localhost:8000/"
		</script>
		</body>
		</html>""")
