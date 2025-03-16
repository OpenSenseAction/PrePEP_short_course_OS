i_max = tsl_range.argmax(dim='cml_id').data[0]
ds_cml = ds_cmls.isel(cml_id=i_max)

fig, axs = plt.subplots(2, 1, figsize=(14, 5))
ds_cml.tsl.plot.line(x='time', ax=axs[0])
ds_cml.rsl.plot.line(x='time', ax=axs[1])
axs[1].set_title('');