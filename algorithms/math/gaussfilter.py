import math


def gaussfilt(xdata, ydata, sigma, xfilt=None, M=None, extrap=None):
    if xfilt is None:
        xfilt = xdata
    if M is None:
        M = 3 * sigma
    if extrap is None:
        extrap = 0
    yfilt = [0] * len(xfilt)
    for i in range(0, len(xfilt), 1):
        indices = [k for k, x in enumerate(xdata) if x > (xfilt[i] - M) and x < (xfilt[i] + M)]
        if indices:
            x = []
            for ind in indices:
                x.append(xdata[ind] - xfilt[i])
            gaussfactors = gausskernel(x, sigma)
            y = []
            yd = []
            for ind in indices:
                yd.append(ydata[ind])
            for j in range(0, len(gaussfactors), 1):
                y.append(gaussfactors[j] * yd[j])
            yfilt[i] = sum(y) / sum(gaussfactors)
        if not indices:
            yfilt[i] = extrap
    return yfilt


def gausskernel(x, sigma):
    res = []
    for element in x:
        res.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * pow((element / sigma), 2)))
    return res
