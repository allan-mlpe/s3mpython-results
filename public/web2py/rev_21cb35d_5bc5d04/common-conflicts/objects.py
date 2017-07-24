<<<<<<< MINE
                self._common_filter = lambda q: reduce(AND, [query(q), newquery(q)])
=======
                self._common_filter = \
                    lambda q: reduce(AND, [query(q), newquery(q)])
>>>>>>> YOURS