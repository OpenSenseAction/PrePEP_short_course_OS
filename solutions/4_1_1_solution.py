# sum up data
ds_cml_sum = ds_cml.sum(dim='time')
radar_ref_sum = radar_ref.sum(dim='time')

# interpolate rainfall using the lat and lon of the link midpoint. 
R_grid_idw = idw_interpolator(
    x=ds_cml_sum.lon_center,  # <------------------------- input x coordinates
    y=ds_cml_sum.lat_center,  # <------------------------- input y coordinates
    z=ds_cml_sum.R,  # <----- rainfall values
    xgrid=radar_ref.longitudes.values,  # <--------- target grid x coordinates
    ygrid=radar_ref.latitudes.values,  # <--------- target grid y coordinates
)

radar_ref_sum['R_grid_idw'] = (('y', 'x'), R_grid_idw)

R_grid_kriging = kriging_interpolator(
    x=ds_cml_sum.lon_center, 
    y=ds_cml_sum.lat_center, 
    z=ds_cml_sum.R,  # <----- rainfall values
    xgrid=radar_ref.longitudes.values,  # <--------- target grid x coordinates
    ygrid=radar_ref.latitudes.values,  # <--------- target grid y coordinates
)

radar_ref_sum['R_grid_kriging'] = (('y', 'x'), R_grid_kriging)

radar_ref_sum = radar_ref_sum.isel(x = slice(10, 30), y = slice(10, 40))

# such a 2-d array can be visulaized with matplotlibs pcolormesh function
fig, ax = plt.subplots(1, 3, figsize = (4*3, 4))

vmax=10

ax[0].set_title('IDW prediction')
im=ax[0].pcolormesh(radar_ref_sum.longitudes.values, radar_ref_sum.latitudes.values, radar_ref_sum.R_grid_idw, vmin=0, vmax=vmax)
plg.plot_map.plot_lines(ds_cml, use_lon_lat=True, ax=ax[0]) 
plt.colorbar(im, ax=ax[0])

ax[1].set_title('Kriging prediction')
im = ax[1].pcolormesh(radar_ref_sum.longitudes.values, radar_ref_sum.latitudes.values, radar_ref_sum.R_grid_kriging, vmin=0, vmax=vmax)
plg.plot_map.plot_lines(ds_cml, use_lon_lat=True, ax=ax[1])
plt.colorbar(im, ax=ax[1])   

ax[2].set_title('radar reference')
im = ax[2].pcolormesh(
    radar_ref_sum.longitudes.values, 
    radar_ref_sum.latitudes.values, 
    radar_ref_sum.rainfall_amount,vmin=0,vmax=vmax
)
plg.plot_map.plot_lines(ds_cml, use_lon_lat=True, ax=ax[2])
plt.colorbar(im, ax=ax[2])
plt.tight_layout();


# crop the radar and estimated rainfall fields so that we compare the interpolated pixels
radar_ref_crop = radar_ref_sum.isel(x = slice(10, 30), y = slice(10, 40))


fig, ax = plt.subplots(1, 2, figsize= (8, 4))
ax[0].hexbin(
    radar_ref_crop.rainfall_amount.values,
    radar_ref_crop.R_grid_idw.values,
    bins = 'log',
    gridsize = 40,
    extent = (0, 10, 0, 10),
    mincnt=1,
)
ax[0].set_title('IDW')
ax[0].set_xlabel('radar')
ax[0].set_ylabel('cml idw')

ax[1].hexbin(
    radar_ref_crop.rainfall_amount.values,
    radar_ref_crop.R_grid_kriging.values,
    bins = 'log',
    gridsize = 40,
    extent = (0, 10, 0, 10),
    mincnt=1,
)
ax[1].set_title('Kriging');
ax[1].set_xlabel('radar')
ax[1].set_ylabel('cml kriging')
plt.tight_layout()