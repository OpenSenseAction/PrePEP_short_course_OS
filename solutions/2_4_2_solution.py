R_cml_15min = ds_cml.isel(sublink_id=0).R.resample(time='15min').mean()
radar_along_cml_R_15min = radar_along_cml.sel(cml_id=ds_cml.cml_id.data).resample(time='15min').mean()


R_threshold = 0.1

plg.validation.plot_hexbin(
    radar_along_cml_R_15min.data.flatten(),
    R_cml_15min.data.flatten(),
    ref_thresh=R_threshold,
    est_thresh=R_threshold,
)

plg.validation.plot_confusion_matrix_count(
    reference=radar_along_cml_R_15min.data.flatten(),
    estimate=R_cml_15min.data.flatten(),
    ref_thresh=0.1,
    est_thresh=0.1,
    n_bins=200,
    bin_type='linear',
);
plt.gca().set_xscale("linear")
#plt.gca().set_yscale("log")
plt.xlim([0.09, 20])

rainfall_metrics = plg.validation.calculate_rainfall_metrics(
    reference=radar_along_cml_R_15min.data.flatten(),
    estimate=R_cml_15min.data.flatten(),
    ref_thresh=0.1,
    est_thresh=0.1,
)
rainfall_metrics