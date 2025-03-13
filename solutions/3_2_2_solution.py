# possible solution exercise 3.2.1

fig,ax = plt.subplots(1,2,figsize=(12,6))
ax[0].set_title('Before fz filter')
scat_00 = ax[0].scatter(ds_pws.x,ds_pws.y,c=ds_pws.rainfall.sum(dim='time'),vmin=1000,vmax=2000)
scat_01 = ax[0].scatter(ds_ref.x,ds_ref.y,c=ds_ref.rainfall.sum(dim='time'),vmin=1000,vmax=2000,s=80,edgecolor='black')
fig.colorbar(scat_00)

ax[1].set_title('After fz filter')
scat_10 = ax[1].scatter(ds_pws.x,ds_pws.y,c=ds_pws.rainfall.where(ds_pws.fz_flag !=1).sum(dim='time'),vmin=1000,vmax=2000)
scat_11 = ax[1].scatter(ds_ref.x,ds_ref.y,c=ds_ref.rainfall.sum(dim='time'),vmin=1000,vmax=2000,s=80,edgecolor='black')
fig.colorbar(scat_10);