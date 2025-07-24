# clean_unused_bib_entry
A short script to clean bib entries that are unused. Useful for lazy writers who copy a thousand of entries in the database then only use 1% of it.

## Steps:
Assume this is your current dir:
```
main.bib
output.aux
```

1. Call checkcites
Assume you use overleaf like me, you should be able to download output.aux file in the log panel. 
```bash
checkcites output.aux > a.txt
```

2. Simply run the python script
```bash
python checkcite_filter.py
```

That's it. 
