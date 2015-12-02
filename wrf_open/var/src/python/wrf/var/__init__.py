import warnings

from extension import *
import extension
from cape import *
import cape
from constants import *
import constants
from ctt import *
import ctt
from dbz import *
import dbz
from destagger import *
import destagger
from dewpoint import *
import dewpoint
from etaconv import *
import etaconv
from geoht import *
import geoht
from helicity import *
import helicity
from interp import *
import interp
from latlon import *
import latlon
from omega import *
import omega
from precip import *
import precip
from pressure import *
import pressure
from psadlookup import *
import psadlookup
from pw import *
import pw
from rh import *
import rh
from slp import *
import slp
from temp import *
import temp
from terrain import *
import terrain
from uvmet import *
import uvmet
from vorticity import *
import vorticity
from wind import *
import wind
from times import *
import times
from units import *
import units

__all__ = ["getvar"]
__all__ += extension.__all__
__all__ += cape.__all__
__all__ += constants.__all__
__all__ += ctt.__all__
__all__ += dbz.__all__
__all__ += destagger.__all__
__all__ += dewpoint.__all__
__all__ += etaconv.__all__
__all__ += geoht.__all__
__all__ += helicity.__all__
__all__ += interp.__all__
__all__ += latlon.__all__
__all__ += omega.__all__
__all__ += precip.__all__
__all__ += psadlookup.__all__
__all__ += pw.__all__
__all__ += rh.__all__
__all__ += slp.__all__
__all__ += temp.__all__
__all__ += terrain.__all__
__all__ += uvmet.__all__
__all__ += vorticity.__all__
__all__ += wind.__all__
__all__ += times.__all__
__all__ += pressure.__all__
__all__ += units.__all__

# func is the function to call.  kargs are required arguments that should 
# not be altered by the user
_FUNC_MAP = {"cape2d" : get_2dcape,
             "cape3d" : get_3dcape,
             "dbz" : get_dbz,
             "maxdbz" : get_max_dbz,
             "dp" : get_dp,
             "dp2m" : get_dp_2m, 
             "height" : get_height,
             "geopt" : get_geopt,
             "srh" : get_srh,
             "uhel" : get_uh,
             "omega" : get_omega,
             "pw" : get_pw,
             "rh" : get_rh, 
             "rh2m" : get_rh_2m, 
             "slp" : get_slp, 
             "theta" : get_theta,
             "temp" : get_temp, 
             "theta_e" : get_eth, 
             "tv" : get_tv, 
             "twb" : get_tw, 
             "terrain" : get_terrain,
             "times" : get_times, 
             "uvmet" : get_uvmet, 
             "uvmet10" : get_uvmet10,
             "avo" : get_avo,
             "pvo" : get_pvo,
             "ua" : get_u_destag, 
             "va" : get_v_destag,
             "wa" : get_w_destag,
             "lat" : get_lat,
             "lon" : get_lon,
             "pressure" : get_pressure,
             "wspddir" : get_destag_wspd_wdir,
             "wspddir_uvmet" : get_uvmet_wspd_wdir,
             "wspddir_uvmet10" : get_uvmet10_wspd_wdir,
             "ctt" : get_ctt
             }

_VALID_ARGS = {"cape2d" : ["missing", "timeidx"],
             "cape3d" : ["missing", "timeidx"],
             "dbz" : ["do_variant", "do_liqskin", "timeidx"],
             "maxdbz" : ["do_variant", "do_liqskin", "timeidx"],
             "dp" : ["timeidx", "units"],
             "dp2m" : ["timeidx", "units"], 
             "height" : ["msl", "units", "timeidx"],
             "geopt" : ["timeidx"],
             "srh" : ["top", "timeidx"],
             "uhel" : ["bottom", "top", "timeidx"],
             "omega" : ["timeidx"],
             "pw" : ["timeidx"],
             "rh" : ["timeidx"], 
             "rh2m" : ["timeidx"], 
             "slp" : ["units", "timeidx"], 
             "temp" : ["units", "timeidx"], 
             "theta" : ["units", "timeidx"],
             "theta_e" : ["timeidx", "units"], 
             "tv" : ["units", "timeidx"], 
             "twb" : ["units", "timeidx"], 
             "terrain" : ["units", "timeidx"],
             "times" : ["timeidx"], 
             "uvmet" : ["units", "timeidx"], 
             "uvmet10" : ["units", "timeidx"],
             "avo" : ["timeidx"],
             "pvo" : ["timeidx"],
             "ua" : ["units", "timeidx"], 
             "va" : ["units", "timeidx"],
             "wa" : ["units", "timeidx"],
             "lat" : ["timeidx"],
             "lon" : ["timeidx"],
             "pressure" : ["units", "timeidx"],
             "wspddir" : ["units", "timeidx"],
             "wspddir_uvmet" : ["units", "timeidx"],
             "wspddir_uvmet10" : ["units", "timeidx"],  
             "ctt" : ["timeidx"]
            }

_ALIASES = {"cape_2d" : "cape2d",
            "cape_3d" : "cape3d",
            "eth" : "theta_e",
            "mdbz" : "maxdbz",
            "geopotential" : "geopt",
            "helicity" : "srh",
            "latitude" : "lat",
            "longitude" : "lon",
            "omg" : "omega",
            "pres" : "pressure",
            "p" : "pressure",
            "rh2" : "rh2m",
            "z": "height",
            "ter" : "terrain",
            "updraft_helicity" : "uhel",
            "td" : "dp",
            "td2" : "dp2m"
            }

class ArgumentError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

def _undo_alias(alias):
    actual = _ALIASES.get(alias, None)
    if actual is None:
        return alias
    else:
        return actual

def _check_kargs(var, kargs):
    for arg, val in kargs.iteritems():
        if arg not in _VALID_ARGS[var]:
            raise ArgumentError("'%s' is an invalid keyword "
                          "argument for '%s" % (arg, var))
            

def getvar(wrfnc, var, **kargs):
    actual_var = _undo_alias(var)
    if actual_var not in _VALID_ARGS:
        raise ArgumentError("'%s' is not a valid variable name" % (var))
    
    _check_kargs(actual_var, kargs)
    return _FUNC_MAP[actual_var](wrfnc,**kargs)
    

    
    
    
    