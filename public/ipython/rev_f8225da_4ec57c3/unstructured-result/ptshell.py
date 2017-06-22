<<<<<<< MINE
            # TODO: Use Jedi to determine meta_text
            # (Jedi currently has a bug that results in incorrect information.)
            # meta_text = ''
            # yield Completion(m, start_position=start_pos,
            #                  display_meta=meta_text)
=======
            m = unicodedata.normalize('NFC', m)

            # When the first character of the completion has a zero length,
            # then it's probably a decomposed unicode character. E.g. caused by
            # the "\dot" completion. Try to compose again with the previous
            # character.
            if wcwidth(m[0]) == 0:
                if document.cursor_position + start_pos > 0:
                    char_before = document.text[document.cursor_position + start_pos - 1]
                    m = unicodedata.normalize('NFC', char_before + m)

                    # Yield the modified completion instead, if this worked.
                    if wcwidth(m[0:1]) == 1:
                        yield Completion(m, start_position=start_pos - 1)
                        continue

>>>>>>> YOURS