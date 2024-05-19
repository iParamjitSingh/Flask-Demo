from matplotlib.figure import Figure

def plot_Graph():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    return fig
