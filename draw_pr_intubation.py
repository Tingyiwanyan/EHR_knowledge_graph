import numpy as np
import matplotlib.pyplot as plt



RNN_ce_precision=[0.10178236397748593,
 0.11451612903225807,
 0.12197928653624857,
 0.12568639414276997,
 0.135752688172043,
 0.14558823529411766,
 0.15528455284552845,
 0.1755062680810029,
 0.21843434343434343,
 0.2983425414364641,
 0.33116883116883117,
 0.4022038567493113,
 0.4218289085545723,
 0.43670886075949367,
 0.4444444444444444,
 0.4628975265017668,
 0.4794007490636704,
 0.49612403100775193,
 0.5100401606425703,
 0.5367965367965368,
 0.5486725663716814,
 0.5688073394495413,
 0.5913461538461539,
 0.6039603960396039,
 0.6192893401015228,
 0.6387434554973822,
 0.6521739130434783,
 0.6538461538461539,
 0.6610169491525424,
 0.6608187134502924,
 0.6646706586826348,
 0.6832298136645962,
 0.6962025316455697,
 0.7248322147651006,
 0.7346938775510204,
 0.7310344827586207,
 0.7304964539007093,
 0.746268656716418,
 0.7619047619047619,
 0.7741935483870968,
 0.7868852459016393,
 0.7916666666666666,
 0.7966101694915254,
 0.7913043478260869,
 0.8,
 0.7962962962962963,
 0.7924528301886793,
 0.7920792079207921,
 0.7959183673469388,
 0.7938144329896907,
 0.8131868131868132,
 0.8160919540229885,
 0.813953488372093,
 0.8271604938271605,
 0.8421052631578947,
 0.8378378378378378,
 0.8333333333333334,
 0.8529411764705882,
 0.8529411764705882,
 0.8656716417910447,
 0.8852459016393442,
 0.8947368421052632,
 0.8928571428571429,
 0.8909090909090909,
 0.9056603773584906,
 0.9038461538461539,
 0.9,
 0.8958333333333334,
 0.9333333333333333,
 0.9302325581395349,
 0.9285714285714286,
 0.926829268292683,
 0.9210526315789473,
 0.9210526315789473,
 0.9428571428571428,
 0.9411764705882353,
 0.9375,
 0.9375,
 0.9354838709677419,
 0.9310344827586207,
 0.9310344827586207,
 0.9230769230769231,
 0.9130434782608695,
 0.9130434782608695,
 0.9523809523809523,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1]

RNN_ce_recall=[1.0,
 0.9770642201834863,
 0.9724770642201835,
 0.944954128440367,
 0.926605504587156,
 0.908256880733945,
 0.8761467889908257,
 0.8348623853211009,
 0.7935779816513762,
 0.7431192660550459,
 0.7018348623853211,
 0.6697247706422018,
 0.6559633027522935,
 0.6330275229357798,
 0.6238532110091743,
 0.6009174311926605,
 0.5871559633027523,
 0.5871559633027523,
 0.5825688073394495,
 0.5688073394495413,
 0.5688073394495413,
 0.5688073394495413,
 0.5642201834862385,
 0.5596330275229358,
 0.5596330275229358,
 0.5596330275229358,
 0.5504587155963303,
 0.5458715596330275,
 0.536697247706422,
 0.518348623853211,
 0.5091743119266054,
 0.5045871559633027,
 0.5045871559633027,
 0.4954128440366973,
 0.4954128440366973,
 0.48623853211009177,
 0.4724770642201835,
 0.45871559633027525,
 0.44036697247706424,
 0.44036697247706424,
 0.44036697247706424,
 0.43577981651376146,
 0.43119266055045874,
 0.41743119266055045,
 0.4036697247706422,
 0.3944954128440367,
 0.3853211009174312,
 0.3669724770642202,
 0.3577981651376147,
 0.3532110091743119,
 0.3394495412844037,
 0.3256880733944954,
 0.3211009174311927,
 0.3073394495412844,
 0.29357798165137616,
 0.28440366972477066,
 0.27522935779816515,
 0.26605504587155965,
 0.26605504587155965,
 0.26605504587155965,
 0.24770642201834864,
 0.23394495412844038,
 0.22935779816513763,
 0.22477064220183487,
 0.22018348623853212,
 0.21559633027522937,
 0.20642201834862386,
 0.19724770642201836,
 0.1926605504587156,
 0.1834862385321101,
 0.17889908256880735,
 0.1743119266055046,
 0.16055045871559634,
 0.16055045871559634,
 0.15137614678899083,
 0.14678899082568808,
 0.13761467889908258,
 0.13761467889908258,
 0.13302752293577982,
 0.12385321100917432,
 0.12385321100917432,
 0.11009174311926606,
 0.0963302752293578,
 0.0963302752293578,
 0.09174311926605505,
 0.0871559633027523,
 0.0779816513761468,
 0.0779816513761468,
 0.0779816513761468,
 0.0779816513761468,
 0.0779816513761468,
 0.07339449541284404,
 0.06880733944954129,
 0.05963302752293578,
 0.05504587155963303,
 0.05045871559633028,
 0.03669724770642202,
 0.022935779816513763,
 0.01834862385321101,
 0.0045871559633027525,
 0.0]

