<p align="center">
<a href="https://github.com/rodluger/showyourwork">
<img width = "450" src="https://raw.githubusercontent.com/rodluger/showyourwork/img/showyourwork.png" alt="showyourwork"/>
</a>
<br>
<br>
<a href="https://github.com/mathren/top_down_compact_obj_mass/actions/workflows/showyourwork.yml">
<img src="https://github.com/mathren/top_down_compact_obj_mass/actions/workflows/showyourwork.yml/badge.svg" alt="Article status"/>
</a>
<a href="https://github.com/mathren/top_down_compact_obj_mass/raw/ppisn_fit-pdf/arxiv.tar.gz">
<img src="https://img.shields.io/badge/article-tarball-blue.svg?style=flat" alt="Article tarball"/>
</a>
<a href="https://github.com/mathren/top_down_compact_obj_mass/raw/ppisn_fit-pdf/dag.pdf">
<img src="https://img.shields.io/badge/article-dag-blue.svg?style=flat" alt="Article graph"/>
</a>
<a href="https://github.com/mathren/top_down_compact_obj_mass/raw/ppisn_fit-pdf/ms.pdf">
<img src="https://img.shields.io/badge/article-pdf-blue.svg?style=flat" alt="Read the article"/>
</a>
</p>

# Building compact object masses top-down

Source and code associated to the research note [arXiv](link) created
with [showyourwork](https://github.com/rodluger/showyourwork).


Click on the rightmost badge at the top to take you to the compiled
article PDF.

##  Fit for the amount of mass loss at core-collapse supernova

We want to develop a new mapping between star (and core) mass and
compact object remnant for rapid population synthesis calculations.

Our aim is to have one way to calculate this across the entire mass
range (from neutron stars to above the pair-instability black hole
mass gap). Moreover, we want the mapping to be continuous. This is not
because it is a priori unphysical to have discontinuities, but because
we don't want to artificially introduce features. Free parameters can
be added later to control the appearance of discontinuities.

The idea is to calculate the mass of the compact object remnant as
total mass minus varius mass loss terms:

```
M_\mathrm{comp.\ obj} = M_\mathrm{pre-CC} - \left(\Delta M_\mathrm{SN} + \Delta M_{\nu, \mathrm{core}} + \Delta M_\mathrm{NLW} + \Delta M_\mathrm{PPI} + \cdots \right)
```

In this way, pre-explosion binary interactions reduce `M_\mathrm{pre-CC}`
already (and possibly modify the core masses), and then each mass loss
process at core-collapse can be added separately.  This can also be
extended to add other mass loss mechanisms at core-collapse

Note that while "building" the compact object mass from the bottom up
(e.g., the [Fryer et
al. 2012](https://ui.adsabs.harvard.edu/abs/2012ApJ...749...91F/abstract)
approach of starting with a proto neutron star mass and accrete the
fallback on it) makes it very difficult to use observationally
informed values for some of the terms in parenthesis. Conversely, in
our approach of "building" the compact object "top down" by removing
from the total mass the ejecta, we can use observationally informed
quantities for each term here if they are available.

If one (or more) of these terms have a stochastic component, this can
naturally produce the scatter in compact object masses expected
because of the stochasticity in supernova explosions (e.g., [Mandel&
Mueller 2020](https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.3214M/abstract).

## Reproducibility

The script `src/figures/fit_DM_PPI.py` generates the fitting formula,
its tex expression, and the figure in the research note automatically
through [showyourwork](https://github.com/rodluger/showyourwork).

The data from Table 1 in [Farmer et
al. 2019](https://ui.adsabs.harvard.edu/abs/2019ApJ...887...53F/abstract)
are automatically downloaded from
[zenodo](https://zenodo.org/record/3346593).

The notebook `notebooks/fit_DM_PPI.ipynb` contains more information, including a
new fit to the [Farmer et
al. 2019](https://ui.adsabs.harvard.edu/abs/2019ApJ...887...53F/abstract)
metallicity dependent pulsational pair-instability mass loss. We note
that recently [Mehta et al. 2021](http://arxiv.org/abs/2105.06366)
have produced more simulations showing the nuclear data in [Farmer et
al. 2019](https://ui.adsabs.harvard.edu/abs/2019ApJ...887...53F/abstract)
might be under-resolved and that can impact the BH masses predicted.
	
## Fit to Farmer et al. 2019 pulsational pair instability mass loss


![fit](./src/figures/fit_DM_PPI.png "title")



