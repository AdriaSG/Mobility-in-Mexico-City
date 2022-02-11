from keplergl_cli import Visualize
mapbox_apikey = "pk.eyJ1IjoiYWRyaWFuYXNnIiwiYSI6ImNreW5nOWZiNDAzZGMyb24ybnZtNmhsOWoifQ.Y4VsqsgJXoA6CCGt_Cdk0Q"

def render_new_map(key):
    """
    This function renders kepler.gl widget with an empty map, the mapbox API key is personal
    """
    vis = Visualize(api_key= key )
    html_path = vis.render(open_browser=True, read_only=False)
    return html_path

#
# Functional programming
# Above function is an example of side-effect-free function, it is working only with their own variables
# which they are not changed, we must be able to call this function anytime and be sure that it won't interfere
# with other functionalities in the tool.
#