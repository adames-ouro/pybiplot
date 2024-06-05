# PyBiPlot: Principal Component Analysis Visual

This aims to reproduce the R's biplot visual for PCA where the visual combines both the scores and loadings. You'll see arrows representing the original variables' contributions to each principal component, and you'll also see how the data points project onto the components.

PyPi link: [PyPi link](https://pypi.org/project/PyBiPlot/)

Explanation of PCA and PyBiPlot usecase link: [PCA link](https://github.com/adames-ouro/PyBiPlot/blob/main/Example_of_use/Dimensionality%20Reduction%20-%20PCA.ipynb)

### Features:

- `Flexibility through Optional Parameters:` Multiple optional parameters allow users to customize the plot's appearance.

- `Support for Overlaying Plots:` Users can decide to overlay the samples and loadings plots or display them side by side.

- `Conditional Coloring based on Discrete Variables:` If provided, the plot can color samples based on the discrete variables' values.

- `Dynamic Labeling:` The script supports dynamic labeling based on the actual values of the projected data, loadings, and explained variances.

- `Arrow Representations for Loadings:` Loadings are represented as arrows, pointing in the direction and magnitude of the loading.

### Use:

```python
BiPlot(ProjectedData, Loadings, ExplainedVar, **kwargs).plot()
```

- `ProjectedData:` (pd.DataFrame) - The projected data.
- `Loadings:` (pd.DataFrame) - The loadings data.
- `ExplainedVar:` (list) - Explained variance for the components.

### Optional Parameters (kwargs):

- `Fig_size:` Figure size (default is (16, 12))
- `Fig_size_sub:` Figure size for subplots (default is (20, 12))
- `Overlaid:` Flag to overlay plots or not (default is True)
- `Plot_style:` Style of the plot (default is 'seaborn-v0_8-bright')
- `Color_by_disc_var:` Column of discrete variable to color by (default is None)
- `Sample_colors:` Colors for samples (default is 'blue')
- `Sample_size:` Size of the sample points (default is 15)
- `Sample_labels:` Flag to show sample labels or not (default is True)
- `Sample_labels_color:` Color for sample labels (default is 'black')
- `Sample_labels_size:` Size of the sample labels (default is 10)
- `Sample_labels_shift:` Shift for sample labels (default is .02)
- `Arrow_colors:` Color of the arrows (default is 'red')
- `Arrow_head_size:` Size of the arrow heads (default is 0.05)
- `Arrow_labels:` Flag to show arrow labels or not (default is True)
- `Arrow_labels_size:` Size of the arrow labels (default is 10)
- `Arrow_labels_color:` Color of the arrow labels (default is 'black')
- `Arrow_labels_shift:` Shift for arrow labels (default is 1.15)
- `X_label_size:` Size of the X-axis label (default is 15)
- `Y_label_size:` Size of the Y-axis label (default is 15)
- `Title_size:` Size of the title (default is 20)
