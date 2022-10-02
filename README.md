LibreOffice Localized Template Set is a collection of LibreOffice templates designed by the "localization" team to fulfill the special needs and requirements of their document formatting and layout in different countries/regions all over the world.

It is designed as a LibreOffice extension, so that users can install it directly and uninstall if they no longer need it.

# How To Install

1. Download the .oxt file located in the "releases" directory.
2. In LibreOffice, click the menu "Tools > Extension Manager", click the "Add" button, navigate to the .oxt file and click "Open". Accept the license to finish the installation.
3. Restart LibreOffice.

# How To Use

After installation, the templates included in this extension will show in the Template Manager dialog in LibreOffice. The template categories as defined in "source/template/groupuinames.xml" will show in the template cagerogy dropdown list (for instance, currently there is only one cagegory named "简体中文模板集" (Simplified Chinese Templates Set).

# Adding New Templates For Your Language Category

Assume you want to add a template named "Foo Template", for the language with a lang-tag "qtz":

1. Add a new directory "source/template/qtz" if their is no such language tag directory.
2. Create a directory "source/template/qtz/foo". This directory will hold all the files for your new template.
3. Design your template in LibreOffice, then unzip your template files into "source/template/qtz/foo". Clean the template files as much as possible. Please note that the <dc:title> tag in your "source/template/qtz/foo/meta.xml" file will be the template name shown on the LibreOffice template manager UI, thus you may use a localized name in this tag.
4. Add a new entry in "source/template/groupuinames.xml". The default-ui-name you define here will show as a template category in the LibreOffice template manager. You can use localized name here.
5. Add a new entry to the "templates_to_be_included" list in the "build.py" python script.
6. Run "build py". You will get the built extension in the "build" directory.

