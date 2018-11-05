"""
Configuration for plotting and saving plots.

Plotting style (from seaborn's `sns.axes_style()`) and context 
(`sns.plotting_context`) configuration.
"""

axes_styles = {'axes.facecolor': 'white',
                'axes.edgecolor': '.15',
                'axes.grid': False,
                'axes.axisbelow': True,
                'axes.labelcolor': '.15',
                'figure.facecolor': 'white',
                'grid.color': '.8',
                'grid.linestyle': '-',
                'text.color': '.15',
                'xtick.color': '.15',
                'ytick.color': '.15',
                'xtick.direction': 'out',
                'ytick.direction': 'out',
                'lines.solid_capstyle': 'round',
                'patch.edgecolor': 'w',
                'image.cmap': 'rocket',
                'font.family': ['sans-serif'],
                'font.sans-serif': ['Arial',
                                    'DejaVu Sans',
                                    'Liberation Sans',
                                    'Bitstream Vera Sans',
                                    'sans-serif'],
                'patch.force_edgecolor': True,
                'xtick.bottom': False,
                'xtick.top': False,
                'ytick.left': False,
                'ytick.right': False,
                'axes.spines.left': True,
                'axes.spines.bottom': True,
                'axes.spines.right': True,
                'axes.spines.top': True}

plotting_context = {'font.size': 9.600000000000001,
                    'axes.labelsize': 9.600000000000001,
                    'axes.titlesize': 9.600000000000001,
                    'xtick.labelsize': 8.8,
                    'ytick.labelsize': 8.8,
                    'legend.fontsize': 8.8,
                    'axes.linewidth': 1.0,
                    'grid.linewidth': 0.8,
                    'lines.linewidth': 1.2000000000000002,
                    'lines.markersize': 4.800000000000001,
                    'patch.linewidth': 0.8,
                    'xtick.major.width': 1.0,
                    'ytick.major.width': 1.0,
                    'xtick.minor.width': 0.8,
                    'ytick.minor.width': 0.8,
                    'xtick.major.size': 4.800000000000001,
                    'ytick.major.size': 4.800000000000001,
                    'xtick.minor.size': 3.2,
                    'ytick.minor.size': 3.2}

saving_config = {'savepath': 'figs/',
                 'dpi': None,
                 'facecolor': 'w',
                 'edgecolor': 'w',
                 'orientation': 'portrait',
                 'papertype': 'letter', 
                 'format': 'eps',
                 'transparent': True, 
                 'bbox_inches': None, 
                 'pad_inches': 0.1,
                 'frameon': None,
                 'metadata': None}
