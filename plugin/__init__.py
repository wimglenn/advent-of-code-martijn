import io
import pkgutil
from contextlib import redirect_stdout

import nbformat


def blacklisted(cell):
    if cell["cell_type"] != "code":
        return True
    if "plt.figure()" in cell["source"]:
        return True
    if "graphviz" in cell["source"]:
        return True
    if "plot_license" in cell["source"]:
        return True
    if "from IPython.display import Markdown" in cell["source"]:
        return True


def transform(line):
    prefix = (
        "%",  # IPython magics
        "plot_area",
        "visualise",
        "plot_graph",
        "plot_execution",
        "animate",
    )
    if line.startswith(prefix):
        line = "# " + line
    return line


def main(year, day, data):
    fname = f"{year}/Day {day:02d}.ipynb"
    try:
        nbs = pkgutil.get_data("plugin", fname)
    except FileNotFoundError:
        raise NotImplementedError(year, day)
    nb = nbformat.reads(nbs, nbformat.NO_CONVERT)
    sources = [cell["source"] for cell in nb["cells"] if not blacklisted(cell)]
    lines = [s for source in sources for s in source.splitlines()]
    source = "\n".join([transform(line) for line in lines])
    string_io = io.StringIO()
    with redirect_stdout(string_io):
        exec(source, globals())
    output = string_io.getvalue()
    part1 = part2 = ""
    for line in output.splitlines():
        if line.startswith("Part 1:"):
            part1 = line[7:].strip()
        if line.startswith("Part 2:"):
            part2 = line[7:].strip()
    return part1, part2
