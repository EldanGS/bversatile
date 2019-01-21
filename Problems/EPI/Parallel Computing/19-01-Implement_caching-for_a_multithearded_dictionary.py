import threading


class SpellCheckService:
    w_last = closest_to_last_word = None
    lock = threading.Lock()

    @staticmethod
    def service(req, resp):
        w = req.extract_word_to_check_from_request()
        result = None
        with SpellCheckService.lock:
            if w == SpellCheckService.w_last:
                result = SpellCheckService.closest_to_last_word.copy()
        if result is None:
            result = closest_in_dictionary(w)
            with SpellCheckService.lock:
                SpellCheckService.w_last = w
                SpellCheckService.closest_to_last_word = result
        resp.encode_into_response(result)
