# Libraries
import pandas as pd
import pandas.api.types as ptypes
import matplotlib.pyplot as plt

class BiPlot:
    def __init__(self, ProjectedData: pd.DataFrame, Loadings: pd.DataFrame, ExplainedVar: list, **kwargs):
        self.ProjectedData = ProjectedData
        self.Loadings = Loadings
        self.ExplainedVar = ExplainedVar

        # Optional arguments
        self.Fig_size = kwargs.get('Fig_size', (16, 12))
        self.Fig_size_sub = kwargs.get('Fig_size_sub', (20, 12))
        self.Overlaid = kwargs.get('Overlaid', True)
        self.Plot_style = kwargs.get('Plot_style', 'seaborn-v0_8-bright')
        self.Color_by_disc_var = kwargs.get('Color_by_disc_var', None)
        self.Sample_colors = kwargs.get('Sample_colors', 'blue')
        self.Sample_size = kwargs.get('Sample_size', 15)
        self.Sample_labels = kwargs.get('Sample_labels', True)
        self.Sample_labels_color = kwargs.get('Sample_labels_color', 'black')
        self.Sample_labels_size = kwargs.get('Sample_labels_size', 10)
        self.Sample_labels_shift = kwargs.get('Sample_labels_shift', .02)
        self.Arrow_colors = kwargs.get('Arrow_colors', 'red')
        self.Arrow_head_size = kwargs.get('Arrow_head_size', 0.05)
        self.Arrow_labels = kwargs.get('Arrow_labels', True)
        self.Arrow_labels_size = kwargs.get('Arrow_labels_size', 10)
        self.Arrow_labels_color = kwargs.get('Arrow_labels_color', 'black')
        self.Arrow_labels_shift = kwargs.get('Arrow_labels_shift', 1.15)
        self.X_label_size = kwargs.get('X_label_size', 15)
        self.Y_label_size = kwargs.get('Y_label_size', 15)
        self.Title_size = kwargs.get('Title_size', 20)

        self.validate_inputs()

    def validate_inputs(self):
        assert isinstance(self.ProjectedData, pd.DataFrame), \
            f"The argument ProjectedData in this function must be a data frame. You passed a {type(self.ProjectedData)}"
        assert isinstance(self.Loadings, pd.DataFrame), \
            f"The argument Loadings in this function must be a data frame. You passed a {type(self.Loadings)}"
        assert all(ptypes.is_numeric_dtype(self.ProjectedData[col]) for col in self.ProjectedData.columns), \
            "ProjectedData must be an all numeric data frame"
        assert all(ptypes.is_numeric_dtype(self.Loadings[col]) for col in self.Loadings.columns), \
            "Loadings must be an all numeric data frame"
        assert isinstance(self.ExplainedVar, list), \
            f"The argument ExplainedVar in this function is a list. You passed a {type(self.ExplainedVar)}"
        assert all(not isinstance(item, str) for item in self.ExplainedVar), \
            "The list for ExplainedVar must contains numbers"

    def plot(self):
        try:
            plt.style.use(self.Plot_style)
        except:
            print('Select a Plot_style in:','\n',plt.style.available)
        
        if self.Color_by_disc_var is None:
            if self.Overlaid:
                fig, ax = plt.subplots(figsize=self.Fig_size)
                self._plot_overlay(ax)
            else:
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=self.Fig_size_sub)
                self._plot_projected(ax1)
                self._plot_loadings(ax2)
        else:
            self._plot_with_color_by_disc_var()

        plt.show()

    def _plot_overlay(self, ax):
        ax.set_xlabel(f'Component 1 ({round(100 * self.ExplainedVar[0], 2)} %)', fontsize=self.X_label_size)
        ax.set_ylabel(f'Component 2 ({round(100 * self.ExplainedVar[1], 2)} %)', fontsize=self.Y_label_size)
        ax.set_title('2 Components', fontsize=self.Title_size)
        ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)

        row_dct = {row: i for i, row in enumerate(self.ProjectedData.index)}

        for row_word in self.ProjectedData.index:
            x, y = self.ProjectedData.iloc[row_dct[row_word], [0, 1]].values.flatten()
            ax.scatter(x, y, marker='o', color=self.Sample_colors, s=self.Sample_size)
            if self.Sample_labels:
                ax.text(x + self.Sample_labels_shift, y + self.Sample_labels_shift, row_word,
                        fontsize=self.Sample_labels_size, color=self.Sample_labels_color)

        for i in range(self.Loadings.shape[0]):
            ax.arrow(0, 0, self.Loadings.iloc[i, 0], self.Loadings.iloc[i, 1], color=self.Arrow_colors, alpha=0.5,
                     head_width=self.Arrow_head_size)
            if self.Arrow_labels:
                ax.text(self.Loadings.iloc[i, 0] * self.Arrow_labels_shift, self.Loadings.iloc[i, 1] * self.Arrow_labels_shift,
                        self.Loadings.index[i], color=self.Arrow_labels_color, fontsize=self.Arrow_labels_size,
                        ha='center', va='center')

    def _plot_projected(self, ax):
        row_dct = {row: i for i, row in enumerate(self.ProjectedData.index)}

        for row_word in self.ProjectedData.index:
            x, y = self.ProjectedData.iloc[row_dct[row_word], [0, 1]].values.flatten()
            ax.scatter(x, y, marker='o', color=self.Sample_colors, s=self.Sample_size)
            if self.Sample_labels:
                ax.text(x + self.Sample_labels_shift, y + self.Sample_labels_shift, row_word,
                        fontsize=self.Sample_labels_size, color=self.Sample_labels_color)

        ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.set_xlabel(f'Component 1 ({round(100 * self.ExplainedVar[0], 2)} %)', fontsize=self.X_label_size)
        ax.set_ylabel(f'Component 2 ({round(100 * self.ExplainedVar[1], 2)} %)', fontsize=self.Y_label_size)
        ax.set_title('2 Components - Observations', fontsize=self.Title_size)

    def _plot_loadings(self, ax):
        for i in range(self.Loadings.shape[0]):
            ax.arrow(0, 0, self.Loadings.iloc[i, 0], self.Loadings.iloc[i, 1], color=self.Arrow_colors, alpha=0.5,
                     head_width=self.Arrow_head_size)
            if self.Arrow_labels:
                ax.text(self.Loadings.iloc[i, 0] * (self.Arrow_labels_shift - .1), self.Loadings.iloc[i, 1] * (self.Arrow_labels_shift - .1),
                        self.Loadings.index[i], color=self.Arrow_labels_color, fontsize=self.Arrow_labels_size,
                        ha='center', va='center')

        ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.set_xlabel(f'Component 1 ({round(100 * self.ExplainedVar[0], 2)} %)', fontsize=self.X_label_size)
        ax.set_ylabel(f'Component 2 ({round(100 * self.ExplainedVar[1], 2)} %)', fontsize=self.Y_label_size)
        ax.set_title('2 Components - Variable Characterization', fontsize=self.Title_size)

    def _plot_with_color_by_disc_var(self):
        name1 = "tab10"
        cmap1 = plt.get_cmap(name1)
        colors_list1 = cmap1.colors

        name2 = 'Set3'
        cmap2 = plt.get_cmap(name2)
        colors_list2 = cmap2.colors

        color_list = colors_list1 + colors_list2

        targets = self.Color_by_disc_var.iloc[:, 0].unique()
        colors = color_list[:len(targets)]

        if self.Overlaid:
            fig, ax = plt.subplots(figsize=self.Fig_size)
            self._plot_overlay_with_color(ax, targets, colors)
        else:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=self.Fig_size_sub)
            self._plot_projected_with_color(ax1, targets, colors)
            self._plot_loadings(ax2)

        plt.show()

    def _plot_overlay_with_color(self, ax, targets, colors):
        ax.set_xlabel(f'Component 1 ({round(100 * self.ExplainedVar[0], 2)} %)', fontsize=self.X_label_size)
        ax.set_ylabel(f'Component 2 ({round(100 * self.ExplainedVar[1], 2)} %)', fontsize=self.Y_label_size)
        ax.set_title('2 Components', fontsize=self.Title_size)
        ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)

        row_dct = {row: i for i, row in enumerate(self.ProjectedData.index)}

        for target, color in zip(targets, colors):
            indicesToKeep = self.Color_by_disc_var == target
            ax.scatter(self.ProjectedData.loc[indicesToKeep, list(self.ProjectedData.columns)[0]],
                       self.ProjectedData.loc[indicesToKeep, list(self.ProjectedData.columns)[1]], marker='o', color=color,
                       s=15, label='samples')

        L = ax.legend()
        for l in range(len(targets)):
            L.get_texts()[l].set_text(targets[l])

        for row_word in self.ProjectedData.index:
            x, y = self.ProjectedData.iloc[row_dct[row_word], [0, 1]].values.flatten()
            if self.Sample_labels:
                ax.text(x + self.Sample_labels_shift, y + self.Sample_labels_shift, row_word,
                        fontsize=self.Sample_labels_size, color=self.Sample_labels_color)

        for i in range(self.Loadings.shape[0]):
            ax.arrow(0, 0, self.Loadings.iloc[i, 0], self.Loadings.iloc[i, 1], color=self.Arrow_colors, alpha=0.5,
                     head_width=self.Arrow_head_size)
            if self.Arrow_labels:
                ax.text(self.Loadings.iloc[i, 0] * self.Arrow_labels_shift, self.Loadings.iloc[i, 1] * self.Arrow_labels_shift,
                        self.Loadings.index[i], color=self.Arrow_labels_color, fontsize=self.Arrow_labels_size,
                        ha='center', va='center')

    def _plot_projected_with_color(self, ax, targets, colors):
        row_dct = {row: i for i, row in enumerate(self.ProjectedData.index)}

        for target, color in zip(targets, colors):
            indicesToKeep = self.Color_by_disc_var == target
            ax.scatter(self.ProjectedData.loc[indicesToKeep, list(self.ProjectedData.columns)[0]],
                       self.ProjectedData.loc[indicesToKeep, list(self.ProjectedData.columns)[1]], marker='o', color=color,
                       s=15)

        for row_word in self.ProjectedData.index:
            x, y = self.ProjectedData.iloc[row_dct[row_word], [0, 1]].values.flatten()
            if self.Sample_labels:
                ax.text(x + self.Sample_labels_shift, y + self.Sample_labels_shift, row_word,
                        fontsize=self.Sample_labels_size, color=self.Sample_labels_color)

        ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
        ax.set_xlabel(f'Component 1 ({round(100 * self.ExplainedVar[0], 2)} %)', fontsize=self.X_label_size)
        ax.set_ylabel(f'Component 2 ({round(100 * self.ExplainedVar[1], 2)} %)', fontsize=self.Y_label_size)
        ax.set_title('2 Components - Observations', fontsize=self.Title_size)
        ax.legend(targets)
