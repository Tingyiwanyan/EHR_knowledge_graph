import numpy as np
import matplotlib.pyplot as plt


tp_rates = [0.0,
 0.014245014245014245,
 0.03418803418803419,
 0.04843304843304843,
 0.05982905982905983,
 0.06552706552706553,
 0.07692307692307693,
 0.09116809116809117,
 0.10541310541310542,
 0.1111111111111111,
 0.1168091168091168,
 0.1282051282051282,
 0.13105413105413105,
 0.13675213675213677,
 0.14814814814814814,
 0.15954415954415954,
 0.1623931623931624,
 0.16809116809116809,
 0.17663817663817663,
 0.1794871794871795,
 0.18233618233618235,
 0.1908831908831909,
 0.19373219373219372,
 0.2022792022792023,
 0.21367521367521367,
 0.2222222222222222,
 0.23076923076923078,
 0.2336182336182336,
 0.23931623931623933,
 0.24786324786324787,
 0.25071225071225073,
 0.2535612535612536,
 0.2535612535612536,
 0.25925925925925924,
 0.27350427350427353,
 0.2792022792022792,
 0.29914529914529914,
 0.301994301994302,
 0.301994301994302,
 0.30484330484330485,
 0.31054131054131057,
 0.31339031339031337,
 0.3162393162393162,
 0.3162393162393162,
 0.3247863247863248,
 0.3333333333333333,
 0.33618233618233617,
 0.33903133903133903,
 0.34472934472934474,
 0.35327635327635326,
 0.3646723646723647,
 0.36752136752136755,
 0.3789173789173789,
 0.3789173789173789,
 0.38461538461538464,
 0.38461538461538464,
 0.3903133903133903,
 0.39886039886039887,
 0.39886039886039887,
 0.39886039886039887,
 0.4017094017094017,
 0.4074074074074074,
 0.41595441595441596,
 0.41595441595441596,
 0.41595441595441596,
 0.4188034188034188,
 0.42450142450142453,
 0.43304843304843305,
 0.4415954415954416,
 0.45014245014245013,
 0.45584045584045585,
 0.45584045584045585,
 0.47293447293447294,
 0.4985754985754986,
 0.4985754985754986,
 0.5042735042735043,
 0.5128205128205128,
 0.5213675213675214,
 0.5384615384615384,
 0.5498575498575499,
 0.5612535612535613,
 0.5783475783475783,
 0.5868945868945868,
 0.6096866096866097,
 0.6210826210826211,
 0.6438746438746439,
 0.6581196581196581,
 0.6951566951566952,
 0.7321937321937322,
 0.7663817663817664,
 0.8062678062678063,
 0.8433048433048433,
 0.886039886039886,
 0.905982905982906,
 0.9373219373219374,
 0.9686609686609686,
 0.9886039886039886,
 0.9971509971509972,
 0.9971509971509972,
 1.0,
 1.0]

fp_rates = [0.0,
 0.0005586592178770949,
 0.0005586592178770949,
 0.0005586592178770949,
 0.0005586592178770949,
 0.0005586592178770949,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0022346368715083797,
 0.0022346368715083797,
 0.002793296089385475,
 0.002793296089385475,
 0.003910614525139665,
 0.0067039106145251395,
 0.0067039106145251395,
 0.0067039106145251395,
 0.007262569832402235,
 0.008379888268156424,
 0.008938547486033519,
 0.008938547486033519,
 0.008938547486033519,
 0.008938547486033519,
 0.009497206703910615,
 0.009497206703910615,
 0.009497206703910615,
 0.009497206703910615,
 0.01005586592178771,
 0.010614525139664804,
 0.010614525139664804,
 0.010614525139664804,
 0.010614525139664804,
 0.010614525139664804,
 0.010614525139664804,
 0.0111731843575419,
 0.0111731843575419,
 0.011731843575418994,
 0.011731843575418994,
 0.011731843575418994,
 0.012290502793296089,
 0.012849162011173185,
 0.013407821229050279,
 0.013966480446927373,
 0.013966480446927373,
 0.013966480446927373,
 0.015083798882681564,
 0.01564245810055866,
 0.016201117318435754,
 0.01675977653631285,
 0.01675977653631285,
 0.01675977653631285,
 0.017877094972067038,
 0.018435754189944135,
 0.02011173184357542,
 0.020670391061452513,
 0.021787709497206705,
 0.02346368715083799,
 0.024581005586592177,
 0.026256983240223464,
 0.027374301675977653,
 0.030167597765363128,
 0.030167597765363128,
 0.03128491620111732,
 0.0335195530726257,
 0.0335195530726257,
 0.03519553072625698,
 0.03798882681564246,
 0.04189944134078212,
 0.04581005586592179,
 0.048044692737430165,
 0.050837988826815644,
 0.054748603351955305,
 0.06201117318435754,
 0.0664804469273743,
 0.07039106145251396,
 0.07597765363128492,
 0.08435754189944134,
 0.09776536312849161,
 0.10670391061452514,
 0.12569832402234637,
 0.22737430167597766,
 0.3011173184357542,
 0.39385474860335196,
 0.49162011173184356,
 0.5793296089385475,
 0.6642458100558659,
 0.7508379888268156,
 0.8262569832402235,
 0.8927374301675978,
 0.9513966480446927,
 0.9770949720670391,
 0.9932960893854749,
 0.9983240223463687,
 1.0]

