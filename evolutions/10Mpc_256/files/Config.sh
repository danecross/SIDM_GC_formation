#!/bin/bash            # this line only there to enable syntax highlighting in this file

USE_FFTW3
BOX_PERIODIC 

DM_SIDM=1  

FOF
FOF_PRIMARY_LINK_TYPES=1
FOF_GROUP_MIN_SIZE=32

SUBFIND
SUBFIND_SAVE_PARTICLEDATA


# ---------------------------------------- Adaptive Grav. Softening (including Lagrangian conservation terms!)
#ADAPTIVE_GRAVSOFT_FORALL=1+2   # enable adaptive gravitational softening lengths for designated particle types (ADAPTIVE_GRAVSOFT_FORGAS should be disabled). the softening is set to the distance
                                # enclosing a neighbor number set in the parameter file. flag value = bitflag like PM_PLACEHIGHRESREGION, which determines which particle types are adaptive (others use fixed softening). cite Hopkins et al., arXiv:1702.06148

####################################################################################################
# --------------------------------------- On the fly FOF groupfinder
# ----------------- This is originally developed as part of GADGET-3 by V. Springel
# ----------------- Users of any of these modules should cite Springel et al., MNRAS, 2001, 328, 726 for the numerical methods.
####################################################################################################
#SUBFIND_ADDIO_NUMOVERDEN=1         # for M200,R200-type properties, compute values within in this number of different overdensities (default=1=)
#SUBFIND_ADDIO_VELDISP              # add the mass-weighted 1D velocity dispersions to properties computed in parent group[s], within the chosen overdensities
#SUBFIND_ADDIO_BARYONS              # add gas mass, mass-weighted temperature, and x-ray luminosity (assuming ionized primoridal gas), and stellar masses, to properties computed in parent group[s], within the chosen overdensities
## ----------------------------------------------------------------------------------------------------
#SUBFIND_REMOVE_GAS_STRUCTURES      # delete (do not save) any structures which are entirely gas (or have fewer than target number of elements which are non-gas, with the rest in gas)
####################################################################################################

#DEBUG                          # enables core-dumps and FPU exceptions

















