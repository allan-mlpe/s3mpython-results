<<<<<<< MINE
            if query:            
                self._common_filter = \
                    lambda q: reduce(AND, [query(q), newquery(q)])
                newquery = query & newquery
=======
            if query:
                self._common_filter = lambda q: reduce(AND, [query(q), newquery(q)])
>>>>>>> YOURS