---
title: Installing OpenQuake with Conda
author: Richard Styron
date: 2022-11-02
slug: installing-openquake-with-conda
---

*Warning! This is not officially supported!*

I use [conda](https://conda.io) extensively to manage Python environments. 
While I have my frustrations with it, in particular the slow and brittle 
dependency solver, it services my needs rather well.

However, no one else at GEM uses it, so it's not supported as an environment 
host for *OpenQuake*. Nonetheless, here's what I do in general (though this 
seems to change slightly every year or so, whenever I make a new environment 
for whatever reason). Note that this involves installing from source (i.e., 
GitHub), rather than releases, on Linux or MacOS (or with WSL on Windows), 
though you could do it from the source code from a given point release if you 
need a specific version. I assume you already have conda installed.

**Step 1:** Clone (or download) the engine from 
[GitHub](https://github.com/gem/oq-engine/) and go into the `oq-engine/` 
directory.
```
git clone git@github.com:gem/oq-engine.git
```

**Step 2:** Go to requirements-py3x-yyyy.txt (for the platform and Python 
version you're using) and comment out the line with `certifi` (`conda` will 
install a newer version that is uniquely compatible with the exact version of 
Python it installs).

**Step 3:** Make a new conda environment with the Python version you want.
```
conda create -n oq python=3.9
```

**Step 4:** Activate the new environment.
```
conda activate oq
```

**Step 5:** Install the requirements with `pip`.
```
pip install -r requirements-py3x-yyyy.txt
```

**Step 6:** (Optional but highly recommended) Install Numba, which is easiest 
through conda. This will also install a lot of other libraries for numerical 
computing, e.g. BLAS and MKL. (*Note, `numba` may already be installed by the 
`requirements.txt` file*)
```
conda install numba
```

**Step 7:** Install the OpenQuake Engine in development mode.
```
pip install -e .
```


And that should work!
