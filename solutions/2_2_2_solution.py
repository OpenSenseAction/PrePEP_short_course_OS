ds_cml = ds_cmls.isel(cml_id=285) # try 285, 333, 122, 57 and 310

factor = 1.2 
ds_cml['rsd'] = ds_cml.tl.rolling(time=60*6, center=True).std() 
ds_cml['rsd_threshold'] = factor * ds_cml.rsd.quantile(.80)
ds_cml['wet'] = ds_cml.rsd > ds_cml.rsd_threshold

# Plot RSL of TL and threshold
fig, axs = plt.subplots(2, 1, figsize=(16,4), sharex=True)
ds_cml.rsd.plot.line(x='time', ax=axs[0])
axs[0].axhline(threshold, color='k', linestyle='--', label='threshold')

# Plot TL and mark wet periods
ds_cml.tl.plot.line(x='time', ax=axs[1]);
highlight_wet_periods(ds_cml.wet, ax=axs[1])
axs[0].set_title('');
axs[1].set_title('');

print(f'RSD threshold from RSD quantile = {ds_cml.rsd_threshold.data:0.2f}')