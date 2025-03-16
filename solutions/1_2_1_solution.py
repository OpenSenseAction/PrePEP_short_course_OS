radar_along_cml_R_sum = radar_along_cml_R_1h.sum(dim='time')
cmls_R_sum = cmls_R_1h.sum(dim='time')

plt.scatter(radar_along_cml_R_sum, cmls_R_sum, alpha=0.7)
plt.xlim([0, 70])
plt.ylim([0, 70])
plt.xlabel('radar rainfall at CML (mm)')
plt.ylabel('CML rainfall sum (mm)')