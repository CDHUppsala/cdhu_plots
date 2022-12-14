# Adapted from https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/__init__.py
from os import listdir
from os.path import isdir, join

from cdhu_plots.cdhu_plotly import cdhu

import matplotlib.pyplot as plt
import pkg_resources
from matplotlib import font_manager


font_files = font_manager.findSystemFonts(fontpaths="cdhu_plots/Lato/")
for font in font_files:
    font_manager.fontManager.addfont(font)


# register the included stylesheet in the matplotlib style library
data_path = pkg_resources.resource_filename("cdhu_plots", "cdhu_plt/")
stylesheets = plt.style.core.read_style_directory(data_path)  # Reads styles in /styles
# Reads styles in /styles subfolders
for inode in listdir(data_path):
    new_data_path = join(data_path, inode)
    if isdir(new_data_path):
        new_stylesheets = plt.style.core.read_style_directory(new_data_path)
        stylesheets.update(new_stylesheets)
# Update dictionary of styles
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
