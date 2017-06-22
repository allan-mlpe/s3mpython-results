<<<<<<< MINE
    def python_jedi_matches(self, text, line_buffer, cursor_pos):
        """Match attributes or global Python names using Jedi."""
        if line_buffer.startswith('aimport ') or line_buffer.startswith('%aimport '):
            return ()
        namespaces = []
        if self.namespace is None:
            import __main__
            namespaces.append(__main__.__dict__)
        else:
            namespaces.append(self.namespace)
        if self.global_namespace is not None:
            namespaces.append(self.global_namespace)

        # cursor_pos is an it, jedi wants line and column

        interpreter = jedi.Interpreter(line_buffer, namespaces, column=cursor_pos)
        path = jedi.parser.user_context.UserContext(line_buffer, \
                (1, len(line_buffer))).get_path_until_cursor()
        path, dot, like = jedi.api.helpers.completion_parts(path)
        if text.startswith('.'):
            # text will be `.` on completions like `a[0].<tab>`
            before = dot
        else:
            before = line_buffer[:len(line_buffer) - len(like)]


        def trim_start(completion):
            """completions need to start with `text`, trim the beginning until it does"""
            if text in completion and not (completion.startswith(text)):
                start_index = completion.index(text)
                if cursor_pos:
                     assert start_index <  cursor_pos
                return completion[start_index:]
            return completion
=======
    def python_matches(self, text):
        """Match attributes or global python names"""
>>>>>>> YOURS