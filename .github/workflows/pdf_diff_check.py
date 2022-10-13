# use diff_pdf_visually module to output pdf diff between current and baseline

from diff_pdf_visually import pdf_similar
import sys
import pathlib

pdf_1 = sys.argv[1]
pdf_2 = sys.argv[2]
print(pdf_1)
print(pdf_2)

pathlib.Path(__file__).parents[2].joinpath(
    'docs', '_build', 'pdf', 'diffpdf').mkdir(parents=True, exist_ok=True)

p = pathlib.Path(__file__).parents[2].joinpath(
    'docs', '_build', 'pdf', 'diffpdf')


def log_pdf_diff(pdf_1, pdf_2, dir):

    pdf_similar(pdf_1, pdf_2, tempdir=dir)


log_pdf_diff(pdf_1, pdf_2, p)