Retain_ce_precision=[0.10182157870154133,
 0.10326859308384652,
 0.10773067331670823,
 0.11169375983219716,
 0.11827354260089686,
 0.12576312576312576,
 0.13802622498274672,
 0.15736885928393005,
 0.1951219512195122,
 0.26644182124789206,
 0.3557692307692308,
 0.4444444444444444,
 0.4630225080385852,
 0.47959183673469385,
 0.498220640569395,
 0.5092250922509225,
 0.5189393939393939,
 0.545816733067729,
 0.5447154471544715,
 0.5531914893617021,
 0.5603448275862069,
 0.5752212389380531,
 0.5855855855855856,
 0.5871559633027523,
 0.5990566037735849,
 0.5911330049261084,
 0.592964824120603,
 0.5979381443298969,
 0.6149732620320856,
 0.6263736263736264,
 0.632768361581921,
 0.6379310344827587,
 0.6369047619047619,
 0.6441717791411042,
 0.6496815286624203,
 0.6490066225165563,
 0.6510067114093959,
 0.6527777777777778,
 0.6549295774647887,
 0.6474820143884892,
 0.6518518518518519,
 0.6589147286821705,
 0.6640625,
 0.6666666666666666,
 0.664,
 0.664,
 0.6721311475409836,
 0.6837606837606838,
 0.6936936936936937,
 0.6880733944954128,
 0.6915887850467289,
 0.6886792452830188,
 0.6990291262135923,
 0.71,
 0.7070707070707071,
 0.7263157894736842,
 0.7340425531914894,
 0.7340425531914894,
 0.7472527472527473,
 0.7586206896551724,
 0.7738095238095238,
 0.775,
 0.7894736842105263,
 0.7808219178082192,
 0.7714285714285715,
 0.7910447761194029,
 0.7868852459016393,
 0.7966101694915254,
 0.8245614035087719,
 0.8392857142857143,
 0.8392857142857143,
 0.8363636363636363,
 0.8301886792452831,
 0.8431372549019608,
 0.8431372549019608,
 0.84,
 0.8541666666666666,
 0.8444444444444444,
 0.8409090909090909,
 0.8333333333333334,
 0.8205128205128205,
 0.8157894736842105,
 0.8157894736842105,
 0.8333333333333334,
 0.8333333333333334,
 0.8333333333333334,
 0.8333333333333334,
 0.8125,
 0.8333333333333334,
 0.8275862068965517,
 0.84,
 0.8636363636363636,
 0.8888888888888888,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1]

