import numpy as np
import matplotlib.pyplot as plt


tp_rates = [1.0,
 0.961651376146789,
 0.9278899082568807,
 0.8941284403669725,
 0.8874311926605505,
 0.8399082568807339,
 0.8186238532110092,
 0.7819266055045872,
 0.7339449541284404,
 0.7064220183486238,
 0.6605504587155964,
 0.6513761467889908,
 0.6376146788990825,
 0.6376146788990825,
 0.6330275229357798,
 0.6330275229357798,
 0.6238532110091743,
 0.6100917431192661,
 0.6009174311926605,
 0.5963302752293578,
 0.591743119266055,
 0.5825688073394495,
 0.5779816513761468,
 0.5688073394495413,
 0.5688073394495413,
 0.5642201834862385,
 0.5596330275229358,
 0.5229357798165137,
 0.5229357798165137,
 0.5137614678899083,
 0.5045871559633027,
 0.5,
 0.4954128440366973,
 0.48623853211009177,
 0.47706422018348627,
 0.46788990825688076,
 0.46788990825688076,
 0.4541284403669725,
 0.44495412844036697,
 0.44036697247706424,
 0.43119266055045874,
 0.43119266055045874,
 0.41743119266055045,
 0.41284403669724773,
 0.3944954128440367,
 0.3853211009174312,
 0.38073394495412843,
 0.3669724770642202,
 0.3623853211009174,
 0.3577981651376147,
 0.3577981651376147,
 0.3532110091743119,
 0.3486238532110092,
 0.3348623853211009,
 0.3211009174311927,
 0.3119266055045872,
 0.30275229357798167,
 0.2981651376146789,
 0.29357798165137616,
 0.28440366972477066,
 0.28440366972477066,
 0.28440366972477066,
 0.27522935779816515,
 0.27522935779816515,
 0.26605504587155965,
 0.26146788990825687,
 0.25688073394495414,
 0.23394495412844038,
 0.22935779816513763,
 0.22477064220183487,
 0.21559633027522937,
 0.21559633027522937,
 0.21559633027522937,
 0.21100917431192662,
 0.20642201834862386,
 0.20642201834862386,
 0.19724770642201836,
 0.1926605504587156,
 0.1834862385321101,
 0.1743119266055046,
 0.16972477064220184,
 0.1651376146788991,
 0.1559633027522936,
 0.15137614678899083,
 0.14220183486238533,
 0.13761467889908258,
 0.13302752293577982,
 0.12385321100917432,
 0.11009174311926606,
 0.09174311926605505,
 0.09174311926605505,
 0.0871559633027523,
 0.08256880733944955,
 0.08256880733944955,
 0.0779816513761468,
 0.05504587155963303,
 0.05045871559633028,
 0.05045871559633028,
 0.045871559633027525,
 0.04128440366972477,
 0.0]

