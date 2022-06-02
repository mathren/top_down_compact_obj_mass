rule fit:
    input:
        "src/data/datafile1.txt"
    output:
        "src/tex/figures/fit_DM_PPI.pdf",
        "src/tex/figures/fit_DM_PPI.jpeg",
        "src/tex/output/fit_DM_PPI.tex"
    script:
        "src/scripts/fit_DM_PPI.py"