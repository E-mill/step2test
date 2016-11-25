def app_wcgi(environ,start_responce):
	body=''
	for x in environ["QUERY_STRING"].split('&'):
		body=body+x+"\n"
	start_responce('200 OK',[('Content-Type','text/plain')])
	return (body)
