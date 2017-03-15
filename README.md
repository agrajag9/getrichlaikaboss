# getrichlaikaboss

Get Rich Headers from LaikaBOSS JSON and return a list of PE compilation tools

Requires:

Python 3

https://github.com/lmco/laikaboss

https://github.com/dishather/richprint

## Usage ##

Using `result.json` produced by LaikaBOSS `laika.py`:

```
$ ./getrichlaikaboss --comp_ids comp_ids.txt --infile result.json
```

## Future Improvments ##

* Add more ID and Verison tuples to `comp_ids.txt`
* I'm sure there's lots of improvements that could be made in my exception handling
