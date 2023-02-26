# Statistics with R Programming. #

Mostly students use in-built codes.

## HOW TO INSTALL AND RUN R: ##
### WITHOUT INSTALLATION/ANDROID/IOS: ###
<ol>
	<li> https://rdrr.io/snippets/ (Official documentation + compiler)</li>
	<li> https://code.sololearn.com/r</li>
	<li> Jupyter with R: https://mybinder.org/v2/gh/binder-examples/r/HEAD?filepath=index.ipynb</li>
</ol>

### DESKTOP (WINDOWS/LINUX) ###
<ul>
	<li> Download and install R
		<ul>
			<li> Windows: https://cran.r-project.org/bin/windows/base/ </li>
			<li> Linux: Open your Package Manager and install r-base </li>
		</ul>
	</li>
	<li> Download and install R-Studio (Windows/Linux)
		<ul>
			<li> Link: https://www.rstudio.com/products/rstudio/download/#download </li>
			<li> Double click to run installer. </li>
		</ul>
	</li>
</ul>

### USING JUPYTER ###
<ul>
	<li> Open R Console
		<ul>
			<li><code>install.packages("IRkernel")</code></li>
			<li> <code>IRkernel::installspec()</code></li>
		</ul>
	</li>
	<li> After  installing successfully, run “jupyter notebook” and under new, pick R as Kernel. </li>
</ul>


## Running Theme ##
We usually make them pick a particular dataset, preferrably relevant to them and make them draw conclusions, so that they see their learning in action and also, train themselves to chase open-ended questions. Some qualities of the dataset should be:
1. At least three columns in the table, of which one is nominal, two are numeric. They can use nominal data to filter and derive observations.
2. Serve the data in a CSV file, or even better, make students generate that CSV file.
3. Data should ideally contain unrealistic number of points: a minimum of 30, so that manual calculation is hard, but not impossible.
4. Preferably choose a data which is best represented by different central tendencies.

Some sample data that can be used are:
1. VARK results of the entire class, with extra tag of gender.
2. Marks in the previous semester, anonymised.

