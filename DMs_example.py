#Version 11_Nov_14

import numpy as np

dsmslist = ['apriori','colorIdio','raceIdio','sexIdio','idioAvg_sr']
# black,male,blue = A ; white,female,red = B, typ = 1, atyp = 2
order = ['A1','A2','B1','B2']

colorIdio = {
"424": np.array([[0,0.036773285,0.660823729,0.792894993],
[0.036773285,0,0.624050444,0.756121708],
[0.660823729,0.624050444,0,0.132071263],
[0.792894993,0.756121708,0.132071263,0]]),
"425": np.array([[0,0.025446939,0.63347252,0.631969767],
[0.025446939,0,0.658919459,0.657416706],
[0.63347252,0.658919459,0,0.001502753],
[0.631969767,0.657416706,0.001502753,0]]),
"426": np.array([[0,0.000682565,0.759982859,0.899470638],
[0.000682565,0,0.759300294,0.898788074],
[0.759982859,0.759300294,0,0.139487779],
[0.899470638,0.898788074,0.139487779,0]]),
"427": np.array([[0,0.136194139,0.520495023,0.519620071],
[0.136194139,0,0.384300884,0.383425932],
[0.520495023,0.384300884,0,0.000874952],
[0.519620071,0.383425932,0.000874952,0]]),
"428": np.array([[0,0.0203039,0.624922319,0.678481059],
[0.0203039,0,0.60461842,0.658177159],
[0.624922319,0.60461842,0,0.05355874],
[0.678481059,0.658177159,0.05355874,0]]),
"429": np.array([[0,0.018520325,0.724205134,0.737331419],
[0.018520325,0,0.742725459,0.755851743],
[0.724205134,0.742725459,0,0.013126284],
[0.737331419,0.755851743,0.013126284,0]]),
"430": np.array([[0,0.028240912,0.76837568,0.78866383],
[0.028240912,0,0.740134768,0.760422917],
[0.76837568,0.740134768,0,0.02028815],
[0.78866383,0.760422917,0.02028815,0]]),
"431": np.array([[0,0.001950307,0.866606817,0.846800518],
[0.001950307,0,0.868557124,0.848750824],
[0.866606817,0.868557124,0,0.019806299],
[0.846800518,0.848750824,0.019806299,0]]),
"432": np.array([[0,0.03438183,0.570200882,0.631168257],
[0.03438183,0,0.604582713,0.665550087],
[0.570200882,0.604582713,0,0.060967374],
[0.631168257,0.665550087,0.060967374,0]]),
"433": np.array([[0,0.02161686,0.774353757,0.907820848],
[0.02161686,0,0.795970616,0.929437708],
[0.774353757,0.795970616,0,0.133467091],
[0.907820848,0.929437708,0.133467091,0]]),
"434": np.array([[0,0.015530372,1.197818171,0.239750116],
[0.015530372,0,1.182287799,0.224219745],
[1.197818171,1.182287799,0,0.958068054],
[0.239750116,0.224219745,0.958068054,0]]),
"435": np.array([[0,0.012378848,0.691338201,0.645271325],
[0.012378848,0,0.703717049,0.657650173],
[0.691338201,0.703717049,0,0.046066876],
[0.645271325,0.657650173,0.046066876,0]]),
"436": np.array([[0,0.050593799,0.605722502,0.708619394],
[0.050593799,0,0.656316301,0.759213194],
[0.605722502,0.656316301,0,0.102896892],
[0.708619394,0.759213194,0.102896892,0]]),
"438": np.array([[0,0.138756151,0.074093114,0.115151061],
[0.138756151,0,0.212849265,0.253907212],
[0.074093114,0.212849265,0,0.041057947],
[0.115151061,0.253907212,0.041057947,0]]),
"439": np.array([[0,0.096816162,0.857351368,0.943782972],
[0.096816162,0,0.760535205,0.846966809],
[0.857351368,0.760535205,0,0.086431604],
[0.943782972,0.846966809,0.086431604,0]]),
"440": np.array([[0,0.005475084,0.542689075,0.622310879],
[0.005475084,0,0.537213991,0.616835795],
[0.542689075,0.537213991,0,0.079621804],
[0.622310879,0.616835795,0.079621804,0]]),
}

