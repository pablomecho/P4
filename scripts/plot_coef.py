import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['figure.dpi'] = 100
plt.rcParams.update({'font.size': 9})



lp = np.loadtxt("lp_2_3.txt")
lpcc = np.loadtxt('lpcc_2_3.txt')
mfcc = np.loadtxt('mfcc_2_3.txt')

fig, axes = plt.subplots(3, ncols=1)
fig.subplots_adjust(top=0.8)

lp_2 = lp[:, 0]
lpcc_2 = lpcc[:, 0]
mfcc_2 = mfcc[:, 0]

lp_3 = lp[:, 1]
lpcc_3 = lpcc[:, 1]
mfcc_3 = mfcc[:, 1]



axes[0].scatter(lp_2, lp_3, label="lp", color='red', s=1)
axes[1].scatter(lpcc_2, lpcc_3, label="lpcc", color='green', s=1)
axes[2].scatter(mfcc_2, mfcc_3, label="mfcc", color='blue', s=1)

for i in range(3):
    axes[i].set_xlabel("2nd coefficient")
    axes[i].set_ylabel("3rd coefficient")
    axes[i].legend(loc='upper right')

plt.suptitle("\n".join(["Correlation between 2nd and 3rd coefficients"]), y=1)


plt.tight_layout()
plt.savefig("Graph_2_3_coef.png", bbox_inches="tight")