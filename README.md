# quickpedia

A Wikipedia CLI tool.

## Features

Currently lets you search for a topic, and summarizes the closest result.

Also lets you write to a file, instead of print to the terminal.

## Todo

* Make you be able to choose between closest result, or list of results.

## Requirements.

* wikipedia

### Installing and running

```batch
git clone https://github.com/TyGillespie/quickpedia
cd quickpedia
pip install -r requirements.txt
python quickpedia.py "terms to search for"
```

## Note

If you want to search more than one word, please put the intire search in quotes. This is due to the current way we're using Argparse (I'm not sure if there's a way to fix this).
