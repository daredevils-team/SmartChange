# Initialize Google Earth API
import ee

ee.Authenticate()
ee.Initialize()

import folium

import io
from PIL import Image


def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
      tiles=map_id_dict['tile_fetcher'].url_format,
      attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
      name=name,
      overlay=True,
      control=True
  ).add_to(self)

# Load an image.
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Define the visualization parameters.
image_viz_params = {
    'bands': ['B5', 'B4', 'B3'],
    'min': 0,
    'max': 0.5,
    'gamma': [0.95, 1.1, 1]
}

# Define a map centered on San Francisco Bay.
map_l8 = folium.Map(location=[37.5010, -122.1899], zoom_start=10)

# Add the image layer to the map and display it.
map_l8.add_ee_layer(image, image_viz_params, 'false color composite')

img_data = map_l8._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.show()
