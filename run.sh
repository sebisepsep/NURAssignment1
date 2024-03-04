echo "Hello :)"

echo "part1" 
python3 part1.py

echo "part2a" 
python3 a2.py

echo "part2b" 
python3 b2.py

echo "part2c" 
python3 c2.py

echo "Creation plots" 
python3 print.py

echo "part2d" 

echo "%timeit" 
echo "2a)"
python3 -m timeit -n 10 -r 1 -s "import a2" "a2.main()"
echo "2b)"
python3 -m timeit -n 10 -r 1 -s "import b2" "b2.main()"
echo "2c)"
python3 -m timeit -n 10 -r 1 -s "import c2" "c2.main()"

echo "Generating the pdf"

pdflatex template.tex
bibtex template.aux
pdflatex template.tex
pdflatex template.tex