Retain_ce_recall= [1.0,
 1.0,
 0.9908256880733946,
 0.9770642201834863,
 0.9678899082568807,
 0.944954128440367,
 0.9174311926605505,
 0.8669724770642202,
 0.8073394495412844,
 0.7247706422018348,
 0.6788990825688074,
 0.6605504587155964,
 0.6605504587155964,
 0.6467889908256881,
 0.6422018348623854,
 0.6330275229357798,
 0.6284403669724771,
 0.6284403669724771,
 0.6146788990825688,
 0.5963302752293578,
 0.5963302752293578,
 0.5963302752293578,
 0.5963302752293578,
 0.5871559633027523,
 0.5825688073394495,
 0.5504587155963303,
 0.5412844036697247,
 0.5321100917431193,
 0.5275229357798165,
 0.5229357798165137,
 0.5137614678899083,
 0.5091743119266054,
 0.4908256880733945,
 0.481651376146789,
 0.46788990825688076,
 0.44954128440366975,
 0.44495412844036697,
 0.43119266055045874,
 0.42660550458715596,
 0.41284403669724773,
 0.4036697247706422,
 0.38990825688073394,
 0.38990825688073394,
 0.3853211009174312,
 0.38073394495412843,
 0.38073394495412843,
 0.3761467889908257,
 0.3669724770642202,
 0.3532110091743119,
 0.3440366972477064,
 0.3394495412844037,
 0.3348623853211009,
 0.3302752293577982,
 0.3256880733944954,
 0.3211009174311927,
 0.3165137614678899,
 0.3165137614678899,
 0.3165137614678899,
 0.3119266055045872,
 0.30275229357798167,
 0.2981651376146789,
 0.28440366972477066,
 0.27522935779816515,
 0.26146788990825687,
 0.24770642201834864,
 0.24311926605504589,
 0.22018348623853212,
 0.21559633027522937,
 0.21559633027522937,
 0.21559633027522937,
 0.21559633027522937,
 0.21100917431192662,
 0.2018348623853211,
 0.19724770642201836,
 0.19724770642201836,
 0.1926605504587156,
 0.18807339449541285,
 0.1743119266055046,
 0.16972477064220184,
 0.16055045871559634,
 0.14678899082568808,
 0.14220183486238533,
 0.14220183486238533,
 0.13761467889908258,
 0.13761467889908258,
 0.13761467889908258,
 0.13761467889908258,
 0.11926605504587157,
 0.11467889908256881,
 0.11009174311926606,
 0.0963302752293578,
 0.0871559633027523,
 0.07339449541284404,
 0.06880733944954129,
 0.05963302752293578,
 0.04128440366972477,
 0.03669724770642202,
 0.027522935779816515,
 0.027522935779816515,
 0.009174311926605505,
 0.0]

