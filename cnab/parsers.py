from rest_framework.parsers import BaseParser, FileUploadParser

class PlainTextParser(BaseParser):

    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):

        return stream