tp_rates_CL = [0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.002849002849002849,
 0.014245014245014245,
 0.03133903133903134,
 0.11965811965811966,
 0.18518518518518517,
 0.23646723646723647,
 0.28774928774928776,
 0.3162393162393162,
 0.3475783475783476,
 0.36752136752136755,
 0.38746438746438744,
 0.3903133903133903,
 0.4074074074074074,
 0.4188034188034188,
 0.42450142450142453,
 0.4301994301994302,
 0.43304843304843305,
 0.4444444444444444,
 0.45014245014245013,
 0.45584045584045585,
 0.45584045584045585,
 0.46153846153846156,
 0.4700854700854701,
 0.4700854700854701,
 0.4700854700854701,
 0.4700854700854701,
 0.4757834757834758,
 0.47863247863247865,
 0.48148148148148145,
 0.48148148148148145,
 0.4843304843304843,
 0.49002849002849,
 0.49002849002849,
 0.49002849002849,
 0.49002849002849,
 0.4928774928774929,
 0.49572649572649574,
 0.49572649572649574,
 0.49572649572649574,
 0.4985754985754986,
 0.5014245014245015,
 0.5014245014245015,
 0.5042735042735043,
 0.5071225071225072,
 0.5071225071225072,
 0.5071225071225072,
 0.5128205128205128,
 0.5128205128205128,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5156695156695157,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5185185185185185,
 0.5213675213675214,
 0.5213675213675214,
 0.5242165242165242,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5299145299145299,
 0.5299145299145299,
 0.5299145299145299,
 0.5327635327635327,
 0.5384615384615384,
 0.5384615384615384,
 0.5384615384615384,
 0.5384615384615384,
 0.5384615384615384,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5413105413105413,
 0.5441595441595442,
 0.5470085470085471,
 0.5498575498575499,
 0.5498575498575499,
 0.5498575498575499,
 0.5527065527065527,
 0.5555555555555556,
 0.5555555555555556,
 0.5612535612535613,
 0.5612535612535613,
 0.5612535612535613,
 0.5612535612535613,
 0.5612535612535613,
 0.5641025641025641,
 0.5669515669515669,
 0.5669515669515669,
 0.5698005698005698,
 0.5698005698005698,
 0.5698005698005698,
 0.5698005698005698,
 0.5698005698005698,
 0.5726495726495726,
 0.5754985754985755,
 0.5754985754985755,
 0.5754985754985755,
 0.5754985754985755,
 0.5754985754985755,
 0.5754985754985755,
 0.5754985754985755,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5783475783475783,
 0.5811965811965812,
 0.5811965811965812,
 0.584045584045584,
 0.584045584045584,
 0.584045584045584,
 0.584045584045584,
 0.584045584045584,
 0.5868945868945868,
 0.5897435897435898,
 0.5925925925925926,
 0.5954415954415955,
 0.5954415954415955,
 0.5954415954415955,
 0.6011396011396012,
 0.603988603988604,
 0.603988603988604,
 0.6068376068376068,
 0.6096866096866097,
 0.6125356125356125,
 0.6125356125356125,
 0.6210826210826211,
 0.6210826210826211,
 0.6296296296296297,
 0.6296296296296297,
 0.6353276353276354,
 0.6438746438746439,
 0.6524216524216524,
 0.6552706552706553,
 0.6609686609686609,
 0.6695156695156695,
 0.6723646723646723,
 0.6866096866096866,
 0.6951566951566952,
 0.698005698005698,
 0.7150997150997151,
 0.7407407407407407,
 0.7863247863247863,
 0.8062678062678063,
 0.9857549857549858,
 0.9971509971509972,
 0.9971509971509972,
 0.9971509971509972,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0]

