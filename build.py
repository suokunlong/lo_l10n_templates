#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import sys
from zipfile import ZipFile

root_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
src_dir = os.path.join(root_dir, "source")
build_dir = os.path.join(root_dir, "build")

extension_path = os.path.join(build_dir, "lo_l10n_templates.oxt")
meta_files = {
    "description.xml",
    "META-INF/manifest.xml",
    "mimetype",
    "Paths.xcu",
    "LICENSE",
}
templates_to_be_included = [
    ("zh_CN/normal", "ott"),
]

if not os.path.exists(build_dir):
    os.mkdir(build_dir)

with ZipFile(extension_path, 'w') as archive:

    # Add meta data
    for meta in meta_files:
        archive.write(os.path.join(src_dir, meta), meta)

    # Zip and add the templates
    for template_info in templates_to_be_included:
        template = os.path.join("template", template_info[0])
        tmp = "/tmp/loextentiontmp"
        with ZipFile(tmp, "w") as odf:
            for root, dirs, files in os.walk(os.path.join(src_dir, template)):
                for name in files:
                    odf_component_full_path = os.path.join(root, name)
                    odf_component = odf_component_full_path[len(src_dir) + len(template) + 2 :]
                    odf.write(odf_component_full_path, odf_component)

        archive.write(tmp, template + "." + template_info[1])

    # Add the groupuinames.xml
    griupuinames = "template/groupuinames.xml"
    archive.write(os.path.join(src_dir, griupuinames), griupuinames)
    
    print(extension_path, ": Done.")
