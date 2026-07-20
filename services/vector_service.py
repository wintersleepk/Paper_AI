import os
import pickle

from config import CACHE_DIR


class VectorService:

    def build(self, paper):

        paper.chunks = [

            paper.full_text[i:i + 1000]

            for i in range(

                0,

                len(paper.full_text),

                1000

            )

        ]

        paper.vector_ready = True

        return paper

    def save(self, paper):

        folder = os.path.join(

            CACHE_DIR,

            paper.pdf_hash

        )

        os.makedirs(

            folder,

            exist_ok=True

        )

        with open(

            os.path.join(

                folder,

                "paper.pkl"

            ),

            "wb"

        ) as f:

            pickle.dump(

                paper,

                f

            )

    def load(self, paper):

        folder = os.path.join(

            CACHE_DIR,

            paper.pdf_hash

        )

        paper_file = os.path.join(

            folder,

            "paper.pkl"

        )

        if not os.path.exists(

            paper_file

        ):

            return None

        try:

            with open(

                paper_file,

                "rb"

            ) as f:

                cached_paper = pickle.load(f)

            return cached_paper

        except Exception:

            return None

    def search(

        self,

        paper,

        query,

        k=5

    ):

        return []