raceIdio = {
"424": np.array([[0,0.176138854,0.404195894,0.642934806],
[0.176138854,0,0.580334747,0.81907366],
[0.404195894,0.580334747,0,0.238738912],
[0.642934806,0.81907366,0.238738912,0]]),
"425": np.array([[0,0.040575141,0.594271803,0.858603312],
[0.040575141,0,0.553696662,0.818028171],
[0.594271803,0.553696662,0,0.264331509],
[0.858603312,0.818028171,0.264331509,0]]),
"426": np.array([[0,0.055657107,0.683721004,0.786792627],
[0.055657107,0,0.739378111,0.842449734],
[0.683721004,0.739378111,0,0.103071623],
[0.786792627,0.842449734,0.103071623,0]]),
"427": np.array([[0,0.112318604,0.568967374,0.713038978],
[0.112318604,0,0.681285978,0.825357582],
[0.568967374,0.681285978,0,0.144071604],
[0.713038978,0.825357582,0.144071604,0]]),
"428": np.array([[0,0.053424239,0.500486946,0.602885315],
[0.053424239,0,0.553911184,0.656309553],
[0.500486946,0.553911184,0,0.102398369],
[0.602885315,0.656309553,0.102398369,0]]),
"429": np.array([[0,0.154699996,0.617999644,0.712469986],
[0.154699996,0,0.77269964,0.867169982],
[0.617999644,0.77269964,0,0.094470342],
[0.712469986,0.867169982,0.094470342,0]]),
"430": np.array([[0,0.055829432,0.81363466,0.887422245],
[0.055829432,0,0.869464092,0.943251677],
[0.81363466,0.869464092,0,0.073787585],
[0.887422245,0.943251677,0.073787585,0]]),
"431": np.array([[0,0.006220873,0.786098179,0.764557612],
[0.006220873,0,0.792319053,0.770778485],
[0.786098179,0.792319053,0,0.021540568],
[0.764557612,0.770778485,0.021540568,0]]),
"432": np.array([[0,0.080823594,0.473204004,0.487119069],
[0.080823594,0,0.554027597,0.567942662],
[0.473204004,0.554027597,0,0.013915065],
[0.487119069,0.567942662,0.013915065,0]]),
"433": np.array([[0,0.266631106,0.751599853,0.758310526],
[0.266631106,0,1.018230959,1.024941632],
[0.751599853,1.018230959,0,0.006710672],
[0.758310526,1.024941632,0.006710672,0]]),
"434": np.array([[0,0.265008346,0.716606155,0.289864642],
[0.265008346,0,0.451597808,0.024856295],
[0.716606155,0.451597808,0,0.426741513],
[0.289864642,0.024856295,0.426741513,0]]),
"435": np.array([[0,0.083906649,0.623583677,0.65358081],
[0.083906649,0,0.707490326,0.737487459],
[0.623583677,0.707490326,0,0.029997133],
[0.65358081,0.737487459,0.029997133,0]]),
"436": np.array([[0,0.090033964,0.768389795,0.770075221],
[0.090033964,0,0.85842376,0.860109185],
[0.768389795,0.85842376,0,0.001685425],
[0.770075221,0.860109185,0.001685425,0]]),
"438": np.array([[0,0.195307382,0.256924917,0.332875997],
[0.195307382,0,0.452232299,0.528183379],
[0.256924917,0.452232299,0,0.075951081],
[0.332875997,0.528183379,0.075951081,0]]),
"439": np.array([[0,0.303888744,0.05127333,0.215980079],
[0.303888744,0,0.355162074,0.519868823],
[0.05127333,0.355162074,0,0.164706749],
[0.215980079,0.519868823,0.164706749,0]]),
"440": np.array([[0,0.146758438,0.356366458,0.438883637],
[0.146758438,0,0.503124895,0.585642075],
[0.356366458,0.503124895,0,0.08251718],
[0.438883637,0.585642075,0.08251718,0]]),
}

