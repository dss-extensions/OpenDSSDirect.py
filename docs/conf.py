import os, sys

if not os.path.exists('../../dss-extensions'):
    raise RuntimeError('dss-extensions common repo not found. Be sure to clone it side-by-side with OpenDSSDirect.py when building docs.')

if not os.path.exists('../../dss_python_backend'):
    raise RuntimeError('dss_python_backend common repo not found. Be sure to clone it side-by-side with OpenDSSDirect.py when building docs.')

sys.path.append('../../dss-extensions/docs')
from common_conf import *
from opendssdirect import dss

project = 'OpenDSSDirect.py'
copyright = '2017-2024 Dheepak Krishnamurthy, Paulo Meira, DSS-Extensions contributors'
author = 'Dheepak Krishnamurthy, Paulo Meira, DSS-Extensions contributors'
version = dss.__version__
release = dss.__version__
        
# If we ever need more extensions or change settings, we are free to change it here. e.g.
extensions.append('autodoc2')

# auto_mode doesn't work great for this kind of project, turn if off:
autodoc2_packages = [
    {
        "path": "../opendssdirect",
        "auto_mode": False,
    },
    {
        "path": "../../dss_python_backend/dss_python_backend",
        "auto_mode": False,
    },
]

autodoc2_docstrings = 'all'
autodoc2_sort_names = True
autodoc2_class_docstring = 'both'
autodoc2_hidden_regexes = [
    r'.*\.__setattr__$',
    r'.*\.__slots__$',
]

html_logo = '_static/opendssdirect.svg'
html_theme_options["logo"] = {
    "image_dark": '_static/opendssdirect-dark.svg',
}
html_theme_options["show_toc_level"] = 1
html_favicon = '_static/dssx.png'

# Ugly patches...

# This one is to make it run at all
patch_autodoc2()

# This one is related to node_ids being too long with duplicated data
# 
import sphinx.domains.python
add_target_and_index_org = sphinx.domains.python.PyObject.add_target_and_index 
class PatchPyObject:
    def add_target_and_index(self, name_cls, sig, signode):
        if name_cls[0].count('.') > 2:
            mod_name = self.options.get('module', self.env.ref_context.get('py:module'))
            assert mod_name == name_cls[0][:len(mod_name)]
            name_cls = (name_cls[0][1 + len(mod_name):], name_cls[1])
            parts = name_cls[0].split('.')
            if len(parts) > 1 and parts[0] == parts[1]:
                name_cls = ('.'.join(parts[1:]), name_cls[1])

        return add_target_and_index_org(self, name_cls, sig, signode)

sphinx.domains.python.PyObject.add_target_and_index = PatchPyObject.add_target_and_index