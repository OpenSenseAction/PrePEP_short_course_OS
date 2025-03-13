# possible solution exercise 3.2.1

# show number of HI flaged timesteps per PWS
print((ds_pws.hi_flag>0).sum(dim='time'))

# simple time seres plot
ds_pws.fz_flag.isel(id=50).plot()

# portion of FZ per time
plt.subplots(figsize=(14,4))
plt.fill_between(ds_pws.time, (ds_pws.fz_flag==0).sum(dim='id')+(ds_pws.fz_flag==-1).sum(dim='id')+(ds_pws.fz_flag==1).sum(dim='id'), color="red",label='FZ')
plt.fill_between(ds_pws.time, (ds_pws.fz_flag<=0).sum(dim='id'), color="yellow",label='not enough neighbouring stations')
plt.fill_between(ds_pws.time, (ds_pws.fz_flag==0).sum(dim='id'), color="lightblue",label='no FZ detected')
plt.legend(loc='lower right');