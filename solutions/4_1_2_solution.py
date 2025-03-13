# remove short cml e.g. < 1500m
ds_cml_sum = ds_cml.sum(dim='time').where(ds_cml.length > 1500,drop=True)
# then same as last exercise