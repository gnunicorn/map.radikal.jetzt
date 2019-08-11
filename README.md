# map.radikal.jetzt


## Updating upstream orgs

**One time setup**

```shell
virtualenv vendor
source vendor/bin/activate
pip install -r vendor/requirements
```

To update run (from within the virtualenv):

```
# ER
rm _data/xr.json
scrapy runspider vendor/scripts/update_xr.py -o _data/xr.json -t json
```



## TODO

 - [ ] add tagging to map
 - [ ] add data infrastructure
 - [ ] replace map token in js
 - [ ] add contribute and imprint


