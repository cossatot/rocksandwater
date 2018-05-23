title: A quick thought on model fitting and extrapolation
date: 2017-09-21
author: Richard Styron
slug: model-fitting-and-extrapolation
tags: quick and regrettable thoughts, rant, statistical seismology
status: draft

I was reading [David Vere-Jones's][dvj] interesting [thoughts on the education 
of a statistical seismologist][0] at the wonderful [CORSSA][1] site. Vere-Jones 
makes a common remark:

> [something to the effect of] it's better to choose a real stochastic model 
> than to stick with a purely descriptive model, because descriptive models are 
> only valid within the range of the data, and cannot be meaningfully 
> extrapolated.

This is advice that should definitely be considered thoroughly, but I'm not 
sure that I agree, especially in the circumstances being discussed (statistical 
modeling of earthquake occurrence). Vere-Jones speaks from decades of 
experience as one of the most prominent and influential earthquake 
statisticians, but he is foremost a statistician, and it's no surprise that he 
prefers prescriptive to descriptive behavior.

However, I think a bit more skepticism of parametric, stochastic models is 
warranted, especially for something like earthquake occurrence. The big issues 
are that we don't have a solid-enough grasp of the physics of the earthquake 
process in order to build a reasonably physically-based stochastic model (in 
the vein of statistical physics models). Furthermore, it is not at all certain 
that the behavior of earthquake faults is similar enough between different 
regions, tectonic regimes and fault types to allow for a single model 


Vere-Jones's major concern, that descriptive models aren't capable of 
accurately describing behavior outside of the range of the observations, is 


This is highlighted by the lack of a suitable stochastic model for representing 
fault network behavior, with the exception of a multivariate Poisson model. 
There are some regional or spatiotemporal models such as ETAS, but these don't 
really incorporate faults; they are still point-process models and earthquake 
locations are more or less spatial Markov processes, without any prior 
information on spatial occurrence (such as that major earthquakes happen on 
pre-existing faults).


[dvj]
[0]
[1]
