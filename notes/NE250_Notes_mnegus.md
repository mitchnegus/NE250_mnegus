# NE250 – Reactor Theory
---


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

---


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
1. $N$: atom/nuclide density $[\text{nuclei}/\text{cm}^3]$
1. $\sigma$: microscopic cross section $[\text{cm}^2]$

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

The chance of fission in system... (See paper notes...)

---



## 9/7/2017

### The Transport Equation

$$ \frac{1}{v} \frac{\partial\psi}{\partial t} + \hat{\Omega} \cdot \nabla\psi + \Sigma_t\psi = \int_{4\pi}{d\hat{\psi}'\int_0^{\infty}{dE' \Sigma_s(E',\hat{\Omega}'\rightarrow E,\hat{\Omega})\psi(E',\hat{\Omega}')}}$$ + $$\frac{\chi(E)}{4\pi}\int_0^{\infty}{dE'\nu(E')\Sigma_f(E')} \int_{4\pi}{d\hat{\Omega}'\phi(\vec{r},E',\hat{\Omega}',t) + s(\vec{r},E,\hat{\Omega},t)}$$

**Initial condition:**  
$\psi(\vec{r},E,\hat{\Omega},0) = \psi_0(\vec{r},E,\hat{\Omega})$

**Interface condition:**  
angular flux must be continuous at all points


##### Other conditions 
**Fixed condition:** incoming flux is specified  
	$\psi(\vec{r}_s,E,\hat{\Omega},t) = \psi_{\text{in}}(\vec{r},E,\hat{\Omega},t)$

Vacuum or black if $\psi_\text{in}(\vec{r},E,\hat{\Omega},t)$

**Reflective conditions:** mirror symmetry at some surface  
	$\psi(\hat{\Omega}_{\text{in}}) = \psi(\hat{\Omega}_{\text{out}},t)$

**Periodic conditions:**  
$\psi(\vec{r}_s) = \psi(\vec{r}_s + \vec{p})$

