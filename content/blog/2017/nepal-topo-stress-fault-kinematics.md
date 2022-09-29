Title: Topographic modulation of fault kinematics in the Himalaya and Tibet
Date: 2017-12-19
Slug: nepal-topo-stress-fault-kinematics
Author: Richard Styron
Tags: active faults, Tibet, Himalaya, tectonics, earthquakes, stress, topographic stress
cover: ../images/2017/topo_kinematic_block_diagram.svg

*This is a draft of a manuscript I've been trying to find a home for; it will 
hopefully get submitted in the next several months, but in the mean time I want 
to at least get the idea out there in some form. I have been working through 
the idea for several years and I think it's pretty cool, so having some 
sunlight on it will be nice.*

*Update 2017-12-21: I have uploaded a PDF of the manuscript to the 
[EarthArXiv](https://eartharxiv.org/) preprint repository; you may find the 
link [here](https://eartharxiv.org/8z9ha), download a PDF and use the DOI for 
your citation needs.*


# Abstract

Throughout the Himalaya and Tibet, moderate- to high-elevation strike-slip 
faults undergo extensional stepovers where they cross pre-existing higher 
topography. Related seismological data have long been explained by an 
influential orogen-scale cross-section model where high-elevation normal 
faulting and low-elevation thrust faulting result from laterally-invariant 
horizontal tectonic stress and vertical stress that varies with topography; 
however, this model cannot incorporate strike-slip faulting or ~10 km 
wavelength topography. Therefore I introduce a 3D elastic model describing the 
modulation of fault kinematics by shorter-wavelength topographic stress, and 
show how this may tightly constrain the tectonic stress field. I then calculate 
the topographic stress field on the Western Nepal Fault System, and use 
topographic stresses and observed fault kinematics to invert for the tectonic 
stress field. The results yield a maximum tectonic compression of 0–0.2 $ρgz$ 
and minimum tectonic compression of -0.1–0.1 $ρgz$, and reproduce kinematics 
from normal, strike-slip and thrust faults and earthquakes in and around 
western Nepal, including the 2015 Gorkha earthquake. This demonstrates that 
where vertical and a horizontal principal stress are near equal, 1-10 km scale 
variations in topography can change fault kinematics, and that pre-existing 
topography can influence the location of subsequent faults and stepovers.

# Introduction

In the Himalaya and Tibet, it has long been observed that thrust earthquakes 
take place at the low-elevation rangefronts surrounding the plateau, while 
normal and strike-slip earthquakes occur in the elevated interior (e.g., 
*Molnar and Tapponnier, 1978; Elliott et al., 2010*) ([Figure 1a][wnfs-maps]). 
*Molnar and Lyon-Caen (1988)* offered an influential physical explanation for 
this simultaneous low-elevation reverse faulting and high-elevation normal 
faulting: Horizontal tectonic compression $\sigma_{H}$ (integrated over the 
crustal column) is essentially spatially invariant, while vertical compression 
$\sigma_{V}$ at depth varies with the height of the overlying terrain. At low 
elevations, $\sigma_{H} > \sigma_{V}$, leading to crustal thickening, while at 
higher elevations, $\sigma_{V} > \sigma_{H}$, causing crustal extension.

[![Active faulting of Tibet and the Himalaya][wnfs-maps]][wnfs-maps]

*__Figure 1A__: Active faults, seismicity and topography of the Tibetan 
Plateau. __B__: Map of the southeastern KF and WNFS. KF=Karakoram Fault. 
ATF=Altyn Tagh Fault. T=Tanggula Range. GM=Gurla Mandhata Detachment. G=Gar 
Basin. TF=Talphi Fault. TDF=Tibrikot-Dogari Faults. BGF=Bari Gad Fault. Focal 
mechanisms from the GCMT Catalog (Ekström et al. 2012). Faults modified from 
HimaTibetMap v. 1.2 (Styron et al. 2010).*

[wnfs-maps]: {static}/images/2017/wnfs_tib_maps.svg

These observations and hypotheses concern entire orogens. Whether they apply at 
smaller scales is a natural question, though unaddressed. The analytical model 
by *Molnar and Lyon-Caen (1988)* rests on the assumption of 
isostatically-supported topography, which is valid over $10^{2}$–$10^{3}$ km 
scales (i.e., orogens), but may not be over 1-10 km (mountain to mountain 
range) scales, where topography is mostly supported elastically (e.g., 
*Bollinger et al. 2004*). Additionally, topographic slopes at these scales may 
impart locally substantial stresses in the upper crust, which may be smoothed 
out at larger scales. The motivating observations are typically earthquake 
focal mechanisms, which are too sparse spatially and from too short a time 
window to fully describe high-resolution deformation.

However, neotectonic mapping provides a more complete description of the 
deformation field integrated over longer timescales ($10^{3}$-$10^{5}$ years) 
and offers better spatial coverage and resolution as well. Recent neotectonic 
maps of the Himalaya and Tibet reveal a rich interaction between fault type and 
elevation over 1-100 km scales ([Figure 1][wnfs-maps]). These observations 
document changes in the kinematics of large fault systems where the faults 
cross smaller topographic features (ridges to mountain ranges); as the 
topography is often known to be older than the active faults, it is likely that 
topography modifies fault kinematics at these scales as well, though the 
mechanisms may be different than in the orogen-scale, isostatic case. 
Documenting this phenomenon is the first objective of this study.

If topography is capable of modifying fault kinematics, then the total 
(tectonic plus topographic) stress field must resolve on the faults with shear 
stress directions that are consistent with the directions of fault slip. 
Therefore, if the topographic stresses can be calculated, these stresses and 
the fault kinematics may be used to constrain the tectonic stress field. 
Precise estimation of tectonic stress is a major advancement for understanding 
earth processes. Stress is generally unknown at the order of magnitude level, 
despite being a fundamental physical property of the earth, and the primary 
control on the earth's deformation. Accurate stress estimates are critical for 
understanding the distribution of seismicity in time and space, as well as the 
physical properties and evolution of faults and orogens. This quantification is 
the second objective of this study. 

# Fault kinematic transitions and topography in Tibet and the Himalaya

Many fault zones within the Tibetan plateau and vicinity show transitions in 
fault kinematics with changes in topography ([Figure 1][wnfs-maps]). These are 
best displayed in transtensional fault zones in the elevated interior of the 
plateau, consistent with the hypothesis that Tibet is at the maximum elevation 
that can be sustained by horizontal tectonic compression (e.g., *Molnar and 
Lyon-Caen, 1988*). For example, the sinistral Longmu Co–Gozha Co fault system 
has a major extensional stepover where the fault crosses the western Kunlun 
Shan, where the 2008 $M_{w}$ 7.1 Yutian earthquake occurred (*Xu et al., 
2013*). Left-lateral faulting continues to the northeast of the high mountains 
as the faults merge with the Altyn Tagh Fault. Similarly, the transtensional 
Yibug Caka and Mugu Purou rifts in central Tibet show local extensional 
stepovers where topography is elevated (*Taylor et al., 2003*; *Ratschbacher et 
al., 2011*), and the conjugate strike-slip systems to their south link to rifts 
where regional elevation steps higher. This is evident in individual 
earthquakes as well: *Chang et al.* (*2016*) observe localized extensional 
fault scarps near isolated high mountains on the western end of the 2001 
$M_{w}$ 7.8 Kunlun rupture.

Additionally, most isolated topographic highs on the plateau outside of 
transtensional zones are cut by active normal faults that do not extend far 
into the lower surroundings; the Gangdese ([Figure 1b][wnfs-maps]) and Tanggula 
Ranges ([Figure 1a][wnfs-maps]) are prime examples. In these locations, the 
horizontal differential stress may not be great enough for fault failure, but 
high $\sigma_{V}$ underneath the ranges causes localized normal faulting.

Perhaps the most clear example of topographic modulation of fault kinematics is 
on the southeastern Karakoram–Western Nepal Fault System, which undergoes three 
distinct extensional stepovers, one for each instance in which the fault system 
intersects pre-existing topographic highs ([Figure 1b][wnfs-map]).

The Karakoram Fault (KF) is a major dextral fault on the boundary between the 
northwestern Himalaya and southwestern Tibet. The KF is purely strike-slip 
through most of its length but has a transtensional zone where it cuts through 
the Gangdese Range called the Gar Basin (*Sanchez et al., 2010*), and 
terminates at the Pulan Graben (dominated by the Gurla Mandhata Detachment, 
GMD) where the KF hits the northern Himalaya (*Murphy et al., 2002*). Some or 
all of the KF slip is transferred to the GMD and south into the Himalaya along 
the Humla Fault (*Murphy and Burgess, 2006*).

Though the nature of fault connectivity remains unclear, it is likely that 
dextral slip continues through the Himalayan wedge along the Western Nepal 
Fault System (WNFS). Dextral and normal slip has been observed on the Tibrikot 
and Dogari segments of the WNFS (*Murphy et al., 2014; Silver et al., 2015*). 
Additional dextral fault offsets have been observed on the Talphi and Bari Gad 
Faults to the northwest and southeast of the Tibrikot fault (*Nakata, 1989*).

A striking feature of the overall geometry of the KF-GMD-WNFS faults is that 
extensional stepovers occur wherever the strike-slip faults encounter locally 
high terrain ([Figure 1b][wfs-maps]). The higher terrain in all cases predates 
the strike-slip faulting along the KF-WNFS system: The Gangdese Range was a 
regional topographic high and sediment source by the Oligocene (*Leary et al., 
2016*), predating the post-middle Miocene faulting in Gar Basin (*Sanchez et 
al., 2010*), while the Himalaya was uplifted to near modern elevation by the 
Miocene (*Garzione et al., 2000*), before extension. Extension along the GMD 
has resulted in great uplift of the footwall (>7700 m), but normal faulting 
must cause a net decrease in regional elevation despite local footwall uplift. 
Additionally, faults associated with the current dextral-normal slip regime cut 
north-dipping brittle and ductile fault fabrics associated with the uplift of 
the Himalaya (*Silver et al., 2015*). It may be that the WNFS becomes 
transpressive in its low-elevation southern extent, as the Bari Gad fault nears 
the active Himalayan frontal folds and thrusts; this is observed on the 
symmetrical Altyn Tagh fault system on Tibet's northern margin (*Cowgill et 
al., 2004*).

# Three-dimensional topographic and tectonic stresses

The regional-scale topography and stress relationship described here share the 
central concept developed in the orogen-scale models, that changes in fault 
style result from variable, primarily vertical topographic stresses superposed 
on relatively invariant, primarily horizontal tectonic stresses ([Figure 
2][fig_block]). However, the regional model has some key differences, as well.


[![Block diagram indicating the stress and topography 
relationships][fig_block]][fig_block]

*__Figure 2__: Schematic block diagram demonstrating the relationships
between stress, topography and faulting. $\sigma_{H}$ and $\sigma_{h}$
(represented by $\sigma_{E}$ and $\sigma_{N}$) are invariant across the
region though $\sigma_{V}$ varies with topography, changing fault
kinematics.*

[fig_block]: {static}/images/2017/topo_kinematic_block_diagram.svg

First, this problem is inherently three-dimensional. Faults of all kinematic 
types in the Himalaya and Tibet accommodate ~N-S shortening, ~E-W extension, or 
both ([Figure 1][wnfs-maps]). This allows us to expand the model's 
dimensionality: The two-dimensional model has $\sigma_{H} > \sigma_{V}$ 
(reverse faulting) in the lowlands and $\sigma_V > \sigma_H$ (normal faulting) 
in the highlands. But we can add a dimension, with $\sigma_H > \sigma_h > 
\sigma_V$ in the lowlands, $\sigma_H > \sigma_V > \sigma_h$ in regions of 
moderate elevations, and $\sigma_{H} > \sigma_{h} > \sigma_{V}$ in the 
highlands, where $\sigma_{h}$ is the minimum principal horizontal stress 
([Figure 2][fig_block]). This expansion enables us to consider faults of all 
styles and orientations (not only those striking perpendicularly to the 2D 
model's cross-section), and to calculate the full 3D stress tensor field. 
Furthermore, if $\sigma_{H}$ and $\sigma_{h}$ are not near equal, there may be 
a large elevation gap between reverse and normal faulting, leading to large 
uncertainties in stress estimations in the 2D model (*Richardson and Coblentz, 
1994*). By considering all three fault styles and principal stresses, the 
uncertainties are much reduced.

Secondly, shorter-wavelength topography is supported elastically rather than 
isostatically (e.g., *Bollinger et al., 2004*). This means that topographic 
stresses may vary dramatically over short horizontal and vertical distances, 
slopes may impart locally strong horizontal stress, and the perturbation to the 
stress field produced by topography extends outward and downward rather than 
simply being a simply vertical sum of the weight of the overlying rocks. As a 
result, short-wavelength topographic stresses may be spatially variable and 
resolve very differently along-strike and down-dip on a through-going fault.

Finally, the regional model does not require invariance of tectonic stress over 
$10^{2} - 10^{3}$ km, only over $10^{0} - 10^{2}$ km. Tectonic stress may 
change over longer distances due to changes in boundary conditions (e.g., plate 
driving forces) and lithospheric rheology. While *Molnar and Lyon-Caen* 
(*1988*) do provide compelling arguments for stress invariance across orogens, 
such invariance is not a requirement of this model. Consistent application of 
stress inversions using the regional model (as below) in many locations 
throughout an orogen may serve as a test of orogen-scale tectonic stress 
invariance.

## Topographic stress

To test the hypothesis that the topography-fault kinematics relationship is 
based on a varying topographic stress superposed on a laterally-invariant 
tectonic stress field, I seek to reproduce the observed fault kinematics by 
calculating the topographic and tectonic stress fields, and resolving them on 
3D fault models in the region, following methods outlined in *Styron and 
Hetland* (*2015*). The topographic stress calculations are deterministic, as 
topography is well known and allowable variation in the Earth's elastic moduli 
does not meaningfully modify the results. The tectonic stresses are solved for 
using a Bayesian inversion scheme. To avoid overfitting and assess the veracity 
of results beyond the study region, the inversion is performed on two 
relatively well-studied faults, the Gurla Mandhata and Tibrikot-Dogari faults, 
and then validated on additional deformation data in the region: a coseismic 
slip model from the 2015 $M_{w}$ 7.8 Gorkha, Nepal earthquake (*Galetzka et 
al., 2015*) and pre-Gorkha focal mechanisms throughout the region. The two 
faults modeled here were selected because the fault geometry and kinematics are 
well known through field (*Murphy et al., 2002; Silver et al., 2015*) and 
thermochronological (*McCallister et al., 2014*) studies; the other faults in 
the WNFS have not received sufficient study to model confidently.

The topographic stresses are calculated through elastic halfspace methods 
following *Liu and Zoback (1992)* and *Styron and Hetland (2015)*, by a 
convolution of functions describing the distribution of topographic loading on 
the halfspace surface with Green's functions describing the propagation of 
stresses in the halfspace from vertical and horizontal point loads on the 
surface. This results in a 3D array with the 3x3 topographic stress tensor 
calculated at every point (500 m horizontal resolution, 1 km vertical 
resolution) in a ~840x700 km region. The halfspace surface is set to sea level, 
though calculations above 1500 m below sea level are discarded due to concerns 
of overestimating shallow topographic stress where slopes are steep, a known 
limitation of the perturbation-expansion method used.

The Gurla Mandhata and Tibrikot-Dogari fault traces are extended to depth based 
on contraints from structural data and thermal modeling. The fault surfaces are 
made into a triangular mesh, and the stress tensors are then interpolated onto 
them using barycentric interpolation. The rake of the maximum shear stress on 
each fault patch is calculated based on the strike and dip of that fault patch.

## Tectonic stress

I then solve for the allowable tectonic stresses through a Bayesian inversion, 
seeking to minimize the misfit between the rake of the resolved total stress 
tensor (topographic plus tectonic) and the observed slip rake. The tectonic 
stress field $T$ is assumed to increase linearly with depth below the halfspace 
surface (*Townend and Zoback, 2000*), and so is scaled to be a fraction of 
lithostatic pressure below the halfspace surface (i.e., $ρgz$, where $ρ$ = 2700 
kg m$^{-3}$). $T$ is horizontal, and has three components: $T_{\max}$, 
$T_{\min}$ and $T_{\text{az}}$ (the azimuth of $T_{\max}$). $T_{\max}$ has a 
uniform prior from [0—1) $ρgz$, $T_{\min}$ has a uniform prior of [-1—1) 
$T_{\max}$ ($T_{\min}$ is by definition smaller than $T_{\max}$ and therefore 
cannot be independently defined in terms of $ρgz$), and $T_{\text{az}}$ has a 
uniform prior of 0°—359°. Each sample of $T$ is then rotated to $T_{N - S}$, 
$T_{E - W}$, and $T_{N - E}$ (the horizontal shear stress) and added to the 
topographic stress tensor at each point.

For each of 1 million samples, the mean rake misfit $\bar{\lambda^{m}}$ is 
calculated as the mean of the absolute value of the rake differences between 
the observed slip rake and modeled maximum shear stress rake. Then, the 
relative likelihood of each sample set is calculated as
$p(D|T) = \frac{\exp(\kappa \cos \bar{\lambda^m})}{\exp(\kappa \cos
\bar{\lambda^m_{\max}})}$ where $\kappa$ is a scale term, reflecting the 
uncertainty in the rake data.

The posteriors $p(T|D)$ are then sampled proportionally to the relative 
likelihood, following Bayes' rule: $p(T|D) \propto p(T)\, p(D|T)$.

## Results

Topographic stresses tend to be in the direction of fault slip, particularly 
for the dip-slip faults, including the Gorkha rupture plane, which is loaded in 
a thrust sense by slope-induced subhorizontal compression. Tectonic stresses 
are not working against topography in the Himalaya.

[![Tectonic stress results][fig_T_results]][fig_T_results]

[fig_T_results]: {static}/images/2017/wnfs_tect_stress_hists.svg

*__Figure 3A__: Scatterplot with marginal histograms of the inversion results
for $T_{\max}$ and $T_{\min}$. __B__: Rose diagram for $T_{\text{az}}$.*


The results of the tectonic stress inversion are shown in [Figure 
3][fig_T_results]. The maximum posterior values for the joint posterior 
distribution (i.e., the location of the highest posterior probability density 
in the 3-variable space) are $T_{\max} = 0.1 \, ρgz$ (~2.7 MPa km$^{-1}$ 
depth), $T_{\min} = - 0.1\, ρgz$, and $T_{\text{az}} = 20°$. The mean absolute 
misfit between the observed and modeled fault rakes for the maximum posterior 
model is 26°. The 1D marginals are somewhat similar; $T_{\max}$ has a mode at 
<0.05 $ρgz$, $T_{\min}$ has a mode near 0, with a tensile skew, and 
$T_{\text{az}}$ has a mode at 20°, parallel to the direction of the Indo-Asian 
convergence (*e.g., Gan et al., 2007*).

These results agree well with regional earthquake data not used in the 
inversion: The maximum-likelihood tectonic stresses were scaled to depth and 
added to the topographic stress tensor at each point in a coseismic slip model 
from the 2015 Gorkha, Nepal earthquake (*Galetzka et al., 2015*) and pre-Gorkha 
focal mechanisms from the central Himalaya and southern Tibet (*ISC*). The 
total stress tensors were resolved on each fault plane and the predicted shear 
stress rake was compared to the observed slip rake. The rakes matched very well 
(<30° misfit) for nearly all data points, regardless of whether the data were 
from thrust, normal or strike-slip earthquakes ([Figure S1). This confirms the 
predictive power of this simple model where spatially-varying topographic 
stress coupled with depth-scaled tectonic stress control a complicated 
deformation field.

[![Figure S1 A,B][fig_s1]][fig_s1]

[fig_s1]: {static}/images/2017/wnfs_s1.svg

*__Figure S1 A__: Maps of south-central Tibet and the Nepal Himalaya showing 
the goodness of fit of the model results.  __B__: Map of the results for the 
2015 Gorkha earthquake (from Galetzka 2015). Note that the observed rakes (in 
red) show much greater scatter than the modeled rakes; I am not sure if this is 
a modeling artefact or not.*

To test the effects of topographic stress (versus simply fault geometry) on 
replicating the shear stresses on the faults, the stress inversion procedure 
was repeated without topographic stresses on the fault planes, while holding 
all else constant. The results yield a most-likely model with $T_{\max} = 
0.05\,ρgz$, $T_{\min} = - 1.15\,ρgz$, and $T_{\text{az}} = 18$; 
$\bar{\lambda^{m}}$ is about 10° higher. The strong tension for $T_{\min}$ is 
required to induce normal-sense shear on the extensional stepovers in the 
absence of strong vertical compression underneath topography. Though the misfit 
is acceptable, it is unclear how orogen-parallel tension greater than $ρgz$ 
could be generated in the Himalaya; block divergence due to variably-oblique 
convergence along the curved Himalayan front should induce some tension 
(*McCaffrey and Nábelek, 1998*), although $ρgz$ is quite high. Additionally, 
unlike topographic stress, tectonic stress alone does not predict the location 
of extensional stepovers; it simply is able to match the slip rake on the 
existing stepovers to some degree.

The stress results are consistent with Himalayan thrusting: $T_{\max} = 0.1\, 
ρgz$ ≈ 7 MPa on a 10° dipping plane at 15 km, which is approximately equal to 
the location and magnitude of the maximum stress drop (~8 MPa) of the Gorkha 
earthquake (*Galetzka et al., 2015*), suggesting that tectonic stress drop may 
have been locally complete during this earthquake. However, shear stresses from 
topography on the Gorkha fault plane are <20 MPa here, so total shear stress 
drop was not complete.

[![Figure S1 C, D][fig_s2]][fig_s2]

[fig_s2]: {static}/images/2017/wnfs_s2.svg

*__Figure S1 C__: Map of the Gurla Mandhata detachment showing the observed and 
modeled rakes, and fault mesh.  __D__: Map of the Tibrikot-Dogari fault showing 
the observed and modeled rakes, and fault mesh.*

# Discussion

In Tibet and the Himalaya, topography likely modulates fault kinematics over 
~10 km scales by locally changing the relative magnitudes of $\sigma_{V}$ to 
$\sigma_{H}$ and $\sigma_{h}$. Pre-existing topographic highs produce high 
$\sigma_{V}$ in the crust beneath, causing extensional stepovers in younger 
strike-slip faults cutting through the topography. This phenomenon is only 
possible where the larger-scale balance of stresses is such that $\sigma_{V} > 
\sigma_{H}$ under topographic highs but $\sigma_{H} > \sigma_{V}$ in adjacent 
lower locations. By computing topographic stress, the orientions and magnitudes 
of $\sigma_{H}$ and $\sigma_{h}$ can be tightly constrained.

In the study areas, the topographic relief (not necessarily the modern 
elevation) predates the current tectonic regime and associated faults, and is 
therefore capable of controlling the location of releasing bends in strike-slip 
faults, as well as isolated grabens (e.g., in the Gangdese range). This may be 
common in orogens with a polyphase or protracted history (yielding enough 
paleorelief) which finally reach a broad equivalence between $\sigma_{V}$ and 
$\sigma_{H}$. However, evidence of this process may be erased with erosion, and 
the process may even reverse as stepover-produced topography builds: *Cowgill 
et al.* (*2004*) suggest that the kinematics of some stepovers on the Altyn 
Tagh fault change due to increasing topography and $\sigma_{V}$.

The tectonic stresses estimated are, perhaps, low for creating the world's 
current highest mountain range. They are significantly lower than those 
estimated at $T_{\max} = 0.5 - 1\,ρgz$ in eastern Tibet with the same methods 
(*Styron and Hetland, 2015*), or $T_{\max} = 1.0\,ρgz$ measured from the upper 
2.5 km of the SAFOD pilot hole on the San Andreas (*Hickman and Zoback, 1994*). 
However, as differential stress is limited by the strength of faults, low 
$T_{\max}$ may be due to a weak Main Himalayan thrust, marking a similarity 
with subduction zone megathrusts (e.g., *Houston, 2015*).

## Acknowledgements

I thank Lydia Staisch, Kurt Sundell and Mike Taylor for comments on drafts of 
this manuscript. All data and code can be found at 
<https://github.com/cossatot/wnfs_stress/>.

# References cited

Bollinger, L., Avouac, J. P., Cattin, R., & Pandey, M. R. (2004). Stress
buildup in the Himalaya. Journal of Geophysical Research: Solid Earth,
109(B11).

Chang, H., Li, L. Y., Molnar, P., & Niemi, N. A. (2016). Activation of a
Minor Graben and Pull-Apart Basin Just East of Bukadaban during the 2001
Kunlun Earthquake (Mw 7.8). Bulletin of the Seismological Society of
America.

Elliott, J. R., Walters, R. J., England, P. C., Jackson, J. A., Li, Z.,
& Parsons, B. (2010). Extension on the Tibetan plateau: recent normal
faulting measured by InSAR and body wave seismology. Geophysical Journal
International, 183(2), 503-535.

Galetzka, J., Melgar, D., Genrich, J.F., Geng, J., Owen, S., Lindsey,
E.O., Xu, X., Bock, Y., Avouac, J.P., Adhikari, L.B. and Upreti, B.N.,
2015. Slip pulse and resonance of the Kathmandu basin during the 2015
Gorkha earthquake, Nepal. Science, 349(6252), pp.1091-1095.

Garzione, C.N., Dettman, D.L., Quade, J., DeCelles, P.G. and Butler,
R.F., 2000. High times on the Tibetan Plateau: Paleoelevation of the
Thakkhola graben, Nepal. Geology, 28(4), pp.339-342.

Houston, H. (2015). Low friction and fault weakening revealed by rising
sensitivity of tremor to tidal stress. Nature Geoscience, 8(5), 409.

International Seismological Centre, On-line Bulletin,
http://www.isc.ac.uk, Internatl. Seismol. Cent., Thatcham, United
Kingdom, 2013.

Leary, R., Orme, D.A., Laskowski, A.K., DeCelles, P.G., Kapp, P.,
Carrapa, B. and Dettinger, M., 2016. Along-strike diachroneity in
deposition of the Kailas Formation in central southern Tibet:
Implications for Indian slab dynamics. Geosphere, 12(4), pp.1198-1223.

Liu, L. and Zoback, M.D., 1992. The Effect of Topography on the State of
Stress in the Crust: Application to the Site of the Cajon Pass
Scientific Drilling Project. Journal of Geophysical Research, 97(B4),
pp.5095-5108.

McCaffrey, R. and Nabelek, J., 1998. Role of oblique convergence in the
active deformation of the Himalayas and southern Tibet plateau. Geology,
26(8), pp.691-694.

McCallister, A.T., Taylor, M.H., Murphy, M.A., Styron, R.H. and Stockli,
D.F., 2014. Thermochronologic constraints on the late Cenozoic
exhumation history of the Gurla Mandhata metamorphic core complex,
Southwestern Tibet. Tectonics, 33(2), pp.27-52.

Molnar, P. and Lyon-Caen, H., 1988. Some simple physical aspects of the
support, structure, and evolution of mountain belts. Geological Society
of America Special Papers, 218, pp.179-208.

Molnar, P. and Tapponnier, P., 1979. Active tectonics of Tibet. Journal
of Geophysical Research: Solid Earth, 83(B11), pp.5361-5375.

Murphy, M.A. and Burgess, W.P., 2006. Geometry, kinematics, and
landscape characteristics of an active transtension zone, Karakoram
fault system, southwest Tibet. Journal of Structural Geology, 28(2),
pp.268-283.

Murphy, M.A., Taylor, M.H., Gosse, J., Silver, C.R.P., Whipp, D.M. and
Beaumont, C., 2014. Limit of strain partitioning in the Himalaya marked
by large earthquakes in western Nepal. Nature Geoscience, 7(1),
pp.38-42.

Murphy, M.A., Yin, A., Kapp, P., Harrison, T.M., Manning, C.E., Ryerson,
F.J., Lin, D. and Jinghui, G., 2002. Structural evolution of the Gurla
Mandhata detachment system, southwest Tibet: Implications for the
eastward extent of the Karakoram fault system. Geological Society of
America Bulletin, 114(4), pp.428-447.

Nakata, T., 1989. Active faults of the Himalaya of India and Nepal.
Geological Society of America Special Papers, 232, pp.243-264.

Richardson, R.M. and Coblentz, D.D., 1994. Stress modeling in the Andes:
Constraints on the South American intraplate stress magnitudes. Journal
of Geophysical Research: Solid Earth, 99(B11), pp.22015-22025.

Sanchez, V.I., Murphy, M.A., Dupré, W.R., Ding, L. and Zhang, R., 2010.
Structural evolution of the Neogene Gar Basin, western Tibet:
Implications for releasing bend development and drainage patterns.
Geological Society of America Bulletin, 122(5-6), pp.926-945.

Silver, C.R., Murphy, M.A., Taylor, M.H., Gosse, J. and Baltz, T., 2015.
Neotectonics of the Western Nepal Fault System: Implications for
Himalayan strain partitioning. Tectonics, 34(12), pp.2494-2513.

Styron, R.H. and Hetland, E.A., 2015. The weight of the mountains:
Constraints on tectonic stress, friction, and fluid pressure in the 2008
Wenchuan earthquake from estimates of topographic loading. Journal of
Geophysical Research: Solid Earth, 120(4), pp.2697-2716.

Styron, R., Taylor, M. and Okoronkwo, K., 2010. Database of active
structures from the Indo-Asian collision. Eos, Transactions American
Geophysical Union, 91(20), pp.181-182.

Taylor, M., Yin, A., Ryerson, F.J., Kapp, P. and Ding, L., 2003.
Conjugate strike-slip faulting along the Bangong-Nujiang suture zone
accommodates coeval east-west extension and north-south shortening in
the interior of the Tibetan Plateau. Tectonics, 22(4).

Townend, J. and Zoback, M.D., 2000. How faulting keeps the crust strong.
Geology, 28(5), pp.399-402.



