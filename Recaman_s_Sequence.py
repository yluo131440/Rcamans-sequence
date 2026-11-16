import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def next_term(previous,step,sequence):
    if previous - step <= 0 or previous - step in sequence:
        return previous + step 
    else:
        return previous - step

def recaman(n):
    sequence = [0]
    for i in range(1,n+1):
        sequence.append(next_term(sequence[-1],i,sequence))
    return sequence


def check_differences(sequence):
    for i in range (1,len(sequence)):
        if abs(sequence[-i] - sequence[-i-1]) != len(sequence) - i:
            return False
        else:
            return True

def first_duplicate(sequence):
    seen = []
    for x in sequence:
        if x in seen:
            return x
        else:
            seen.append(x) 
    return None


def appears(value,sequence):
    for x in sequence:
        if x == value:
            return True
    return False

def first_missing(sequence):
    for i in range(len(sequence)):
        if appears(i,sequence) == False:
            return i

def count_present(sequence,upper):
    a = 0
    for i in range(upper):
       if appears(i,sequence) == True:
           a += 1
    return a 

def draw_recaman(n=65,
                 filename="recaman.pdf",
                 linewidth=1.2,
                 color="#1a1a1a",
                 linestyle="solid",
                 capstyle="round",
                 start_up=True,
                 background=None):
    """Render the arc diagram of the first n+1 Recaman terms into a PDF.
 
    n          : number of steps (the diagram has n arcs).
    filename   : output path; a ".pdf" extension gives a vector PDF, but
                 matplotlib also accepts ".svg" or ".png" here.
    linewidth  : stroke width of the arcs.
    color      : any matplotlib color (name, "#rrggbb", (r, g, b) ...).
    linestyle  : "solid", "dashed", "dotted" or "dashdot".
    capstyle   : how stroke ends look -- "round", "butt" or "projecting".
    start_up   : True -> the first arc is drawn above the axis.
    background : figure background color, or None for transparent.
    """
    seq = recaman(n)
 
    fig, ax = plt.subplots(figsize=(12, 5))
 
    for i in range(1, len(seq)):
        x0, x1 = seq[i - 1], seq[i]
        center = (x0 + x1) / 2.0
        diameter = abs(x1 - x0)          # equals i, since |a_i - a_{i-1}| = i
 
        up = (i % 2 == 1) == start_up
        theta1, theta2 = (0, 180) if up else (180, 360)
 
        arc = Arc((center, 0), width=diameter, height=diameter,
                  theta1=theta1, theta2=theta2,
                  linewidth=linewidth, edgecolor=color, linestyle=linestyle)
        arc.set_capstyle(capstyle)
        ax.add_patch(arc)
 
    # frame the picture tightly around the arcs, keep circles circular
    radii = [i / 2.0 for i in range(1, len(seq))]
    top = max(r for i, r in enumerate(radii, start=1) if (i % 2 == 1) == start_up)
    bottom = max(r for i, r in enumerate(radii, start=1) if (i % 2 == 1) != start_up)
    margin = 0.02 * max(seq) + 1
    ax.set_xlim(min(seq) - margin, max(seq) + margin)
    ax.set_ylim(-bottom - margin, top + margin)
    ax.set_aspect("equal")
    ax.axis("off")
 
    if background is not None:
        fig.patch.set_facecolor(background)
        ax.set_facecolor(background)
 
    fig.savefig(filename,
                bbox_inches="tight", pad_inches=0.1,
                transparent=(background is None))
    plt.close(fig)
    print(f"Saved {filename}  ({n} arcs, values 0..{max(seq)})")

draw_recaman()