sexIdio = {
"424": np.array([[0,0.150103964,0.545343788,0.762123817],
[0.150103964,0,0.695447751,0.912227781],
[0.545343788,0.695447751,0,0.216780029],
[0.762123817,0.912227781,0.216780029,0]]),
"425": np.array([[0,0.150979584,0.316058734,0.44466631],
[0.150979584,0,0.467038318,0.595645894],
[0.316058734,0.467038318,0,0.128607576],
[0.44466631,0.595645894,0.128607576,0]]),
"426": np.array([[0,0.008642589,0.490850838,0.862657118],
[0.008642589,0,0.499493427,0.871299707],
[0.490850838,0.499493427,0,0.37180628],
[0.862657118,0.871299707,0.37180628,0]]),
"427": np.array([[0,0.125367707,0.314518424,0.491278711],
[0.125367707,0,0.439886132,0.616646418],
[0.314518424,0.439886132,0,0.176760287],
[0.491278711,0.616646418,0.176760287,0]]),
"428": np.array([[0,0.195239385,0.362364542,0.380082954],
[0.195239385,0,0.557603927,0.575322339],
[0.362364542,0.557603927,0,0.017718412],
[0.380082954,0.575322339,0.017718412,0]]),
"429": np.array([[0,0.006873055,0.694934192,0.791552688],
[0.006873055,0,0.688061136,0.784679632],
[0.694934192,0.688061136,0,0.096618496],
[0.791552688,0.784679632,0.096618496,0]]),
"430": np.array([[0,0.175204542,0.711412365,0.689104546],
[0.175204542,0,0.886616907,0.864309088],
[0.711412365,0.886616907,0,0.022307819],
[0.689104546,0.864309088,0.022307819,0]]),
"431": np.array([[0,0.065212204,0.796590018,0.801673141],
[0.065212204,0,0.861802222,0.866885344],
[0.796590018,0.861802222,0,0.005083122],
[0.801673141,0.866885344,0.005083122,0]]),
"432": np.array([[0,0.052973409,0.558899726,0.760554668],
[0.052973409,0,0.505926317,0.707581259],
[0.558899726,0.505926317,0,0.201654942],
[0.760554668,0.707581259,0.201654942,0]]),
"433": np.array([[0,0.319082756,0.573361603,0.544028968],
[0.319082756,0,0.892444359,0.863111724],
[0.573361603,0.892444359,0,0.029332635],
[0.544028968,0.863111724,0.029332635,0]]),
"434": np.array([[0,0.472452454,0.905270848,0.417764056],
[0.472452454,0,0.432818394,0.054688398],
[0.905270848,0.432818394,0,0.487506792],
[0.417764056,0.054688398,0.487506792,0]]),
"435": np.array([[0,0.057105171,0.614587441,0.71586752],
[0.057105171,0,0.671692613,0.772972691],
[0.614587441,0.671692613,0,0.101280078],
[0.71586752,0.772972691,0.101280078,0]]),
"436": np.array([[0,0.028207387,0.635492517,0.793345486],
[0.028207387,0,0.663699904,0.821552873],
[0.635492517,0.663699904,0,0.157852968],
[0.793345486,0.821552873,0.157852968,0]]),
"438": np.array([[0,0.029118245,0.471394557,0.685340443],
[0.029118245,0,0.442276311,0.656222198],
[0.471394557,0.442276311,0,0.213945887],
[0.685340443,0.656222198,0.213945887,0]]),
"439": np.array([[0,0.046261205,0.116316238,0.622085558],
[0.046261205,0,0.070055033,0.575824353],
[0.116316238,0.070055033,0,0.505769321],
[0.622085558,0.575824353,0.505769321,0]]),
"440": np.array([[0,0.150438543,0.216420993,0.445429261],
[0.150438543,0,0.366859536,0.595867803],
[0.216420993,0.366859536,0,0.229008268],
[0.445429261,0.595867803,0.229008268,0]]),
}

idioAvg_sr = {
"sex": np.array([[ 0.        ,  0.12707889,  0.52023855,  0.6379722 ],
       [ 0.12707889,  0.        ,  0.57135764,  0.69592734],
       [ 0.52023855,  0.57135764,  0.        ,  0.18512706],
       [ 0.6379722 ,  0.69592734,  0.18512706,  0.        ]]),
"race": np.array([[ 0.        ,  0.1304514 ,  0.56045773,  0.61971218],
       [ 0.1304514 ,  0.        ,  0.6527112 ,  0.71196565],
       [ 0.56045773,  0.6527112 ,  0.        ,  0.11528971],
       [ 0.61971218,  0.71196565,  0.11528971,  0.        ]]),
"color": np.array([[ 0.        ,  0.04022884,  0.6795282 ,  0.6693192 ],
       [ 0.04022884,  0.        ,  0.67725499,  0.66704599],
       [ 0.6795282 ,  0.67725499,  0.        ,  0.11808087],
       [ 0.6693192 ,  0.66704599,  0.11808087,  0.        ]])
}

apriori = {'apriori': np.array([[0,0.3333333333,1,0.6666666667],
[0.3333333333,0,0.6666666667,0.3333333333],
[1,0.6666666667,0,0.3333333333],
[0.6666666667,0.3333333333,0.3333333333,0]])}

#qa:
gl = globals()
print('DSMS qa:')
for dsm in dsmslist:
    print('\nDSM set: \'%s\'\n\nDSM | Shape | First | Last' % (dsm))
    for key,i in gl[dsm].iteritems():
        print key,i.shape,i[0][0],i[-1][-1]
