<<<<<<< MINE
            # Prevent an attacker from adding an arbitrary url after the _next variable in the request.
            # Browsers will fix a single / so check multiple things just in case
            items = filter(None, next.split('/'))
            has_url = any(x in next for x in ['//', ':', 'ftp', 'http', 'rss', 'xml'])
            if has_url and len(items) > 1:
                if items[1] != current.request.env.http_host:
                    next = None
=======
            # Prevent an attacker from adding an arbitrary url after the
            # _next variable in the request.
            items = next.split('/')
            if next:
                if next[0] != '/':
                    if '://' not in next or next.split('://')[1].split('/')[0] != current.request.env.http_host:
                        if ':' in next.split('/')[0]:
                            next = None
>>>>>>> YOURS