fp_rates_cl = [0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0005586592178770949,
 0.002793296089385475,
 0.010614525139664804,
 0.015083798882681564,
 0.020670391061452513,
 0.022905027932960894,
 0.025139664804469275,
 0.026815642458100558,
 0.027932960893854747,
 0.02905027932960894,
 0.02905027932960894,
 0.03128491620111732,
 0.03240223463687151,
 0.0335195530726257,
 0.034636871508379886,
 0.03687150837988827,
 0.037430167597765365,
 0.038547486033519554,
 0.04078212290502793,
 0.041340782122905026,
 0.041340782122905026,
 0.04189944134078212,
 0.04189944134078212,
 0.04189944134078212,
 0.043016759776536316,
 0.043016759776536316,
 0.04357541899441341,
 0.044134078212290505,
 0.044134078212290505,
 0.044134078212290505,
 0.044134078212290505,
 0.04581005586592179,
 0.04581005586592179,
 0.04581005586592179,
 0.04636871508379888,
 0.04636871508379888,
 0.04636871508379888,
 0.04692737430167598,
 0.04692737430167598,
 0.04748603351955307,
 0.04748603351955307,
 0.048044692737430165,
 0.048044692737430165,
 0.049162011173184354,
 0.049162011173184354,
 0.049162011173184354,
 0.049720670391061456,
 0.049720670391061456,
 0.049720670391061456,
 0.05027932960893855,
 0.050837988826815644,
 0.05139664804469274,
 0.05139664804469274,
 0.05139664804469274,
 0.05139664804469274,
 0.05139664804469274,
 0.05139664804469274,
 0.05139664804469274,
 0.05195530726256983,
 0.05195530726256983,
 0.05195530726256983,
 0.05251396648044693,
 0.05251396648044693,
 0.05251396648044693,
 0.05251396648044693,
 0.05307262569832402,
 0.05307262569832402,
 0.05307262569832402,
 0.05418994413407821,
 0.05418994413407821,
 0.05418994413407821,
 0.05418994413407821,
 0.05418994413407821,
 0.054748603351955305,
 0.054748603351955305,
 0.054748603351955305,
 0.054748603351955305,
 0.054748603351955305,
 0.0553072625698324,
 0.0553072625698324,
 0.0553072625698324,
 0.055865921787709494,
 0.055865921787709494,
 0.056424581005586595,
 0.056424581005586595,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.057541899441340784,
 0.05810055865921788,
 0.05810055865921788,
 0.05865921787709497,
 0.05977653631284916,
 0.05977653631284916,
 0.05977653631284916,
 0.05977653631284916,
 0.060335195530726256,
 0.06201117318435754,
 0.06256983240223464,
 0.06256983240223464,
 0.06256983240223464,
 0.06256983240223464,
 0.06256983240223464,
 0.06256983240223464,
 0.06312849162011173,
 0.06312849162011173,
 0.06312849162011173,
 0.06312849162011173,
 0.06312849162011173,
 0.06368715083798883,
 0.06368715083798883,
 0.06424581005586592,
 0.06424581005586592,
 0.06424581005586592,
 0.06424581005586592,
 0.06480446927374302,
 0.06536312849162011,
 0.06536312849162011,
 0.0670391061452514,
 0.0670391061452514,
 0.06759776536312849,
 0.06815642458100558,
 0.06871508379888268,
 0.06871508379888268,
 0.06871508379888268,
 0.06871508379888268,
 0.06983240223463687,
 0.07094972067039106,
 0.07094972067039106,
 0.07094972067039106,
 0.07262569832402235,
 0.07262569832402235,
 0.07374301675977654,
 0.07541899441340782,
 0.07597765363128492,
 0.0776536312849162,
 0.0776536312849162,
 0.0776536312849162,
 0.07877094972067039,
 0.07877094972067039,
 0.07932960893854749,
 0.07988826815642458,
 0.07988826815642458,
 0.08044692737430167,
 0.08156424581005586,
 0.08212290502793296,
 0.08212290502793296,
 0.08268156424581005,
 0.08435754189944134,
 0.08491620111731843,
 0.08491620111731843,
 0.08659217877094973,
 0.0893854748603352,
 0.09273743016759776,
 0.09385474860335195,
 0.09497206703910614,
 0.09832402234636871,
 0.09888268156424582,
 0.10167597765363129,
 0.10446927374301676,
 0.10782122905027933,
 0.10837988826815642,
 0.11340782122905028,
 0.11899441340782123,
 0.12067039106145251,
 0.12513966480446928,
 0.12849162011173185,
 0.1329608938547486,
 0.13631284916201117,
 0.14469273743016758,
 0.15418994413407822,
 0.1653631284916201,
 0.18044692737430168,
 0.20391061452513967,
 0.23519553072625698,
 0.3016759776536313,
 0.9363128491620112,
 0.9905027932960894,
 0.9983240223463687,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0]

