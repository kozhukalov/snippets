all: main.pdf

%.pdf: %.dvi
	dvipdf $<

%.dvi: %.tex
	latex $<
