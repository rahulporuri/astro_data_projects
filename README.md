A collection of astronomical data available online and the science we can extract from them. 

There is a lot of free data online and a lot of places to access it from. One of my favorites is the [sdss skyserver](http://skyserver.sdss3.org/dr10/en/home.aspx). I intend to find this data, modify it and finally extract useful/popular results from it. There are basic/advanced/research projects available on the sdss dr10 [projects](http://skyserver.sdss3.org/dr10/en/proj/projhome.aspx) site. 

implemented so far -
* the HR diagram. data sets include 300 stars, 5000 stars, globular cluster dada and links to data from the Hipparchos and Tycho catalogues! 
* sdss object colors - 100,000 objects from the SDSS DR10.
* celestial plotting using matplotlib and galactic coordinates for quasars from the SDSS DR10.

to be implemented - 
* galactic distribution of stars and the evident spiral arms! - distance/parallax and l,b/ra,dec data from hipparcos/tycho.
* color-color diagram for galaxies to differentiate between the spirals and ellipticals.
* color-distance plots for galaxy clusters to prove that older galaxies lie at the center and that younger ones are at the outskirts.

implemeting the cosmic distance ladder, starting with
 * stellar parallax, hipparcos/tycho data already available.
 * stellar color data available from HR diagrams for main sequence fitting
 * RR lyrae and cepheid variable data. [HST data](http://iopscience.iop.org/1538-3881/133/4/1810/fulltext/205656.html), [pl relation using galactic variables](http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1993ApJ...418..135G&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf), [pl for type II cepheids](http://mnras.oxfordjournals.org/content/397/2/933.full), [cepheids in andromeda](http://www.aanda.org/index.php?option=com_article&access=bibcode&Itemid=129&bibcode=2007A%2526A...473..847VFUL). 
 * supernova data needed
 * Tully-Fisher data on the [HST key project paper](http://iopscience.iop.org/0004-637X/529/2/698/fulltext/) & [HST key project data](http://adsabs.harvard.edu/cgi-bin/nph-data_query?bibcode=2000ApJ...529..698S&db_key=AST&link_type=DATA), [TF calibrator galaxies](http://iopscience.iop.org/0067-0049/128/2/461/fulltext/) and [WISE TF](http://iopscience.iop.org/0004-637X/771/2/88/article)
 * hubble law data needed
 * (am i missing anything?)

for help with markdown, refer to the [*mastering markdown guide*](https://guides.github.com/features/mastering-markdown/) by github.