tp_rate_ce_retain=[0.0,
 0.011396011396011397,
 0.037037037037037035,
 0.04843304843304843,
 0.06267806267806268,
 0.07122507122507123,
 0.07122507122507123,
 0.08262108262108261,
 0.08547008547008547,
 0.09116809116809117,
 0.09686609686609686,
 0.10541310541310542,
 0.1111111111111111,
 0.1111111111111111,
 0.1225071225071225,
 0.12535612535612536,
 0.14245014245014245,
 0.14814814814814814,
 0.15384615384615385,
 0.15954415954415954,
 0.16524216524216523,
 0.16809116809116809,
 0.17663817663817663,
 0.1794871794871795,
 0.18233618233618235,
 0.18518518518518517,
 0.1908831908831909,
 0.19658119658119658,
 0.20512820512820512,
 0.21367521367521367,
 0.21367521367521367,
 0.21652421652421652,
 0.22792022792022792,
 0.23076923076923078,
 0.23646723646723647,
 0.23931623931623933,
 0.23931623931623933,
 0.24216524216524216,
 0.24786324786324787,
 0.25071225071225073,
 0.2535612535612536,
 0.25925925925925924,
 0.26495726495726496,
 0.2678062678062678,
 0.2678062678062678,
 0.27350427350427353,
 0.27635327635327633,
 0.2792022792022792,
 0.2792022792022792,
 0.28205128205128205,
 0.29914529914529914,
 0.301994301994302,
 0.301994301994302,
 0.30484330484330485,
 0.31339031339031337,
 0.3162393162393162,
 0.3247863247863248,
 0.33048433048433046,
 0.33048433048433046,
 0.3333333333333333,
 0.34472934472934474,
 0.35327635327635326,
 0.3646723646723647,
 0.36752136752136755,
 0.3732193732193732,
 0.3817663817663818,
 0.38461538461538464,
 0.39316239316239315,
 0.4017094017094017,
 0.4131054131054131,
 0.4188034188034188,
 0.42450142450142453,
 0.42735042735042733,
 0.43874643874643876,
 0.45014245014245013,
 0.46438746438746437,
 0.4700854700854701,
 0.49002849002849,
 0.4985754985754986,
 0.5042735042735043,
 0.5242165242165242,
 0.5384615384615384,
 0.5641025641025641,
 0.5783475783475783,
 0.6239316239316239,
 0.6609686609686609,
 0.6951566951566952,
 0.7094017094017094,
 0.7435897435897436,
 0.7749287749287749,
 0.7948717948717948,
 0.8290598290598291,
 0.8575498575498576,
 0.8746438746438746,
 0.8974358974358975,
 0.9202279202279202,
 0.9458689458689459,
 0.9686609686609686,
 0.9886039886039886,
 0.9943019943019943,
 1.0]

