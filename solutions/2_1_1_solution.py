tsl_range = ds_cmls.tsl.max(dim='time') - ds_cmls.tsl.min(dim='time')
tsl_range.plot.hist(bins=50, figsize=(14, 4));