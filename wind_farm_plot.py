import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# Plot parameters for style
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["legend.scatterpoints"] = 1
plt.rcParams["legend.numpoints"] = 1
plt.rcParams['figure.dpi'] = 300


class wind_farm_layout():
    '''
    Wind farm layout class. Nests the functions for plotting.
    Parameters:
        x: array of wind turbine coordinates.
        y: array of wind turbine coordinates.
        D: array of wind turbine rotor diameters.
        boundary_list: list of boundary constraint polygons
        ax: axis to plot on.
    '''

    def __init__(self, x, y, D, boundary_list, min_spacing=0, ax=None):
        self.x = x
        self.y = y
        self.D = D
        self.boundary_list = boundary_list
        self.min_spacing = min_spacing
        if ax:
            self.ax = ax

    def plot_layout(self):
        self.ax.scatter(self.x, self.y, s=60, marker="2", color='k')
        sc = [plt.Circle((xi, yi), .5 * self.min_spacing, fill=False,
                         #facecolor='b', alpha=0.25,
                         edgecolor='k', linestyle='--', linewidth=.5
                         ) for xi, yi in zip(self.x, self.y)]
        [self.ax.add_patch(spacing_constraint) for spacing_constraint in sc]
        # plot boundary constraints
        for bound in self.boundary_list:
            x_bound, y_bound = bound.T
            x_bound = np.append(x_bound, x_bound[0])
            y_bound = np.append(y_bound, y_bound[0])
            self.ax.plot(x_bound, y_bound, color='k', linewidth=.7)
            self.ax.set_aspect('equal')

def main():
    if __name__ == '__main__':
        import numpy as np
        import pickle
        import matplotlib.pyplot as plt
    
        x = np.arange(0, 1500, 500) + 263.1e3
        y = np.zeros_like(x) + 6.5057e6
    
        D = 120
        min_spacing = 200
    
        with open("pf_multiboundary", "rb") as fp:
            multiboundary = pickle.load(fp)
    
        boundary_list = []
        for boundary, n in multiboundary:
            boundary_list.append(boundary)
            
        from wind_farm_plot import wind_farm_layout as wfl
    
        fig, ax = plt.subplots()
        ploter = wfl(x, y, D, boundary_list, min_spacing, ax=ax)
        ploter.plot_layout()

main()