fp_rates_ce_retain=[0.0,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0011173184357541898,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0016759776536312849,
 0.0022346368715083797,
 0.0022346368715083797,
 0.002793296089385475,
 0.002793296089385475,
 0.003910614525139665,
 0.003910614525139665,
 0.004469273743016759,
 0.004469273743016759,
 0.004469273743016759,
 0.005027932960893855,
 0.005027932960893855,
 0.005027932960893855,
 0.005027932960893855,
 0.005027932960893855,
 0.006145251396648044,
 0.006145251396648044,
 0.0067039106145251395,
 0.007262569832402235,
 0.00782122905027933,
 0.008379888268156424,
 0.008379888268156424,
 0.008938547486033519,
 0.008938547486033519,
 0.009497206703910615,
 0.009497206703910615,
 0.009497206703910615,
 0.009497206703910615,
 0.01005586592178771,
 0.010614525139664804,
 0.011731843575418994,
 0.012290502793296089,
 0.012849162011173185,
 0.012849162011173185,
 0.012849162011173185,
 0.012849162011173185,
 0.013407821229050279,
 0.013966480446927373,
 0.013966480446927373,
 0.015083798882681564,
 0.015083798882681564,
 0.017318435754189943,
 0.017877094972067038,
 0.01899441340782123,
 0.019553072625698324,
 0.020670391061452513,
 0.020670391061452513,
 0.021229050279329607,
 0.0223463687150838,
 0.02346368715083799,
 0.025139664804469275,
 0.027374301675977653,
 0.029608938547486034,
 0.030167597765363128,
 0.030167597765363128,
 0.03240223463687151,
 0.035754189944134075,
 0.037430167597765365,
 0.038547486033519554,
 0.03966480446927374,
 0.041340782122905026,
 0.04636871508379888,
 0.04860335195530726,
 0.05027932960893855,
 0.05307262569832402,
 0.06256983240223464,
 0.10502793296089385,
 0.12849162011173185,
 0.2245810055865922,
 0.31787709497206706,
 0.3715083798882682,
 0.4251396648044693,
 0.4798882681564246,
 0.5268156424581005,
 0.5748603351955307,
 0.6284916201117319,
 0.6670391061452514,
 0.7162011173184357,
 0.7737430167597765,
 0.8346368715083798,
 0.894413407821229,
 0.9368715083798883,
 0.976536312849162,
 0.9916201117318436,
 1.0]

