import numpy as np
import matplotlib.pyplot as plt





precision_retain_ce = [0.17224199, 0.18890643, 0.41168711, 0.49811202, 0.54342034,
       0.56462927, 0.59794944, 0.61305052, 0.63255196, 0.63702024,
       0.65054444, 0.64554705, 0.64342174, 0.64911363, 0.6472129 ,
       0.65029655, 0.66462172, 0.67217009, 0.67407295, 0.68026732,
       0.69556219, 0.71002429, 0.72195224, 0.72817734, 0.72953121,
       0.7460728 , 0.76531302, 0.76701629, 0.7650663 , 0.7757686 ,
       0.75921648, 0.77220588, 0.76      , 0.78264791, 0.81616162,
       0.85285714, 0.8       , 1.        , 1.        , 1.        ,
       1.        ]

recall_retain_ce = [1.        , 0.97768946, 0.74130947, 0.63740026, 0.59427587,
       0.53869509, 0.50542525, 0.47161177, 0.45307191, 0.43838326,
       0.4281954 , 0.39854722, 0.38231652, 0.36828215, 0.34732036,
       0.33508086, 0.32873951, 0.31983806, 0.3116304 , 0.30320513,
       0.2935689 , 0.28147775, 0.27495725, 0.26455178, 0.25997303,
       0.25128918, 0.24264231, 0.23212296, 0.21449921, 0.20878492,
       0.18830331, 0.16558616, 0.13055155, 0.10036298, 0.07328144,
       0.04107422, 0.01190476, 0.00238095, 0.        , 0.        ,
       0.        ]

precision_ce_rnn_icu=[]

recall_ce_rnn_icu=[]

precision_RNN_cl = []

recall_cl_rnn = []


precision_cl_retain_icu = [0.17224199, 0.20753078, 0.37626277, 0.45401269, 0.50388093,
       0.53945258, 0.55350211, 0.57060207, 0.58768186, 0.59696839,
       0.61776521, 0.6235327 , 0.63360907, 0.63744871, 0.64716477,
       0.65777298, 0.66535006, 0.6769723 , 0.68918341, 0.691313  ,
       0.69436944, 0.69986374, 0.7035098 , 0.70830455, 0.70572919,
       0.70740916, 0.71832512, 0.72940375, 0.73824668, 0.72904765,
       0.74636513, 0.75606154, 0.77377739, 0.7812381 , 0.76507937,
       0.72027473, 0.78333333, 1.        , 1.        , 1.        ,
       1.        ]

recall_cl_retain_icu = [1.        , 0.96446131, 0.79446903, 0.71452532, 0.65351712,
       0.62820288, 0.59643886, 0.57563047, 0.55870304, 0.5401269 ,
       0.52301632, 0.51264931, 0.49820802, 0.4830062 , 0.47303994,
       0.45680777, 0.44673234, 0.43204116, 0.41591417, 0.39708491,
       0.3849553 , 0.3750275 , 0.36681984, 0.36073854, 0.34234702,
       0.32615583, 0.31919613, 0.2992284 , 0.29068925, 0.26566405,
       0.24803159, 0.22604669, 0.20076472, 0.16891004, 0.13237142,
       0.07257241, 0.01879228, 0.        , 0.        , 0.        ,
       0.        ]




plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("ICU Prediction", fontsize=14)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
x = [0.0, 1.0]
#plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

plt.plot(recall_ce_rnn_icu, precision_ce_rnn_icu, color='g', linestyle='dashed', linewidth=1, label='RNN+CE(AUC=0.794)')


plt.plot(recall_retain_ce,precision_retain_ce,color='blue',linestyle='dashed', label='RETAIN+CE(AUC=0.802)')

#plt.plot(fp_rate_hl_retain,tp_rate_hl_retain,color='orange',label='RETAIN+HL')

plt.plot(recall_cl_rnn,precision_RNN_cl,color='violet',linewidth=1.5,label='RNN+CL(AUC=0.823)')
plt.plot(recall_cl_retain_icu, precision_cl_retain_icu, color='red', linewidth=1.5, label='RETAIN+CL(AUC=0.821)')


plt.legend(loc='lower right')
plt.show()