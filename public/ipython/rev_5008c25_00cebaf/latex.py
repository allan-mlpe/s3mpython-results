"""
Exporter that allows Latex Jinja templates to work.  Contains logic to
appropriately prepare IPYNB files for export to LaTeX.  Including but 
not limited to escaping LaTeX, fixing math region tags, using special
tags to circumvent Jinja/Latex syntax conflicts.
"""


import os

from IPython.utils.traitlets import Unicode, List
from IPython.config import Config

from IPython.nbconvert import filters, transformers
from .exporter import Exporter
class  LatexExporter (Exporter) :
	"""
    Exports to a Latex template.  Inherit from this class if your template is
    LaTeX based and you need custom tranformers/filters.  Inherit from it if 
    you are writing your own HTML template and need custom tranformers/filters.  
    If you don't need custom tranformers/filters, just change the 
    'template_file' config option.  Place your template in the special "/latex" 
    subfolder of the "../templates" folder.
    """
	    
    file_extension = Unicode(        'tex', config=True,         help="Extension of the file that should be written to disk")
	
    template_file = Unicode(        'base', config=True,        help="Name of the template file to use")
	
        template_path = Unicode(        os.path.join("..", "templates", "latex"), config=True,        help="Path where the template files are located.")
	
    template_skeleton_path = Unicode(        os.path.join("..", "templates", "latex", "skeleton"), config=True,        help="Path where the template skeleton files are located.")
	
        jinja_comment_block_start = Unicode("((=", config=True)
	    jinja_comment_block_end = Unicode("=))", config=True)
	    jinja_variable_block_start = Unicode("(((", config=True)
	    jinja_variable_block_end = Unicode(")))", config=True)
	    jinja_logic_block_start = Unicode("((*", config=True)
	    jinja_logic_block_end = Unicode("*))", config=True)
	    
        template_extension = Unicode(".tplx", config=True)
	

    def _init_filters(self):
        """
        Register all of the filters required for the exporter.
        """
        
                super(LatexExporter, self)._init_filters()

                self.register_filter('escape_tex', filters.escape_latex) 
        self.register_filter('highlight', filters.highlight2latex)
	@property
    def default_config(self):
<<<<<<< MINE
        c = Config({            'NbConvertBase': {                'display_data_priority' : ['latex', 'svg', 'png', 'jpg', 'jpeg', 'text']                },             'ExtractFigureTransformer': {                    'enabled':True                 },             'SVG2PDFTransformer': {                    'enabled':True                 },             'LatexTransformer': {                    'enabled':True                 }         })
=======
        c = Config({            'NbConvertBase': {                'display_data_priority' : ['latex', 'pdf', 'png', 'jpg', 'svg', 'jpeg', 'text']                },             'ExtractFigureTransformer': {                    'enabled':True                 },             'SVG2PDFTransformer': {                    'enabled':True                 },             'LatexTransformer': {                    'enabled':True                 }         })
>>>>>>> YOURS
        c.merge(super(LatexExporter,self).default_config)
        return c
	"""
    Exports to a Latex template.  Inherit from this class if your template is
    LaTeX based and you need custom tranformers/filters.  Inherit from it if 
    you are writing your own HTML template and need custom tranformers/filters.  
    If you don't need custom tranformers/filters, just change the 
    'template_file' config option.  Place your template in the special "/latex" 
    subfolder of the "../templates" folder.
    """