tp_rates_CL_RNN = [0.0,
 0.0,
 0.0,
 0.0,
 0.008547008547008548,
 0.019943019943019943,
 0.07407407407407407,
 0.1168091168091168,
 0.1794871794871795,
 0.22507122507122507,
 0.27350427350427353,
 0.3076923076923077,
 0.33903133903133903,
 0.35327635327635326,
 0.38746438746438744,
 0.4074074074074074,
 0.42165242165242167,
 0.42450142450142453,
 0.43304843304843305,
 0.4444444444444444,
 0.452991452991453,
 0.4586894586894587,
 0.46438746438746437,
 0.46438746438746437,
 0.46438746438746437,
 0.4700854700854701,
 0.4757834757834758,
 0.47863247863247865,
 0.47863247863247865,
 0.48148148148148145,
 0.49002849002849,
 0.49002849002849,
 0.4928774928774929,
 0.4985754985754986,
 0.5014245014245015,
 0.5014245014245015,
 0.5014245014245015,
 0.5014245014245015,
 0.5014245014245015,
 0.5042735042735043,
 0.5042735042735043,
 0.5042735042735043,
 0.5071225071225072,
 0.5071225071225072,
 0.50997150997151,
 0.5128205128205128,
 0.5128205128205128,
 0.5128205128205128,
 0.5156695156695157,
 0.5213675213675214,
 0.5242165242165242,
 0.5242165242165242,
 0.5242165242165242,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5270655270655271,
 0.5299145299145299,
 0.5327635327635327,
 0.5356125356125356,
 0.5356125356125356,
 0.5384615384615384,
 0.5384615384615384,
 0.5384615384615384,
 0.5413105413105413,
 0.5441595441595442,
 0.5470085470085471,
 0.5470085470085471,
 0.5470085470085471,
 0.5527065527065527,
 0.5527065527065527,
 0.5527065527065527,
 0.5555555555555556,
 0.5555555555555556,
 0.5555555555555556,
 0.5555555555555556,
 0.5555555555555556,
 0.5555555555555556,
 0.5555555555555556,
 0.5584045584045584,
 0.5584045584045584,
 0.5584045584045584,
 0.5584045584045584,
 0.5584045584045584,
 0.5612535612535613,
 0.5612535612535613,
 0.5641025641025641,
 0.5641025641025641,
 0.5669515669515669,
 0.5726495726495726,
 0.5754985754985755,
 0.5783475783475783,
 0.5783475783475783,
 0.5811965811965812,
 0.584045584045584,
 0.584045584045584,
 0.584045584045584,
 0.584045584045584,
 0.5925925925925926,
 0.5925925925925926,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.5982905982905983,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.6011396011396012,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.603988603988604,
 0.6068376068376068,
 0.6068376068376068,
 0.6068376068376068,
 0.6068376068376068,
 0.6096866096866097,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6153846153846154,
 0.6182336182336182,
 0.6182336182336182,
 0.6182336182336182,
 0.6210826210826211,
 0.6210826210826211,
 0.6210826210826211,
 0.6239316239316239,
 0.6239316239316239,
 0.6267806267806267,
 0.6267806267806267,
 0.6267806267806267,
 0.6296296296296297,
 0.6296296296296297,
 0.6296296296296297,
 0.6353276353276354,
 0.6381766381766382,
 0.6381766381766382,
 0.6381766381766382,
 0.6381766381766382,
 0.6410256410256411,
 0.6410256410256411,
 0.6410256410256411,
 0.6410256410256411,
 0.6410256410256411,
 0.6410256410256411,
 0.6438746438746439,
 0.6438746438746439,
 0.6495726495726496,
 0.6495726495726496,
 0.6552706552706553,
 0.6552706552706553,
 0.6552706552706553,
 0.6552706552706553,
 0.6552706552706553,
 0.6609686609686609,
 0.6638176638176638,
 0.6638176638176638,
 0.6695156695156695,
 0.6695156695156695,
 0.6752136752136753,
 0.6780626780626781,
 0.6837606837606838,
 0.6837606837606838,
 0.6923076923076923,
 0.698005698005698,
 0.7065527065527065,
 0.7264957264957265,
 0.7720797720797721,
 0.8233618233618234,
 0.9857549857549858,
 0.9971509971509972,
 1.0,
 1.0,
 1.0,
 1.0]

