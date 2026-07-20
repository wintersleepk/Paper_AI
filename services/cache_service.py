import hashlib


class CacheService:

    def pdf_hash(self, uploaded_file):

        uploaded_file.seek(0)

        file_bytes = uploaded_file.read()

        uploaded_file.seek(0)

        return hashlib.sha256(
            file_bytes
        ).hexdigest()