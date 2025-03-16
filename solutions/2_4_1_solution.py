ds_cml = ds_cmls.isel(cml_id=123)

# Full processing
ds_cml['rsd'] = ds_cml.tl.rolling(time=60*6, center=True).std() 
ds_cml['roll_std_threshold'] = 1.2 * ds_cml.rsd.quantile(0.80, dim='time')
ds_cml['wet'] = ds_cml.rsd > ds_cml.roll_std_threshold

ds_cml['baseline'] = pycml.processing.baseline.baseline_constant(
    trsl=ds_cml.tl, 
    wet=ds_cml.wet, 
    n_average_last_dry=5*6)  # use average of TL of last 5 minutes

ds_cml['A_obs'] = ds_cml.tl - ds_cml.baseline
ds_cml["A_obs"] = ds_cml.A_obs.where(ds_cml.A_obs >= 0, 0)
ds_cml['waa'] = pycml.processing.wet_antenna.waa_pastorek_2021_from_A_obs(
    A_obs=ds_cml.A_obs,
    f_Hz=ds_cml.frequency * 1e6,
    pol=ds_cml.polarization.data,
    L_km=ds_cml.length / 1000,
    A_max=3,
    zeta=0.7,  
    d=0.15, 
)

# subtract baseline and wet antenna attenuation from total path loss
ds_cml['A'] = ds_cml.tl - ds_cml.baseline - ds_cml.waa
# set negative values to zero
ds_cml['A'] = ds_cml.A.where(ds_cml.A > 0, 0) 

ds_cml['R'] = pycml.processing.k_R_relation.calc_R_from_A(
    A=ds_cml.A, 
    L_km=float(ds_cml.length)/1000, 
    f_GHz=ds_cml.frequency/1000,
    pol=ds_cml.polarization
)