fp_rates_cl_RNN = [0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0011173184357541898,
 0.0022346368715083797,
 0.006145251396648044,
 0.0067039106145251395,
 0.0067039106145251395,
 0.007262569832402235,
 0.008379888268156424,
 0.008379888268156424,
 0.009497206703910615,
 0.009497206703910615,
 0.009497206703910615,
 0.01005586592178771,
 0.01005586592178771,
 0.010614525139664804,
 0.010614525139664804,
 0.010614525139664804,
 0.012290502793296089,
 0.012290502793296089,
 0.013407821229050279,
 0.01564245810055866,
 0.016201117318435754,
 0.01675977653631285,
 0.018435754189944135,
 0.018435754189944135,
 0.018435754189944135,
 0.018435754189944135,
 0.018435754189944135,
 0.018435754189944135,
 0.01899441340782123,
 0.01899441340782123,
 0.01899441340782123,
 0.019553072625698324,
 0.019553072625698324,
 0.02011173184357542,
 0.02011173184357542,
 0.02011173184357542,
 0.02011173184357542,
 0.02011173184357542,
 0.020670391061452513,
 0.021229050279329607,
 0.021229050279329607,
 0.021787709497206705,
 0.0223463687150838,
 0.0223463687150838,
 0.0223463687150838,
 0.0223463687150838,
 0.022905027932960894,
 0.022905027932960894,
 0.02346368715083799,
 0.02346368715083799,
 0.02346368715083799,
 0.02346368715083799,
 0.024022346368715083,
 0.024581005586592177,
 0.025139664804469275,
 0.025139664804469275,
 0.02569832402234637,
 0.02569832402234637,
 0.02569832402234637,
 0.026256983240223464,
 0.026815642458100558,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.027932960893854747,
 0.028491620111731845,
 0.02905027932960894,
 0.02905027932960894,
 0.029608938547486034,
 0.029608938547486034,
 0.029608938547486034,
 0.029608938547486034,
 0.030167597765363128,
 0.030726256983240222,
 0.030726256983240222,
 0.030726256983240222,
 0.03128491620111732,
 0.03128491620111732,
 0.03128491620111732,
 0.031843575418994415,
 0.031843575418994415,
 0.0329608938547486,
 0.0329608938547486,
 0.0329608938547486,
 0.0335195530726257,
 0.0335195530726257,
 0.03407821229050279,
 0.034636871508379886,
 0.03519553072625698,
 0.03519553072625698,
 0.035754189944134075,
 0.035754189944134075,
 0.035754189944134075,
 0.035754189944134075,
 0.036312849162011177,
 0.03687150837988827,
 0.03798882681564246,
 0.03798882681564246,
 0.03798882681564246,
 0.038547486033519554,
 0.038547486033519554,
 0.038547486033519554,
 0.03910614525139665,
 0.03966480446927374,
 0.04022346368715084,
 0.041340782122905026,
 0.041340782122905026,
 0.041340782122905026,
 0.04189944134078212,
 0.04189944134078212,
 0.04189944134078212,
 0.043016759776536316,
 0.043016759776536316,
 0.04357541899441341,
 0.044134078212290505,
 0.044134078212290505,
 0.0446927374301676,
 0.0446927374301676,
 0.0446927374301676,
 0.0446927374301676,
 0.0446927374301676,
 0.04581005586592179,
 0.04581005586592179,
 0.04581005586592179,
 0.04692737430167598,
 0.04692737430167598,
 0.04692737430167598,
 0.04748603351955307,
 0.04748603351955307,
 0.048044692737430165,
 0.049720670391061456,
 0.05139664804469274,
 0.05139664804469274,
 0.05195530726256983,
 0.05195530726256983,
 0.05251396648044693,
 0.05307262569832402,
 0.05307262569832402,
 0.05307262569832402,
 0.056424581005586595,
 0.05698324022346369,
 0.05865921787709497,
 0.05865921787709497,
 0.05865921787709497,
 0.05921787709497207,
 0.05921787709497207,
 0.05977653631284916,
 0.05977653631284916,
 0.06089385474860335,
 0.06201117318435754,
 0.06312849162011173,
 0.0659217877094972,
 0.0670391061452514,
 0.06815642458100558,
 0.06927374301675977,
 0.07039106145251396,
 0.07039106145251396,
 0.07318435754189945,
 0.07486033519553073,
 0.07653631284916201,
 0.0776536312849162,
 0.07932960893854749,
 0.08100558659217877,
 0.08435754189944134,
 0.08659217877094973,
 0.08770949720670392,
 0.09273743016759776,
 0.09664804469273743,
 0.10558659217877095,
 0.11173184357541899,
 0.12513966480446928,
 0.1435754189944134,
 0.16871508379888267,
 0.20279329608938548,
 0.2871508379888268,
 0.49441340782122906,
 0.9754189944134078,
 0.9977653631284916,
 1.0,
 1.0,
 1.0,
 1.0]

plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ICU Transfer Prediction", fontsize=14)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
x = [0.0, 1.0]
plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

plt.plot(fp_rates, tp_rates, color='green', linewidth=1, label='RNN+CE(AUC=0.794)')


plt.plot(fp_rates_ce_retain,tp_rate_ce_retain,color='blue',label='RETAIN+CE(AUC=0.759)')

#plt.plot(fp_rate_hl_retain,tp_rate_hl_retain,color='orange',label='RETAIN+HL')

plt.plot(fp_rates_cl_RNN,tp_rates_CL_RNN,color='violet',label='RNN+CL(AUC=0.816)')
plt.plot(fp_rates_cl, tp_rates_CL, color='red', linewidth=1, label='RETAIN+CL(AUC=0.823)')


plt.legend(loc='lower right')
plt.show()