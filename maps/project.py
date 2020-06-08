from maps.config import *
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Polygon

from maps.roi import ROI


class Project(object):
    def __init__(self,
                 workflow={'model_engine': 'geomodeller'},
                 # region of interest coordinates in metre-based system (or non-degree system)
                 # (minx, miny, maxx, maxy, bottom, top)
                 # TODO: Remove harcoding if local files ship with examples
                 geology_file="/map2loop-2/maps/data/hams-test.shp",
                 fault_file="/map2loop-2/maps/data/GEOS_GEOLOGY_LINEARSTRUCTURE_500K_GSD.shp",
                 structure_file="/map2loop-2/maps/data/hams2_structure.shp",
                 mindep_file="/map2loop-2/maps/data/mindeps_2018.shp",
                 bbox=(500057, 7455348, 603028, 7567953, -8200, 1200)
                 ):
        # TODO: Create ways to get and set local files
        self.update_workflow(workflow)
        self.geology_file = geology_file
        self.fault_file = fault_file
        self.structure_file = structure_file
        self.mindep_file = mindep_file

        self.update_roi(bbox)
    # TODO: Make workflow dictionary more editable

    def update_workflow(self, workflow):
        if(workflow['model_engine'] == 'geomodeller'):
            workflow.update({'seismic_section': False,
                             'cover_map': False,
                             'near_fault_interpolations': True,
                             'fold_axial_traces': False,
                             'stereonets': False,
                             'formation_thickness': True,
                             'polarity': False,
                             'strat_offset': False,
                             'contact_dips': True})
        elif(workflow['model_engine'] == 'loopstructural'):
            workflow.update({'seismic_section': False,
                             'cover_map': False,
                             'near_fault_interpolations': False,
                             'fold_axial_traces': True,
                             'stereonets': False,
                             'formation_thickness': True,
                             'polarity': False,
                             'strat_offset': False,
                             'contact_dips': False})
        elif(workflow['model_engine'] == 'gempy'):
            workflow.update({'seismic_section': False,
                             'cover_map': False,
                             'near_fault_interpolations': False,
                             'fold_axial_traces': True,
                             'stereonets': False,
                             'formation_thickness': False,
                             'polarity': False,
                             'strat_offset': False,
                             'contact_dips': False})
        elif(workflow['model_engine'] == 'noddy'):
            workflow.update({'seismic_section': False,
                             'cover_map': False,
                             'near_fault_interpolations': False,
                             'fold_axial_traces': False,
                             'stereonets': False,
                             'formation_thickness': False,
                             'polarity': False,
                             'strat_offset': False,
                             'contact_dips': False})
        else:
            workflow.update({'seismic_section': False,
                             'cover_map': False,
                             'near_fault_interpolations': False,
                             'fold_axial_traces': False,
                             'stereonets': True,
                             'formation_thickness': True,
                             'polarity': False,
                             'strat_offset': True,
                             'contact_dips': False})
        self.workflow = workflow

    def update_roi(self, bbox):
        # TODO: Make crs defaults and specifiable not from config
        self.bbox = bbox
        minx = bbox[0]
        maxx = bbox[1]
        miny = bbox[2]
        maxy = bbox[3]
        lat_point_list = [miny, miny, maxy, maxy, maxy]
        lon_point_list = [minx, maxx, maxx, minx, minx]
        bbox_geom = Polygon(zip(lon_point_list, lat_point_list))
        polygon = gpd.GeoDataFrame(
            index=[0], crs=dst_crs, geometry=[bbox_geom])
        # TODO: Allow acces to polygon dataframe
        self.roi = ROI(self.geology_file, self.fault_file,
                       self.structure_file, self.mindep_file, self.bbox[:4], c_l)


# def main():
#     proj = Project()
#     # print(proj.roi)
#     # print(proj.workflow)
#     print(proj)


# if __name__ == "__main__":
#     main()