rnn_cl_precision = [0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10186915887850467,
 0.10186915887850467,
 0.10154422087037904,
 0.10255198487712665,
 0.17395727365208546,
 0.25413533834586466,
 0.2982142857142857,
 0.3340122199592668,
 0.37471264367816093,
 0.40954773869346733,
 0.4323607427055703,
 0.4527777777777778,
 0.46839080459770116,
 0.4808259587020649,
 0.48936170212765956,
 0.4938650306748466,
 0.5,
 0.5063694267515924,
 0.5097402597402597,
 0.5130718954248366,
 0.5165562913907285,
 0.5273972602739726,
 0.5310344827586206,
 0.532871972318339,
 0.5331010452961672,
 0.5368421052631579,
 0.5390070921985816,
 0.5428571428571428,
 0.5448028673835126,
 0.5487364620938628,
 0.5507246376811594,
 0.5507246376811594,
 0.5527272727272727,
 0.5567765567765568,
 0.5567765567765568,
 0.5588235294117647,
 0.562962962962963,
 0.5650557620817844,
 0.5671641791044776,
 0.5671641791044776,
 0.5714285714285714,
 0.5714285714285714,
 0.5714285714285714,
 0.5735849056603773,
 0.5735849056603773,
 0.5735849056603773,
 0.5735849056603773,
 0.5779467680608364,
 0.5779467680608364,
 0.5801526717557252,
 0.5801526717557252,
 0.5801526717557252,
 0.5801526717557252,
 0.5823754789272031,
 0.5868725868725869,
 0.5868725868725869,
 0.5868725868725869,
 0.5868725868725869,
 0.5891472868217055,
 0.5891472868217055,
 0.5891472868217055,
 0.5891472868217055,
 0.5875486381322957,
 0.5875486381322957,
 0.58984375,
 0.592156862745098,
 0.5928853754940712,
 0.5912698412698413,
 0.592,
 0.5903614457831325,
 0.592741935483871,
 0.592741935483871,
 0.5975609756097561,
 0.5975609756097561,
 0.5975609756097561,
 0.6024590163934426,
 0.6024590163934426,
 0.6008230452674898,
 0.6008230452674898,
 0.6008230452674898,
 0.5975103734439834,
 0.6,
 0.6,
 0.6,
 0.6,
 0.6,
 0.6050420168067226,
 0.6050420168067226,
 0.6050420168067226,
 0.6050420168067226,
 0.6075949367088608,
 0.6075949367088608,
 0.6101694915254238,
 0.6101694915254238,
 0.6101694915254238,
 0.6127659574468085,
 0.6127659574468085,
 0.6127659574468085,
 0.6137339055793991,
 0.6137339055793991,
 0.6137339055793991,
 0.6147186147186147,
 0.6173913043478261,
 0.6173913043478261,
 0.6173913043478261,
 0.6173913043478261,
 0.6173913043478261,
 0.6173913043478261,
 0.618421052631579,
 0.618421052631579,
 0.6211453744493393,
 0.6238938053097345,
 0.6266666666666667,
 0.6261261261261262,
 0.6261261261261262,
 0.6244343891402715,
 0.6272727272727273,
 0.6284403669724771,
 0.631336405529954,
 0.6372093023255814,
 0.6415094339622641,
 0.6415094339622641,
 0.6428571428571429,
 0.645933014354067,
 0.645933014354067,
 0.645933014354067,
 0.645933014354067,
 0.645933014354067,
 0.6490384615384616,
 0.6473429951690821,
 0.6519607843137255,
 0.6567164179104478,
 0.66,
 0.6582914572864321,
 0.6581632653061225,
 0.6581632653061225,
 0.6581632653061225,
 0.6564102564102564,
 0.6564102564102564,
 0.6528497409326425,
 0.6528497409326425,
 0.6528497409326425,
 0.6510416666666666,
 0.6510416666666666,
 0.6544502617801047,
 0.6613756613756614,
 0.6613756613756614,
 0.6613756613756614,
 0.6702702702702703,
 0.6684782608695652,
 0.6741573033707865,
 0.6761363636363636,
 0.6820809248554913,
 0.6982248520710059,
 0.703030303030303,
 0.7098765432098766,
 0.7115384615384616,
 0.7397260273972602,
 0.7372262773722628,
 0.7398373983739838,
 0.7567567567567568,
 0.7475728155339806,
 0.7847058823529411,
 0.7646376811594203,
 0.8308333333333334,
 0.882608695652174,
 0.9166666666666666,
 0.95,
 1.0,
 1.0,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1]

rnn_cl_recall = [1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 0.9954128440366973,
 0.9954128440366973,
 0.7844036697247706,
 0.7752293577981652,
 0.7660550458715596,
 0.7522935779816514,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7477064220183486,
 0.7385321100917431,
 0.7385321100917431,
 0.7339449541284404,
 0.7293577981651376,
 0.7201834862385321,
 0.7201834862385321,
 0.7155963302752294,
 0.7064220183486238,
 0.7064220183486238,
 0.7064220183486238,
 0.7018348623853211,
 0.7018348623853211,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6972477064220184,
 0.6926605504587156,
 0.6926605504587156,
 0.6926605504587156,
 0.6926605504587156,
 0.6880733944954128,
 0.6834862385321101,
 0.6788990825688074,
 0.6743119266055045,
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
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6376146788990825,
 0.6376146788990825,
 0.6330275229357798,
 0.6330275229357798,
 0.6284403669724771,
 0.6284403669724771,
 0.6284403669724771,
 0.6238532110091743,
 0.6238532110091743,
 0.6192660550458715,
 0.6192660550458715,
 0.6192660550458715,
 0.6192660550458715,
 0.6192660550458715,
 0.6192660550458715,
 0.6192660550458715,
 0.6146788990825688,
 0.6100917431192661,
 0.6055045871559633,
 0.6055045871559633,
 0.6009174311926605,
 0.591743119266055,
 0.591743119266055,
 0.591743119266055,
 0.5871559633027523,
 0.5871559633027523,
 0.5779816513761468,
 0.5779816513761468,
 0.5779816513761468,
 0.573394495412844,
 0.573394495412844,
 0.573394495412844,
 0.573394495412844,
 0.573394495412844,
 0.573394495412844,
 0.5688073394495413,
 0.5642201834862385,
 0.5504587155963303,
 0.5458715596330275,
 0.5412844036697247,
 0.5412844036697247,
 0.5321100917431193,
 0.5275229357798165,
 0.5091743119266054,
 0.4954128440366973,
 0.463302752293578,
 0.41743119266055045,
 0.3853211009174312,
 0.3532110091743119,
 0.2981651376146789,
 0.22935779816513763,
 0.16972477064220184,
 0.08256880733944955,
 0.01834862385321101,
 0.013761467889908258,
 0.0045871559633027525,
 0.0045871559633027525,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0]

