# pws and ref time series in native temporal resolution
ds_pws.rainfall.isel(id=16).plot(figsize=(12,2),alpha=0.5,label='pws')
ds_ref.rainfall.isel(id=0).plot(color='C1',alpha=0.5,label='reference')
plt.legend()

# identical, but pws resampled to hourly ranifall
ds_pws.rainfall.isel(id=16).resample(time='1h').sum().plot(figsize=(12,2),alpha=0.5,label='pws')
ds_ref.rainfall.isel(id=0).plot(color='C1',alpha=0.5,label='reference')
plt.legend();