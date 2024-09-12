import subprocess
from rich.progress import track
from os import makedirs
from os.path import exists, splitext
from shutil import rmtree
from glob import iglob
from pathlib import Path

# Define subsets
subsets = {
    "latin": "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD",
    "latin-ext": "U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF",
}

output_dir = "output"
# Define features you want to activate and deactivate
active_layout_features = "ccmp,locl,mark,mkmk,lnum,kern,ss03,cv05,cv06"
deactivate_features = "calt,liga,clig"

# Clean the output directory if it exists
if exists(output_dir):
    rmtree(output_dir)
makedirs(output_dir)

# Iterate over input font files
for filepath in iglob("input/*.woff2"):
    filename = Path(filepath).name

    # Subset the font for each defined subset
    for subset in track(subsets, description=f"Subsetting {filename}..."):
        u_range = subsets[subset]
        outputfile = splitext(filename)[0]

        # Build the pyftsubset command
        subp_args = [
            "pyftsubset",
            filepath,
            f"--unicodes={u_range}",
            "--flavor=woff2",
            f"--output-file={output_dir}/{outputfile}.{subset}.woff2",
        ]

        # Add active layout features
        if active_layout_features:
            subp_args.append(f"--layout-features+={active_layout_features}")

        # Deactivate specific features
        if deactivate_features:
            subp_args.append(f"--layout-features-={deactivate_features}")

        # Execute the pyftsubset command
        subprocess.run(subp_args, check=True)