**Finiteness conditions:** (can't have infinite flux)   
$0 \leq \psi(\vec{r},E,\hat{\Omega},t) < \infty$

**Source condition:** localized (pt.) sources introduce mathemetaical singularities
$S(\vec{r},E,\hat{\Omega},t) = \lim_{\vec{r}\rightarrow\vec{r_0}}\int{dS \; \hat{e} \cdot \hat{\Omega}}$


### Approximations to the Transport Equation

#### One-speed Transport Equation

Assume all particles are the same speed

$\vec{v} = v_0 \cdot \hat{\Omega}$

The equation becomes
$$ \frac{1}{v} \frac{\partial \psi(\vec{r},\hat{\Omega},t)}{\partial t} + \hat{\Omega} \nabla \psi (\vec{r},\hat{\Omega},t) + \Sigma_t(r)\psi (\vec{r},\hat{\Omega},t) = \int_{4\pi}{d\hat{\Omega}' \Sigma_s(\hat{\Omega}'\rightarrow\hat{\Omega}) \psi(\vec{r},\hat{\Omega}',t) + \frac{\nu\Sigma_f}{4\pi}\int_{4\pi}d\hat{\Omega}'{\psi(\vec{r},\hat{\Omega}',t) + S(\vec{r},\hat{\Omega},t)}}$$

#### One-dimensional

$\vec{r} = (x,y,z)$  
$d\hat{\Omega} = sin\theta \; d\theta \; d\varphi = d\mu \; d\varphi$, where $\mu = cos\theta$

$$ \frac{1}{v} \frac{\partial \psi(x,\hat{\Omega},t)}{\partial t} + \Omega_x \frac{\partial}{\partial x} \psi (x,\hat{\Omega},t) + \Sigma_t(x)\psi (x,\hat{\Omega},t) = \int_{4\pi}{d\hat{\Omega}' \Sigma_s(\hat{\Omega}'\rightarrow\hat{\Omega}) \psi(x,\hat{\Omega}',t) + \frac{v\Sigma_f}{4\pi}\int_{4\pi}d\hat{\Omega}'{\psi(x,\hat{\Omega}',t) + S(x,\hat{\Omega},t)}}$$



### The Diffusion Equation

Usually the scalar flux is all that is needed to get a fairly accurate picture of our system. Reaction rates usually only depend on the neutron flux, not the direction of neutron motion.

**Assume** that the angular flux depends only weakly on direction.

*Recall:*  
$\phi(\vec{r},t) = \int_{4\pi}{d\hat{\Omega} \psi(\vec{r},\hat{\Omega},t)}$
$J(\vec{r},t) = \int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \;\psi(\vec{r},\hat{\Omega},t)}$

Integrate transport equation over all angles

1. **Time:** No approximations in time
$$ \frac{1}{v}\frac{\partial}{\partial t}\int_{4\pi}{d\hat{\Omega} \; \psi(\vec{r},\hat{\Omega},t)} = \frac{1}{v}\frac{\partial}{\partial t} \phi(\vec{r},t) $$

1. **Absorption:** No approximations in absorption
$$\Sigma_t \int_{4\pi}{d\hat{\Omega} \; \psi(\vec{r},\hat{\Omega},t)} = \Sigma_t \; \phi(\vec{r},t)$$

1. **Fission:** No approximations in fission
$$ \int_{4\pi}{d\hat{\Omega}} = \int_0^{\pi}{\sin\theta \; d\theta} \int_0^{2\pi}{d\varphi} = 4\pi$$
$$\int_{4\pi}{d\hat{\Omega} \frac{\nu \Sigma_f}{4\pi}\int_{4\pi}{d\hat{\Omega}'\psi(\vec{r},\hat{\Omega},t)}} = \nu \Sigma_f \phi(\vec{r},t)$$

1. **Source:** No approximations in source 
$$\int_{4\pi}{d\hat{\Omega} \; s(\vec{r},\hat{\Omega},t)} \equiv S(\vec{r},t)$$

1. **Scattering:** For scattering, interchange the order of integration
$$ \int_{4\pi}{d\hat{\Omega} \int_{4\pi}{d\hat{\Omega}' \Sigma_s(\hat{\Omega}'\rightarrow \hat{\Omega}) \; \psi}(\vec{r},\hat{\Omega}',t}) = \int_{4\pi}{d\hat{\Omega}' \int_{4\pi}{d\hat{\Omega} \Sigma_s(\hat{\Omega}'\rightarrow\hat{\Omega}) \; \psi}(\vec{r},\hat{\Omega}',t)}$$

	Now we assume that scattering is azimuthally symmetric (scattering depends only on cosine). The particle is as likely to scatter at angle $\theta$ in any direction off $ \hat{\Omega}$.
$$\int_{4\pi}{d\hat{\Omega} \;\Sigma_s(\hat{\Omega}'\cdot\hat{\Omega})} = 2\pi \int_{-1}^1{d\mu \; \Sigma_s(\mu)} = \Sigma_s$$
	Then, if we substitute this in above
$$\Sigma_s\int_{4\pi}{d\hat{\Omega} \; \psi(\vec{r},\hat{\Omega}',t)} =  \Sigma_s \phi(\vec{r},t)$$

1. **Streaming:** To adjust streaming, we first manipulate the order
$$ \int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \cdot \nabla \; \psi(\vec{r},\hat{\Omega},t)} = \nabla \cdot \int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \; \psi(\vec{r},\hat{\Omega},t)} = \nabla \cdot \vec{J}(\vec{r},t)$$

#### Neutron Continuity Equation (NCE)
Put all the above integrations together to get the "Zeroth Angular moment"; notice that we have three equations (each $\vec{r}$ has $x,y,z$ components) and 4 unknown quantities.

$$ \frac{1}{v} \frac{\partial \phi(\vec{r},t)}{\partial t} + \nabla \hat{J}(\vec{r},t) + \Sigma_t \phi(\vec{r},t) = \Sigma_s \phi(\vec{r},t) + \nu \Sigma_f \phi(\vec{r},t) + S(\vec{r},t) $$

#### First angular moment 
Multiply the TE by $\hat{\Omega}$ and integrate.  We will drop the fission term (technically we will assume it is part of the source), though the procedure is nearly the same when it is included.

Note:  
$\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega}} = 0$  
$\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \; \hat{\Omega}} = \frac{4\pi}{3}\bar{\bar{I}} $ 

$\bar{\bar{I}}$ is the identity tensor:  
	$$\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega}_i \; \hat{\Omega}}_j = 
	\begin{cases}
	0, & i \neq j  \\
	\frac{4\pi}{3},&  i = j
	\end{cases}$$

$\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \; \hat{\Omega}} = 0 $ 


When multiplied out, we have

$$ \int_{4\pi}{d\hat{\Omega}} \; \text{[TE]} $$

1. **Time:**
1. **Absorption:**
1. **Source (fission now absent):**
1. **Scattering:** Expand scattering cross section in Legendre Polynomials (a sequence of orthogonal polynomials)

	$$P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} \left[ (x^2 - 1)^n \right]$$

	Expand $\Sigma_s(\hat{\Omega}' \cdot \hat{\Omega})$ in Legendre polynomials

	$$ \Sigma_s(\hat{\Omega}' \cdot \hat{\Omega}) = \sum_0^{\infty}{\frac{2\ell + 1}{4\pi}\Sigma_{s\ell}P_{\ell}(\hat{\Omega}')P_{\ell}(\hat{\Omega})} $$

	* $\ell = 0$ is isotropic  
$P_0(\hat{\Omega}) = 1$  
$\Sigma_s(\hat{\Omega}',\hat{\Omega}) \approx \frac{1}{4\pi}\Sigma_{s0}$

	* $\ell = 1$ is linearly anisotropic  
$P_1(\hat{\Omega}) = \hat{\Omega})$  
$\Sigma_s(\hat{\Omega}',\hat{\Omega}) \approx \frac{1}{4\pi}(\Sigma_{s0} + 3 \hat{\Omega}' \cdot \hat{\Omega}\Sigma_{s1})$

	Assume scattering is at most linearly anisotropic (if its not, there's some "weird" stuff going on")

	$$\frac{1}{4\pi}\int_{4\pi}{d\hat{\Omega} \hat{\Omega}  \int_{4\pi}{d\hat{\Omega}(\Sigma_{s0} + 3 \hat{\Omega}' \cdot \hat{\Omega}\Sigma_{s1}) \; \psi(\vec{r},\hat{\Omega},t)}} = \frac{1}{4\pi}\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega}}\int_{4\pi}{d\hat{\Omega}'\Sigma_{s} \; \psi(\vec{r},\hat{\Omega}',t)} + \frac{1}{4\pi}\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega}\hat{\Omega}}\int_{4\pi}{d\hat{\Omega}' \; \hat{\Omega}' 3 \Sigma_{s1} \; \psi(\vec{r},\hat{\Omega}',t)}$$
	
	Using the defined identities, we find 
	
	$$\frac{1}{4\pi}\int_{4\pi}{d\hat{\Omega} \hat{\Omega}  \int_{4\pi}{d\hat{\Omega}(\Sigma_{s0} + 3 \hat{\Omega}' \cdot \hat{\Omega}\Sigma_{s1}) \; \psi(\vec{r},\hat{\Omega},t)}} = \Sigma_{s1} \; J(\vec{r},t)$$

1. **Streaming:**
	$$\int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \; \hat{\Omega} \cdot \nabla \psi(\vec{r},\hat{\Omega},t)} = \nabla \cdot \int_{4\pi}{d\hat{\Omega} \; \hat{\Omega} \;\hat{\Omega} \; \psi(\vec{r},\hat{\Omega},t)} $$

Putting each of these 5 components back together the **current continuity equation** is
$$\frac{1}{v}{\partial J}{\partial t} + \nabla \cdot \int_{4\pi}{d\hat{\Omega} \;\hat{\Omega}\hat{\Omega} \; \psi(\vec{r},\hat{\Omega},t)} + \Sigma_t \vec{J}(\vec{r},t) = \Sigma_{s1}\vec{J}(\vec{r},t) + S_1(\vec{r},t)$$

Now we have 2 moment equations (zeroth and first) so a total of 4 equations (neutron continuity and 3 tensor equations). There are now 10 unknowns–$\phi$ (1), $\vec{J}$ (3), and the new tensor term (6).


...
---

## 8/31/2017

Library review: [Notes](https://hackmd.io/IYZhBMA4AYCME4C0BWALPATI1tkkbAIxGKEBmhIsAxocuNeMEA==?both#)