fp_rates = [0.9942797711908476,
 0.7862714508580343,
 0.7264690587623505,
 0.671866874674987,
 0.5990639625585024,
 0.516900676027041,
 0.4253770150806032,
 0.30577223088923555,
 0.1830473218928757,
 0.14248569942797712,
 0.08060322412896516,
 0.07384295371814872,
 0.0686427457098284,
 0.06500260010400416,
 0.06032241289651586,
 0.057722308892355696,
 0.0530421216848674,
 0.0514820592823713,
 0.0499219968798752,
 0.04784191367654706,
 0.045761830473218926,
 0.041081643265730626,
 0.0374414976599064,
 0.03692147685907436,
 0.036401456058242326,
 0.03380135205408216,
 0.03224128965158606,
 0.030681227249089962,
 0.029641185647425898,
 0.0265210608424337,
 0.024440977639105563,
 0.02392095683827353,
 0.02392095683827353,
 0.0218408736349454,
 0.0218408736349454,
 0.02080083203328133,
 0.018200728029121163,
 0.0171606864274571,
 0.01612064482579303,
 0.01612064482579303,
 0.015600624024960999,
 0.015080603224128965,
 0.015080603224128965,
 0.015080603224128965,
 0.013520540821632865,
 0.013000520020800831,
 0.011960478419136765,
 0.011960478419136765,
 0.011960478419136765,
 0.011960478419136765,
 0.011960478419136765,
 0.011960478419136765,
 0.011440457618304731,
 0.0109204368174727,
 0.009880395215808632,
 0.0093603744149766,
 0.0093603744149766,
 0.0093603744149766,
 0.008840353614144566,
 0.008840353614144566,
 0.008320332813312533,
 0.0078003120124804995,
 0.0078003120124804995,
 0.007280291211648466,
 0.007280291211648466,
 0.0062402496099844,
 0.005720228809152366,
 0.005200208008320333,
 0.005200208008320333,
 0.005200208008320333,
 0.005200208008320333,
 0.0046801872074883,
 0.004160166406656267,
 0.004160166406656267,
 0.004160166406656267,
 0.004160166406656267,
 0.003640145605824233,
 0.003640145605824233,
 0.003640145605824233,
 0.0031201248049922,
 0.0031201248049922,
 0.0031201248049922,
 0.0031201248049922,
 0.0031201248049922,
 0.0031201248049922,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0020800832033281333,
 0.0015600624024961,
 0.0015600624024961,
 0.0010400416016640667,
 0.0]

tp_rates_CL = []

fp_rates_cl = []

tp_rate_ce_retain= []

fp_rates_ce_retain=[]


tp_rates_CL_RNN = [1.0,
 1.0,
 0.7798165137614679,
 0.7568807339449541,
 0.7522935779816514,
 0.7522935779816514,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7339449541284404,
 0.7339449541284404,
 0.7339449541284404,
 0.7293577981651376,
 0.7201834862385321,
 0.7201834862385321,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7155963302752294,
 0.7110091743119266,
 0.7110091743119266,
 0.7110091743119266,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.7018348623853211,
 0.6972477064220184,
 0.6972477064220184,
 0.6926605504587156,
 0.6926605504587156,
 0.6926605504587156,
 0.6926605504587156,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6880733944954128,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6743119266055045,
 0.6743119266055045,
 0.6743119266055045,
 0.6743119266055045,
 0.6743119266055045,
 0.6743119266055045,
 0.6743119266055045,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6697247706422018,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6651376146788991,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6559633027522935,
 0.6513761467889908,
 0.6513761467889908,
 0.6422018348623854,
 0.6422018348623854,
 0.6422018348623854,
 0.6376146788990825,
 0.6238532110091743,
 0.6100917431192661,
 0.5963302752293578,
 0.5642201834862385,
 0.5321100917431193,
 0.4908256880733945,
 0.44954128440366975,
 0.37155963302752293,
 0.3073394495412844,
 0.1834862385321101,
 0.0]

