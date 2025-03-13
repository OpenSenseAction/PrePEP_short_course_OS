# minimal distance between a pws and a reference 'gauge'
print(distance_matrix_pws_ref.where(distance_matrix_pws_ref==distance_matrix_pws_ref.values.min(),drop=True))
# plot
ds_pws.rainfall.sel(id='ams56').resample(time='1h').sum().plot(figsize=(12,2),alpha=0.5,label='pws')
ds_ref.rainfall.sel(id='11').plot(color='C1',alpha=0.5,label='reference')
plt.legend()
plt.show()

# maximal distance between a pws and a reference 'gauge'
print(distance_matrix_pws_ref.where(distance_matrix_pws_ref==distance_matrix_pws_ref.values.max(),drop=True))
# plot
ds_pws.rainfall.sel(id='ams10').resample(time='1h').sum().plot(figsize=(12,2),alpha=0.5,label='pws')
ds_ref.rainfall.sel(id='10').plot(color='C1',alpha=0.5,label='reference')
plt.legend();