retain_cl_precision = [0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10182157870154133,
 0.10186915887850467,
 0.10234741784037558,
 0.24202898550724639,
 0.3450413223140496,
 0.39285714285714285,
 0.41353383458646614,
 0.4274611398963731,
 0.44086021505376344,
 0.4478021978021978,
 0.4565826330532213,
 0.47093023255813954,
 0.4864864864864865,
 0.49240121580547114,
 0.5015576323987538,
 0.5047021943573667,
 0.5111111111111111,
 0.5176848874598071,
 0.5261437908496732,
 0.53156146179402,
 0.5353535353535354,
 0.5374149659863946,
 0.5467128027681661,
 0.5451388888888888,
 0.5528169014084507,
 0.5567375886524822,
 0.5587188612099644,
 0.5587188612099644,
 0.5607142857142857,
 0.5627240143369175,
 0.5667870036101083,
 0.5652173913043478,
 0.5672727272727273,
 0.5714285714285714,
 0.5735294117647058,
 0.5735294117647058,
 0.5735294117647058,
 0.5756457564575646,
 0.5799256505576208,
 0.5871212121212122,
 0.5938697318007663,
 0.5938697318007663,
 0.5923076923076923,
 0.5945945945945946,
 0.5968992248062015,
 0.59765625,
 0.6,
 0.5984251968503937,
 0.5968379446640316,
 0.5952380952380952,
 0.5976095617529881,
 0.596,
 0.6032388663967612,
 0.6032388663967612,
 0.6056910569105691,
 0.6056910569105691,
 0.6081632653061224,
 0.6081632653061224,
 0.6081632653061224,
 0.6081632653061224,
 0.6081632653061224,
 0.610655737704918,
 0.6090534979423868,
 0.6115702479338843,
 0.6141078838174274,
 0.6141078838174274,
 0.6141078838174274,
 0.6166666666666667,
 0.6166666666666667,
 0.6166666666666667,
 0.6150627615062761,
 0.6150627615062761,
 0.6134453781512605,
 0.6160337552742616,
 0.6160337552742616,
 0.6160337552742616,
 0.6186440677966102,
 0.6186440677966102,
 0.6186440677966102,
 0.6186440677966102,
 0.6170212765957447,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6206896551724138,
 0.6233766233766234,
 0.6233766233766234,
 0.6260869565217392,
 0.6260869565217392,
 0.6244541484716157,
 0.6244541484716157,
 0.6271929824561403,
 0.6299559471365639,
 0.6299559471365639,
 0.6327433628318584,
 0.6327433628318584,
 0.6355555555555555,
 0.6355555555555555,
 0.6355555555555555,
 0.6383928571428571,
 0.6383928571428571,
 0.6383928571428571,
 0.6441441441441441,
 0.6441441441441441,
 0.6441441441441441,
 0.6441441441441441,
 0.6470588235294118,
 0.6470588235294118,
 0.6454545454545455,
 0.6454545454545455,
 0.6454545454545455,
 0.6454545454545455,
 0.6454545454545455,
 0.6438356164383562,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6527777777777778,
 0.6558139534883721,
 0.6650943396226415,
 0.6698564593301436,
 0.6714975845410628,
 0.6764705882352942,
 0.6732673267326733,
 0.6732673267326733,
 0.6732673267326733,
 0.68,
 0.678391959798995,
 0.678391959798995,
 0.6767676767676768,
 0.6767676767676768,
 0.6802030456852792,
 0.6802030456852792,
 0.6804123711340206,
 0.6822916666666666,
 0.6822916666666666,
 0.6822916666666666,
 0.680628272251309,
 0.6772486772486772,
 0.6808510638297872,
 0.679144385026738,
 0.6827956989247311,
 0.6827956989247311,
 0.6827956989247311,
 0.6923076923076923,
 0.7,
 0.7,
 0.7039106145251397,
 0.7039106145251397,
 0.6971428571428572,
 0.7011494252873564,
 0.7011494252873564,
 0.6994219653179191,
 0.7058823529411765,
 0.7151515151515152,
 0.7098765432098766,
 0.7197452229299363,
 0.7254901960784313,
 0.7248322147651006,
 0.723404255319149,
 0.746268656716418,
 0.75,
 0.75,
 0.7477477477477478,
 0.7383177570093458,
 0.7684210526315789,
 0.7738095238095238,
 0.7638888888888888,
 0.7818181818181819,
 0.8333333333333334,
 0.9230769230769231,
 1.0,
 1.0,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1,
 1]