fp_rates_cl_RNN = [1.0,
 1.0,
 0.22568902756110246,
 0.15912636505460218,
 0.13000520020800832,
 0.11128445137805512,
 0.10244409776391056,
 0.09152366094643785,
 0.08476339053562143,
 0.07748309932397296,
 0.07384295371814872,
 0.07020280811232449,
 0.06604264170566823,
 0.06344253770150807,
 0.06292251690067603,
 0.06188247529901196,
 0.06032241289651586,
 0.05876235049401976,
 0.05720228809152366,
 0.056162246489859596,
 0.054602184087363496,
 0.0530421216848674,
 0.05252210088403536,
 0.052002080083203325,
 0.052002080083203325,
 0.0514820592823713,
 0.05096203848153926,
 0.050442017680707225,
 0.048881955278211126,
 0.048881955278211126,
 0.048881955278211126,
 0.0483619344773791,
 0.0483619344773791,
 0.0483619344773791,
 0.04784191367654706,
 0.047321892875715026,
 0.046801872074883,
 0.04628185127405096,
 0.045761830473218926,
 0.045761830473218926,
 0.04472178887155486,
 0.044201768070722826,
 0.044201768070722826,
 0.044201768070722826,
 0.04316172646905876,
 0.042641705668226726,
 0.0421216848673947,
 0.04160166406656266,
 0.041081643265730626,
 0.04004160166406656,
 0.0390015600624025,
 0.0390015600624025,
 0.037961518460738426,
 0.0374414976599064,
 0.03692147685907436,
 0.03692147685907436,
 0.03692147685907436,
 0.036401456058242326,
 0.0358814352574103,
 0.0358814352574103,
 0.0358814352574103,
 0.0358814352574103,
 0.0358814352574103,
 0.0358814352574103,
 0.0358814352574103,
 0.03536141445657826,
 0.03536141445657826,
 0.034841393655746226,
 0.034841393655746226,
 0.034841393655746226,
 0.034841393655746226,
 0.034841393655746226,
 0.034841393655746226,
 0.034841393655746226,
 0.0343213728549142,
 0.0343213728549142,
 0.0343213728549142,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.03380135205408216,
 0.0327613104524181,
 0.03224128965158606,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031721268850754034,
 0.031201248049921998,
 0.03016120644825793,
 0.029641185647425898,
 0.029121164846593862,
 0.027561102444097763,
 0.0265210608424337,
 0.0265210608424337,
 0.0265210608424337,
 0.0265210608424337,
 0.0265210608424337,
 0.0265210608424337,
 0.026001040041601663,
 0.026001040041601663,
 0.026001040041601663,
 0.026001040041601663,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.02548101924076963,
 0.0249609984399376,
 0.024440977639105563,
 0.024440977639105563,
 0.02392095683827353,
 0.0234009360374415,
 0.0234009360374415,
 0.0234009360374415,
 0.0234009360374415,
 0.0234009360374415,
 0.022880915236609463,
 0.02236089443577743,
 0.02236089443577743,
 0.02236089443577743,
 0.02236089443577743,
 0.02236089443577743,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.0218408736349454,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.021320852834113363,
 0.02080083203328133,
 0.02080083203328133,
 0.0202808112324493,
 0.0202808112324493,
 0.0202808112324493,
 0.019760790431617263,
 0.0187207488299532,
 0.0187207488299532,
 0.018200728029121163,
 0.01768070722828913,
 0.0171606864274571,
 0.016640665626625067,
 0.01612064482579303,
 0.01612064482579303,
 0.01612064482579303,
 0.015600624024960999,
 0.015600624024960999,
 0.015600624024960999,
 0.015080603224128965,
 0.014560582423296931,
 0.014560582423296931,
 0.013520540821632865,
 0.013000520020800831,
 0.013000520020800831,
 0.013000520020800831,
 0.0124804992199688,
 0.0124804992199688,
 0.011960478419136765,
 0.011440457618304731,
 0.010400416016640665,
 0.010400416016640665,
 0.010400416016640665,
 0.009880395215808632,
 0.009880395215808632,
 0.0093603744149766,
 0.008840353614144566,
 0.008840353614144566,
 0.008840353614144566,
 0.0078003120124804995,
 0.006760270410816433,
 0.0062402496099844,
 0.004160166406656267,
 0.003640145605824233,
 0.003640145605824233,
 0.0020800832033281333,
 0.0]

plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("Death Prediction", fontsize=14)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
x = [0.0, 1.0]
plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

plt.plot(fp_rates, tp_rates, color='green', linewidth=1, label='RNN+CE')


plt.plot(fp_rates_ce_retain,tp_rate_ce_retain,color='blue',label='RETAIN+CE')

#plt.plot(fp_rate_hl_retain,tp_rate_hl_retain,color='orange',label='RETAIN+HL')

plt.plot(fp_rates_cl_RNN,tp_rates_CL_RNN,color='violet',label='RNN+CL')

plt.plot(fp_rates_cl, tp_rates_CL, color='red', linewidth=1, label='RETAIN+CL')



plt.legend(loc='lower right')
plt.show()