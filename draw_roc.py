import numpy as np
import matplotlib.pyplot as plt


tp_rates = [1.0,
 1.0,
 1.0,
 0.9954337899543378,
 0.9908675799086758,
 0.9863013698630136,
 0.9726027397260274,
 0.954337899543379,
 0.9269406392694064,
 0.8767123287671232,
 0.8493150684931506,
 0.8310502283105022,
 0.7945205479452054,
 0.771689497716895,
 0.7397260273972602,
 0.7351598173515982,
 0.726027397260274,
 0.7123287671232876,
 0.7031963470319634,
 0.684931506849315,
 0.6757990867579908,
 0.6712328767123288,
 0.6621004566210046,
 0.6529680365296804,
 0.6529680365296804,
 0.639269406392694,
 0.6210045662100456,
 0.6210045662100456,
 0.6210045662100456,
 0.6118721461187214,
 0.6027397260273972,
 0.5981735159817352,
 0.593607305936073,
 0.589041095890411,
 0.589041095890411,
 0.589041095890411,
 0.589041095890411,
 0.5799086757990868,
 0.5753424657534246,
 0.5753424657534246,
 0.5707762557077626,
 0.5616438356164384,
 0.5616438356164384,
 0.5525114155251142,
 0.547945205479452,
 0.54337899543379,
 0.54337899543379,
 0.5388127853881278,
 0.5342465753424658,
 0.5296803652968036,
 0.5296803652968036,
 0.5296803652968036,
 0.5296803652968036,
 0.5251141552511416,
 0.5205479452054794,
 0.5159817351598174,
 0.5114155251141552,
 0.5114155251141552,
 0.502283105022831,
 0.4885844748858447,
 0.4885844748858447,
 0.4840182648401826,
 0.4794520547945205,
 0.4794520547945205,
 0.4794520547945205,
 0.4703196347031963,
 0.4703196347031963,
 0.4657534246575342,
 0.4657534246575342,
 0.4611872146118721,
 0.4611872146118721,
 0.45662100456621,
 0.4520547945205479,
 0.4474885844748858,
 0.4474885844748858,
 0.4429223744292237,
 0.4429223744292237,
 0.4383561643835616,
 0.4337899543378995,
 0.4292237442922374,
 0.4246575342465753,
 0.4246575342465753,
 0.4200913242009132,
 0.4155251141552511,
 0.410958904109589,
 0.4063926940639269,
 0.4018264840182648,
 0.3926940639269406,
 0.3926940639269406,
 0.3835616438356164,
 0.3698630136986301,
 0.3698630136986301,
 0.3561643835616438,
 0.3515981735159817,
 0.3424657534246575,
 0.3333333333333333,
 0.3242009132420091,
 0.3013698630136986,
 0.2831050228310502,
 0.2465753424657534,
 0.0]

fp_rates = [1.0,
 0.9625390218522373,
 0.8678459937565036,
 0.7991675338189386,
 0.7117585848074922,
 0.617585848074922,
 0.5171696149843913,
 0.42351716961498437,
 0.33350676378772115,
 0.2643080124869927,
 0.19406867845993755,
 0.14516129032258066,
 0.09365244536940687,
 0.0691987513007284,
 0.05463059313215401,
 0.04630593132154006,
 0.04266389177939646,
 0.040062434963579606,
 0.03485952133194589,
 0.03433922996878252,
 0.033818938605619145,
 0.029136316337148804,
 0.027055150884495317,
 0.023413111342351717,
 0.022892819979188347,
 0.02081165452653486,
 0.019771071800208116,
 0.019771071800208116,
 0.019250780437044746,
 0.019250780437044746,
 0.019250780437044746,
 0.01716961498439126,
 0.01716961498439126,
 0.01716961498439126,
 0.015608740894901144,
 0.014568158168574402,
 0.01404786680541103,
 0.01404786680541103,
 0.01404786680541103,
 0.01404786680541103,
 0.01404786680541103,
 0.01404786680541103,
 0.013527575442247659,
 0.013527575442247659,
 0.013007284079084287,
 0.013007284079084287,
 0.011966701352757543,
 0.011446409989594173,
 0.010926118626430802,
 0.010926118626430802,
 0.010926118626430802,
 0.010926118626430802,
 0.009885535900104058,
 0.009885535900104058,
 0.009365244536940686,
 0.008844953173777315,
 0.008844953173777315,
 0.008844953173777315,
 0.008844953173777315,
 0.008844953173777315,
 0.007284079084287201,
 0.007284079084287201,
 0.007284079084287201,
 0.007284079084287201,
 0.007284079084287201,
 0.007284079084287201,
 0.006763787721123829,
 0.006243496357960458,
 0.005723204994797087,
 0.005723204994797087,
 0.005202913631633715,
 0.004682622268470343,
 0.004682622268470343,
 0.004682622268470343,
 0.004162330905306972,
 0.004162330905306972,
 0.004162330905306972,
 0.004162330905306972,
 0.004162330905306972,
 0.0036420395421436005,
 0.0036420395421436005,
 0.0036420395421436005,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.003121748178980229,
 0.0026014568158168575,
 0.0026014568158168575,
 0.0026014568158168575,
 0.002081165452653486,
 0.002081165452653486,
 0.002081165452653486,
 0.0015608740894901144,
 0.0]

plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ROC curve", fontsize=14)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
x = [0.0, 1.0]
plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

plt.plot(fp_rates, tp_rates, color='green', linewidth=1, label='RNN+CE')

plt.legend(loc='lower right')
plt.show()