retain_cl_recall = [1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 1.0,
 0.7660550458715596,
 0.7660550458715596,
 0.7568807339449541,
 0.7568807339449541,
 0.7568807339449541,
 0.7522935779816514,
 0.7477064220183486,
 0.7477064220183486,
 0.7431192660550459,
 0.7431192660550459,
 0.7431192660550459,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7385321100917431,
 0.7339449541284404,
 0.7293577981651376,
 0.7247706422018348,
 0.7247706422018348,
 0.7201834862385321,
 0.7201834862385321,
 0.7201834862385321,
 0.7201834862385321,
 0.7201834862385321,
 0.7201834862385321,
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
 0.7110091743119266,
 0.7110091743119266,
 0.7110091743119266,
 0.7064220183486238,
 0.7064220183486238,
 0.7064220183486238,
 0.7018348623853211,
 0.7018348623853211,
 0.6972477064220184,
 0.6926605504587156,
 0.6880733944954128,
 0.6880733944954128,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6834862385321101,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
 0.6788990825688074,
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
 0.6651376146788991,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6605504587155964,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6559633027522935,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6513761467889908,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6467889908256881,
 0.6422018348623854,
 0.6376146788990825,
 0.6330275229357798,
 0.6238532110091743,
 0.6238532110091743,
 0.6238532110091743,
 0.6238532110091743,
 0.6192660550458715,
 0.6192660550458715,
 0.6146788990825688,
 0.6146788990825688,
 0.6146788990825688,
 0.6146788990825688,
 0.6055045871559633,
 0.6009174311926605,
 0.6009174311926605,
 0.6009174311926605,
 0.5963302752293578,
 0.5871559633027523,
 0.5871559633027523,
 0.5825688073394495,
 0.5825688073394495,
 0.5825688073394495,
 0.5825688073394495,
 0.5779816513761468,
 0.5779816513761468,
 0.5779816513761468,
 0.5779816513761468,
 0.5779816513761468,
 0.5596330275229358,
 0.5596330275229358,
 0.5596330275229358,
 0.555045871559633,
 0.5504587155963303,
 0.5412844036697247,
 0.5275229357798165,
 0.518348623853211,
 0.5091743119266054,
 0.4954128440366973,
 0.46788990825688076,
 0.45871559633027525,
 0.42660550458715596,
 0.41284403669724773,
 0.38073394495412843,
 0.3623853211009174,
 0.3348623853211009,
 0.2981651376146789,
 0.25229357798165136,
 0.19724770642201836,
 0.13761467889908258,
 0.05504587155963303,
 0.009174311926605505,
 0.0045871559633027525,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0]






plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Intubation Prediction", fontsize=14)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
x = [0.0, 1.0]
#plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

plt.plot(RNN_ce_recall, RNN_ce_precision, color='green', linewidth=1, label='RNN+CE(AUC=0.827)')


plt.plot(Retain_ce_recall,Retain_ce_precision,color='blue',label='RETAIN+CE(AUC=0.836)')

#plt.plot(fp_rate_hl_retain,tp_rate_hl_retain,color='orange',label='RETAIN+HL')

plt.plot(rnn_cl_recall,rnn_cl_precision,color='violet',label='RNN+CL(AUC=0.856)')
plt.plot(retain_cl_recall, retain_cl_precision, color='red', linewidth=1, label='RETAIN+CL(AUC=0.840)')


plt.legend(loc='lower right')
plt.show()