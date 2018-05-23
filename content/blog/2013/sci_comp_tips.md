Title: Some tips for new scientific programmers
Date: 2013-12-20
Slug: sci-comp-tips
Tags: matlab, python, programming


*This post is slightly modified from an email that I wrote to some friends
 who were looking for tips on getting started with scientific 
 computing with MATLAB. I'm not the world's 
expert on the subject, and I traded MATLAB for Python a couple years back,
but the advice should be solid for newcomers in either language.*


There are 3 broad categories of matlab/general coding best practices: 
performance things, code reusability, and readability.

#### For performance
Preallocate arrays (make empty ones of the final size) instead of creating 
them within loops; otherwise MATLAB will have to find new space in memory
for the new array, make it, and delete the old one, etc. each loop iteration.

Learn to vectorize where possible instead of for loops.

Other, more general tips:
 
[http://www.mit.edu/~pwb/cssm/GMPP.pdf](http://www.mit.edu/~pwb/cssm/GMPP.pdf)

[http://www.mathworks.com/matlabcentral/fileexchange/5685-writing-fast-matlab-code](http://www.mathworks.com/matlabcentral/fileexchange/5685-writing-fast-matlab-code)

[http://www.mathworks.com/matlabcentral/fileexchange/22943](http://www.mathworks.com/matlabcentral/fileexchange/22943)

[http://blogs.mathworks.com/loren/2012/01/13/best-practices-for-programming-matlab/](http://blogs.mathworks.com/loren/2012/01/13/best-practices-for-programming-matlab/)

[http://www.ee.columbia.edu/~marios/matlab/matlab_tricks.html](http://www.ee.columbia.edu/~marios/matlab/matlab_tricks.html)

[http://www.mathworks.com/help/matlab/matlab_prog/techniques-for-improving-performance.html](http://www.mathworks.com/help/matlab/matlab_prog/techniques-for-improving-performance.html)

#### Code reusability
The basic, or at least most important, principle of this 
is what is called 'abstraction', 
or breaking complicated procedures down into smaller, generic pieces. 
Writing functions is the classic example of this. Where possible, 
functions should be short (50 lines max) and general enough that 
they can be used for many things. More technically, abstraction 
refers to making code more modular, sort of like Henry Ford's 
'interchangeable parts'. Your time series analysis functions should be 
able to take arbitrary types of data, with arbitrary time steps. It 
should be easy to adjust the time window for a rolling mean, or change 
from a boxcar to a gaussian smoothing, or use median and median absolute 
deviation instead of mean and standard deviation, without having to 
rewrite a lot of code. This doesn't mean that you have to write super 
generalized libraries, but if functions are well-designed and abstracted, 
even if you have to write a different one, you can often mimick the 
design of the function, and make few or no changes to the input arguments 
or its outputs (the design of input and output, etc. is often referred to 
as the 'API' or 'application programming interface', especially for 
larger libraries or programs).

A big corollary of this is "DRY" coding (Don't Repeat Yourself), 
so that a function or workflow is only written once. Therefore, 
it always does the same things, so all calculations will be consistent. 
Then, if you need to change the way it is done, it will change for all 
scripts and all variables that use it. You will also write much less 
code this way, making yourself more efficient.

This will also make it much easier to debug code and to have 
others (collaborators, reviewers, students, yourself in one year) 
figure out what the code does and how to use it.


#### Style and readability:
Remember that computer code is to be read by humans 
and only incidentally by computers.

The biggest things in this are to insert spaces in between 
variable names, operators (+,-), etc. Put blank lines in between 
lines of code (where appropriate) and don't put more than 2 blank 
lines in between anything. Most importantly, make function and 
variable names long and descriptive. Matlab programmers are particularly 
bad about this. It's cultural and it's horrible.

[http://www.ee.columbia.edu/~marios/matlab/MatlabStyle1p5.pdf](http://www.ee.columbia.edu/~marios/matlab/MatlabStyle1p5.pdf)

and this one is really good in general, not specifically about matlab 
(and written by economists):

[http://faculty.chicagobooth.edu/matthew.gentzkow/research/ra_manual_coding.pdf](http://faculty.chicagobooth.edu/matthew.gentzkow/research/ra_manual_coding.pdf)

Matlab programmers often make variable or function names look like 
"bsxfun" or "BSXFUN", which means... who the hell knows. I think it stands 
for 'basis function' or 'basics function' but I don't know. Therefore 
if I see it, I'm confused, or if i am trying to look for a function 
that does whatever it does, I can't find it easily. C/C++ 
programmers will write 'basisFunction' in what is called 
'camelCase' by others, and many think this is ugly and 
somewhat unreadable, but is certainly better. The convention 
used by everyone else (except Mathematica programmers, 
where this is not allowed) is 'basis_function' which is nice and readable.

Also, make all your code less than 81 characters wide. Split your lines. 
This makes things much easier when you have several scripts, or an 
editor window, a terminal, and a journal article, all open on the 
same screen.

#### Python!
Probably the best way to accomplish many of these goals is to use 
Python instead of Matlab... It's much easier to write fast code (though 
the language itself is about as fast) because code is more often 
automatically vectorized, the syntax is more clear, and it's much,
 much easier to write functions and to organize them. The users are 
 often more computer literate, so more experienced help is easily 
 available. Plus it's free and open-source, so you can actually see 
 what the code does, and install it on any computer for free. In fact, 
 every modern computer already has it, minus scientific libraries. 
 IPython Notebook is also the best thing in the world for prototyping 
 scientific code and doing any data analysis.  Pandas is incredibly
 useful, as is JobLib Parallel.  Did I mention that it's free?

#### Version control
There are three main reasons to use version control.
USING IT IS REALLY EASY, TOO. Start doing this the absolute next 
time you do any coding. You will definitely not regret it. 
[http://hginit.com/](http://hginit.com/) <-- read this tutorial/
introduction. It's really fast and kind of funny, even if you 
don't end up using Mercurial.

The first is that it saves versions of the code, so you can go 
back at any point and see changes, or revert to a previous, working 
version if you screw something up. The second is that you can easily 
back up and share code at GitHub or BitBucket, in a way that is easier 
to use and much less screwupable than Dropbox, because the entire code 
history is automatically saved as well, and it's not automatically 
synced to your computer, so if you delete it accidentally, it's still 
online.

The third is that you can have several concurrent versions of the 
code and switch back and forth between them, and merge them when 
need be. Also, other people (collaborators, students, anyone...) 
can also 'fork' your code and make their own changes, and if they 
want to add something, they can. And you can keep it all synced. 
I do this between computers because I typically work alone, but I 
share data with the world via GitHub and one day hopefully I will 
collaborate with people.

There are a couple different types of version control, centralized 
version control (SVN is the most common) and distributed version 
control (Git and Mercurial (also called Hg, the chem. symbol for 
mercury) ) are the most common. You want distributed version control.

Git and mercurial both used to be used about equally, but git has 
pulled ahead in recent years, because of 'cooler kids' using it, 
because GitHub (which is awesome) uses it exclusively (vs. BitBucket), 
and because it's a bit more powerful. The first two are basically 
network effects. Mercurial is a bit easier to use off the bat, I 
think, but both are pretty similar in basic usage. Both git and 
mercurial have good GUIs now, too (SourceTree is the best I've used), 
which makes learning a lot easier.

I used to use mercurial but have switched to git, because I like 
github so much, and because more people use it commercially, so I 
realized that if I want a job doing anything with software, or 
want to contribute to open-source projects, I will have to know it. 

GitHub has free public code repos (repositories) but you have to 
pay for private ones. BitBucket isn't as great a website/code 
host, but has unlimited free private code repos for academics.
