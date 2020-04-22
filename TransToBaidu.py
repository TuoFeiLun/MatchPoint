
from pyproj import CRS
from pyproj import Transformer
from urllib.request import urlopen
import json

'''
input  your coordinate system ，  transform to wgs-84 , 
but About Geographic Coordinate system trandform that only have Beijing_1954_To_WGS_1984_1 standard in present  

Unless  you are transform your Model Coordinate System to WGS-84 correctly ,  
you can transform your Model coordinate to baidu's ANY Coornidate system using Baidu Web API 

ak = '5ef7DaH5hSFwNDNMGyVbzUCC8bBGjGGT'
'''


class TransToBaiduC:

    def __init__(self, ak, model_wkid):
        self.ak = ak
        self.model_wkid = model_wkid


    def ModelXY_2_WGS(self, ModelX: float, ModelY: float) -> tuple:
        crsmodel = CRS.from_epsg(self.model_wkid)  # input your Coordinate

        crswgs = CRS.from_epsg(4326)  # WGS84 Geography EPSG

        transformer_1 = Transformer.from_crs(crsmodel, crswgs, always_xy=True)

        tup_result_1 = transformer_1.transform(ModelX, ModelY)

        return tup_result_1


    def wgs84_to_bd09(self, lng1, lat1) -> tuple:
        # transform from WGS1984 to baidu geography coordinate

        lng_lat = str(lng1)+','+str(lat1)
        coords = lng_lat
        from_cord = str(1)
        to_cord = str(5)
        url_1 = 'http://api.map.baidu.com/geoconv/v1/'
        uri_1 = url_1 + '?'+'coords='+coords+'&from='+from_cord+'&to='+to_cord+'&ak='+self.ak
        req_1 = urlopen(uri_1)
        res_1 = req_1.read()
        rtpe_cord = json.loads(res_1)
        #print(rtpe_cord)
        re_lg_lt = (rtpe_cord['result'][0]['x'],rtpe_cord['result'][0]['y'])

        print('wgs_2_baidu09:', re_lg_lt[0],  re_lg_lt[1])
        return re_lg_lt


    def wgs84_to_bd09mc(self, lng1, lat1) -> tuple:
        # transform from WGS1984 to baidu 09 project coordinate

        lng_lat = str(lng1)+','+str(lat1)
        coords = lng_lat
        from_cord = str(1)
        to_cord = str(6)
        url_1 = 'http://api.map.baidu.com/geoconv/v1/'
        uri_1 = url_1 + '?'+'coords='+coords+'&from='+from_cord+'&to='+to_cord+'&ak='+self.ak
        req_1 = urlopen(uri_1)
        res_1 = req_1.read()
        rtpe_cord = json.loads(res_1)
        #print(rtpe_cord)
        re_baidu_meter = (rtpe_cord['result'][0]['x'],rtpe_cord['result'][0]['y'])

        #print('wgs_2_baidu09mc:', re_baidu_meter[0],  re_baidu_meter[1])
        return re_baidu_meter


    def bd09_to_bd09mc(self, lng1, lat1) -> tuple:
        # transform baidu's longitude latitude to baidu's mercator project coordinate

        lng_lat_mc = str(lng1)+','+str(lat1)
        coords_mc = lng_lat_mc
        from_mc_cord = str(5)
        to_mc_cord = str(6)
        url_1 = 'http://api.map.baidu.com/geoconv/v1/'
        uri_mcbd = url_1 + '?'+'coords='+coords_mc+'&from='+from_mc_cord+'&to='+to_mc_cord+'&ak='+self.ak
        req_mcbd = urlopen(uri_mcbd)
        res_mcbd = req_mcbd.read()
        rtpe_mc_cord = json.loads(res_mcbd)
        bdmc = (rtpe_mc_cord['result'][0]['x'],rtpe_mc_cord['result'][0]['y'])

        print('baidu geography to baidu meters :', bdmc[0], bdmc[1])
        return bdmc


if __name__ == "__main__":
    pass




