from plotFasor import *

ifuente = 10
vfuente = 220

zcap = -10j
zbob = 10j
r5 = 5
r10 = 10

# caso 1

vcap_1 = ifuente * zcap
icap_1 = ifuente

vr10_1 = 0
ir10_1 = 0

zeq = paralell(r5, zbob)

vr5_1 = ifuente * zeq
vbob_1 = vr5_1
ir5_1 = vr5_1 / r5
ibob_1 = vbob_1 / zbob

ifuente_v_1 = -vr5_1
vfuente_i_1 = -ibob_1

#caso 2

ir10_2 = vfuente / r10
ir5_2 = vfuente / (r5 + zbob)
ibob_2 = -ir5_2

vr10_2 = vfuente
vr5_2 = ir5_2 * r5
vbob_2 = ibob_2 * zbob

vfuente_i_2 = -(ir10_2 + ir5_2)
ifuente_v_2 = vr5_2

# sumamos

vfuente_i = vfuente_i_1 + vfuente_i_2
ifuente_v = ifuente_v_1 + ifuente_v_2

vcap = vcap_1
icap = icap_1

vbob = vbob_1 + vbob_2
ibob = ibob_1 + ibob_2

vr5 = vr5_1 + vr5_2
ir5 = ir5_1 + ir5_2

vr10 = vr10_1 + vr10_2
ir10 = ir10_1 + ir10_2


# potencias

pfuente_v = vfuente * conj(vfuente_i)
pfuente_i = ifuente_v * conj(ifuente)

pcap = vcap * conj(icap)
pbob = vbob * conj(ibob)

pr5 = vr5 * conj(ir5)
pr10 = vr10 * conj(ir10)

print(pfuente_i + pfuente_v + pcap + pbob + pr5 + pr10)

print("s fuente i = ", printComplex(pfuente_i), " kWatt +jVAR")
print("s fuente v = ", printComplex(pfuente_v), " kWatt +jVAR")
print("s cap = ", printComplex(pcap), " kWatt +jVAR")
print("s bob = ", printComplex(pbob), " kWatt +jVAR")
print("s r5 = ", printComplex(pr5), " kWatt +jVAR")
print("s r10 = ",printComplex(pr10), " kWatt +jVAR")

