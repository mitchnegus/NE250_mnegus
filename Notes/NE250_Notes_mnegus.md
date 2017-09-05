# NE250 – Reactor Theory



## 8/24/2017 


### Nuclear Reactions 

Two types

#### 1. Spontaneous *(decay)*

* $\alpha$: $^A_ZX \rightarrow ^{A-4}_{Z-2}X + ^4_2\alpha$
* $\beta$: $^A_ZX \rightarrow ^A_{Z+1}X + \beta + \bar{\nu}$
* $\gamma$ $X^* \rightarrow X +() \gamma$

##### Decay Equations
$ t \rightarrow N(t) $  
$ t+dt \rightarrow N(t+dt) $

$dN(t) = N(t+dt) - N(t) $  
$dN(t) = -\lambda N(t) dt$ where $\lambda$ is the decay constant.

... working through, with B.C. $N(t=0) = N_0$ ...

$$N(t) = N_0 e^{-\lambda t}$$

**Mean Lifetime:** 

$\frac{dN(t)}{N_0} = \lambda e^{-\lambda t} dt = p_d(t)$ where $p_d(t) dt$ is the probability of decay in time $dt$

$$\bar{t} = \int_0^{\infty} t p(t) dt = \frac{1}{\lambda}$$

**Half Life:**

$T_{1/2}$ is defined as the time s.t. $N(T_{1/2}) = \frac{N_0}{2}$; 
$$T_{1/2} = \frac{ln2}{\lambda}$$

#### 2. Induced *(projectile/target)*

*this will be the emphasis of NE 250*

##### Neutron-Nucleus

* elastic scattering
* inelastic scattering/compound nuclear reaction  
	$$n + ^A_ZX \rightarrow ^{A+1}_ZX^*$$
	(could result in production of a $\gamma$ or $\alpha$, emission of a $n$, or fission)
	
	###### Capture is a subset of absorption!
	Absorption: $(n,\alpha), (n,\gamma), (n,f)$  
	Capture: $(n,\gamma)$
	
###### Cross Sections ($\sigma$)
* A property of the isotope and reaction
* A function of the isotope temperature (vibrational motion) and neutron speed (linear motion)
* Tabulated in XSec libraries *(3 common formats)*
	* ENDF (USA)
	* JEFF (Europe/NEA)
	* JENDL (Japan)

![](/Users/mitch/Documents/Cal/3_2017_Fall/NUCENG250–Nuclear_Reactor_Theory/mnegus/Notes/fig/Lecture01_U235-Xsec.gif)

* Resonances in X-Sec plots due to excited energy levels that can be reached; nuclei only all excitation to these levels, and so only neutrons with this energy amount will be absorbed
* Cross sections measured at 300K (room temp); calculated using
	$$ E = k_BT $$ where $k_B$ is Boltzmann's constant and $T=300 \text{ K} \Rightarrow E = 0.0253 \text{ eV}$
* Higher temperatures cause resonant peak widths to broaden (less time spent near center of vibrational trajectory) $\rightarrow$ **Doppler Broadening**

###### Units
$1 \text{ barn} = 10^{24} \text{ cm}^2$  
$1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$



## 8/25/2017

### Nuclear Reactions (cont.)
#### Fission

Can be spontaneous or induced

$$ n + ^{235}\text{U} \rightarrow X + Y + \bar{\nu} n + E $$

$\bar{\nu}$ is the average number of neutrons produced in a given fission event.

$ E_f \approx 200 \text{ MeV} $ (this is much higher than chemical reactions which are on the order of eV!)

##### Fissile Isotopes

$ E_b > E_{\text{threshold}}$

These neutrons could (almost) be considered as "able to fission from 0 KE neutrons."

Includes $^{235}\text{U}$, $^{233}\text{U}$, $^{239}\text{Pu}$, $^{241}\text{Pu}$

##### Fissionable Isotopes

Fission requires collision with high $E$ neutrons.

For $^{235}\text{U}$ this is empirically given by $$\chi(E) = 0.453e^{-1.036E}\sinh(\sqrt{2.29E})$$

![](/Users/mitch/Documents/Cal/3_2017_Fall/NUCENG250–Nuclear_Reactor_Theory/mnegus/Notes/fig/Lecture02_FissionEDist.png)



Also, note that $\bar{\nu}$ depends on the isotope. Below is a plot of $\bar{\nu}$ for $^{239}\text{Pu}$, $^{233}\text{U}$ and $^{235}\text{U}$:

