import os
from bs4 import BeautifulSoup


def build_corpus():
    documents = []
    docs_in_class = [0, 0]

    def read_directory(dir: str, lbl: int):
        for file_name in os.listdir(dir):
            with open(os.path.join(dir, file_name), "r") as f:
                documents.append(
                    (BeautifulSoup(f.read(), "lxml").text.replace("\n", " "), lbl)
                )
                docs_in_class[lbl] += 1

    directory_path = lambda folder: os.path.join(
        os.path.dirname(__file__),
        f"course-cotrain-data/fulltext/{folder}",
    )
    
    read_directory(directory_path("non-course"), 0)
    read_directory(directory_path("course"), 1)

    return documents, sum(docs_in_class), docs_in_class


def vocabulary(corpus):
    return list({term for terms, _ in corpus for term in terms})
