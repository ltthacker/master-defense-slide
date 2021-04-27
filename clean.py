import os

ext = ["*.aux",
        "*.bbl",
        "*.fls",
        "*.log",
        "*.synctex.gz",
        "*.fdb_latexmk",
        "*.blg",
        "*.out",
        "*.run.xml",
        "*.toc",
        "*.glo",
        "*.bcf",
        "*.acn",
        "*.ist",
        "*.lof",
        "*.lot",
        "*.nav",
        "*.snm",
        ]

for e in ext:
    command = f'find . -name "{e}" -type f -delete'
    os.system(command)