![](/Users/mitch/Documents/Cal/3_2017_Fall/NUCENG250–Nuclear_Reactor_Theory/mnegus/Notes/fig/Lecture02_nubarUPu.png)

##### Fertile Isotopes

Isotopes which either undergo neutron capture (and subsequent decay) to become fissile isotopes.


#### Energy breakdown of fission outputs

* ~ 180 MeV in the KE of fission products
* ~ 5 MeV in the kinetic energy of neutrons
* ~ 7 MeV in prompt $\gamma$s
* ~ 8 MeV in $\beta^{-}$ decay of fission products
* ~ 7 MeV in delayed $\gamma$s
* ~ 12 MeV in neutrinos

The energy from all outputs can be captured except for neutrinos.


### Criticality

#### Multiplication Factor, $k$

$$ k = \frac{\text{# neutrons generated}}{\text{# neutrons lost}} $$

$\text{# neutrons generated = neutrons fission}$  
$\text{# neutrons lost = # neutrons absorbed + # neutrons leaked}$

$k=1$: the reaction is critical; the chain reaction is controlled (reactor)  
$k<1$: the reactor is subcritcal; boring  
$k>1$: the reaction is supercritical; this is a bomb  

### Derivation of the Neutron Transport Equation

Solving for the multiplication factor requires that we know: 

1. $n$: neutron density $[n/\text{cm}^3]$
2. $N$: atom/nuclide density $[\text{nuclei}/\text{cm}^3]$
3. $\sigma$: microscopic cross section $[\text{cm}^2]$

**Reaction rate:** $ \; R = n N \sigma$

**Macroscopic cross section $[1/\text{cm}]$:** $ \; \Sigma = N \sigma $

**Angular neutron density $[\frac{n}{\text{cm}^3 \cdot \text{sr}}]$:** $\; n (\vec{r}, E, \hat{\Omega}, t)$

$\vec{v} = v \,\hat{\Omega}, \; |\hat{\Omega}| = 1$ (describes a sphere, formed by $\theta$ and $\phi$)

$ dr^3 = dx \; dy \; dz$

$ dE$

$ d\hat{\Omega} = \sin\theta \; d\theta \; d\phi$; $d\hat{\Omega}$ is a scalar, about the original position defined by vector $\hat{\Omega}$.

![](/Users/mitch/Documents/Cal/3_2017_Fall/NUCENG250–Nuclear_Reactor_Theory/mnegus/notes/fig/Lecture02_PhaseSpace.png)

Altogether, $ n (\vec{r}, E, \hat{\Omega}, t) \; d^3r \; dE \; d\hat{\Omega}$, gives the # of neutrons in the small volume about $\vec{r}$ with energy, $E$, and moving in direction $d\hat{\Omega}$ about $\hat{\Omega}$ at time t.

**Angular neutron flux (scalar):** $\phi(\vec{r}, E, \hat{\Omega}, t) = v n (\vec{r}, E, \hat{\Omega}, t)$  
**Angular neturon current (vector):** $\vec{J}(\vec{r}, E, \hat{\Omega}, t) = \hat{\Omega} \phi (\vec{r}, E, \hat{\Omega}, t)$

We can find the number of neutrons in a volume $V$ using
$$ \int_V{ n(\vec{r}, E, \hat{\Omega}, t) \; d^3r }$$

Change with time is then 
$$ \frac{\partial}{\partial t}\left[\int_V{ n(\vec{r}, E, \hat{\Omega}, t) \; d^3r }\right] dE \; d\hat{\Omega} = \text{ # neutrons gained - # neutrons lost}$$

\# neutrons gained: source (fission), in-scattering ($E', \hat{\Omega}' \rightarrow E, \hat{\Omega}$)
\# neutrons lost: absorption, scattering ($E, \hat{\Omega} \rightarrow E', \hat{\Omega}'$)

We also add a streaming term, to quantify neutrons leaking out (and in) to the system.

---

## 9/1/2017

### Derivation of the Neutron Transport Equation (cont.)

The chance of a collision in the system is given by 
$$ \left[ \int_V{ \Sigma_{\text{tot}}(\vec{r},E) v n(\vec{r},E,\hat{\Omega},t) \; d^3r} \right] dE \; d\hat{\Omega} $$

...
---

## 8/31/2017

Library review: [Notes](https://hackmd.io/IYZhBMA4AYCME4C0BWALPATI1tkkbAIxGKEBmhIsAxocuNeMEA==?both#)



