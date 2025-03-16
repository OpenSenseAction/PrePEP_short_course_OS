def do_rsd_wet_dry_and_count_wet_periods(tl, threshold):
    rsd = tl.rolling(time=60*6, center=True).std() 
    wet = rsd > threshold
    return wet.sum(dim='time')

threshold_vec = np.arange(0, 4, 0.01)
wet_counts = [
    do_rsd_wet_dry_and_count_wet_periods(
        tl=ds_cml.tl.isel(sublink_id=0), 
        threshold=threshold,
        ).data # return numpy array here
    for threshold in threshold_vec
]

plt.plot(threshold_vec, wet_counts)
plt.xlabel('RSD threshold')
plt.ylabel('count of wet data points');