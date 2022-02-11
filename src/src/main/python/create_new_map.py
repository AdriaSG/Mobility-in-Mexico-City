from keplergl_cli import Visualize
mapbox_apikey = "pk.eyJ1IjoiYWRyaWFuYXNnIiwiYSI6ImNreW5nOWZiNDAzZGMyb24ybnZtNmhsOWoifQ.Y4VsqsgJXoA6CCGt_Cdk0Q"

def create_new_map(key):
    """
    This function renders kepler.gl widget with an empty map, the mapbox API key is personal
    """
    vis = Visualize(api_key= key )
    html_path = vis.render(open_browser=True, read_only=False)
    return html_path

create_new_map(mapbox_apikey)