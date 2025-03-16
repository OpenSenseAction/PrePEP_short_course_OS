ds_cml["A_obs"] = ds_cml.tl - ds_cml.baseline
ds_cml["A_obs"] = ds_cml.A_obs.where(ds_cml.A_obs >= 0, 0)
ds_cml["waa"] = pycml.processing.wet_antenna.waa_pastorek_2021_from_A_obs(
    A_obs=ds_cml.A_obs,
    f_Hz=ds_cml.frequency * 1e6,
    pol=ds_cml.polarization.data,
    L_km=ds_cml.length / 1000,
    A_max=6,
    zeta=0.7,  
    d=0.15, 
)

# calculate attenuation caused by rain and remove negative attenuation
ds_cml["A"] = ds_cml.tl - ds_cml.baseline - ds_cml.waa
ds_cml["A"] = ds_cml.A.where(ds_cml.A > 0, 0)


# Plot 
waa_plot(ds_cml)

