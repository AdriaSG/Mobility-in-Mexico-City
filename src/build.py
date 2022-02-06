#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "urban_mobility_tool"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on('sklearn')
    project.depends_on('pandas')
    project.depends_on('matplotlib.pyplot')
    project.depends_on('seaborn')

    pass
