## Clebsh-Gordan Coefficient finder ##
This tool is designed to make finding Clebsh-Gordan coefficients easier.
This is done using SQLite to make a database (see database.py) and PyQT5 to create a UI (see interface.py).

I use Clebsh-Gordan coefficients in particle physics to calculate the bound state of 2 angular momentum states. To do this I use the equation below in which the Clebsh-Gordan coefficent is seen as C(j<sub>1</sub>, j<sub>2</sub>)<sup>(j)</sup><sub>m<sub>1</sub>,m<sub>2</sub></sub>:

<image src = "assetts/equation.png">

Currently the program only includes the 1/2 x 1/2 coefficients as I have not added the rest to the database yet.

The application is seen below:

<image src = "assetts\Screenshot.png">

For more information on Clebsh-Gordan coefficients see this link: https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients.

In this code I have created the database using data from the particle data group which can be found here: https://pdg.lbl.gov/2002/clebrpp.pdf.

