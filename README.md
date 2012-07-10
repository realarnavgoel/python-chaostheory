python-chaostheory
==============
A python module developed to display an application of natural language processing via chaos theory

Usage
=====
<pre>
  <code>
    import chaostheory
    chaostheory.pychaos("century21st.htm")
  </code>
</pre>
License
======
<a href = "http://www.gnu.org/copyleft/gpl.html">GNU General Public License 3.0</a>

(Basic GPL used by all)

Concept of the Module
====================

Chaos Theory deals with understanding & prediction of calamities- natural and man-made that have occured in the past
and have possibility of occuring in the future. The name of module <code> "chaostheory" </code> can be imported from the current directory
while scripting in python . The function linked to the module is <code>"pychaos()"</code> which take a <code>"filename"</code>
as an argument.The filename to be provided is "century21st.htm" that is included in the repository. It is static 
wikipedia htm page containing the information of all the events that have occured in the 21st century. 

Since this is static htm page, the output is fixed and defined according the data written in html script. This module is
meant to provide you the output of the years in which various calamities as listed by tokens such as ['war','killed',
'virus','disaster','riot','destroy','damage','devastate','death','earthquake','tsunami','deadly','catastrophe',
'Earthquake','War','Tsunami','Hurricane','Cyclone'] took place. 

Authors Comments
===============

My effort is a step towards the field of Natural Language Processing where huge data in real time is imported, tokenized
and processed to provide relevant information according to our needs.
You can use on both Python 2.x or Python 3.x

For any bugs and issues in implementation , please to write to me at arnavgoel2016[at]gmail[dot]com.
