# Applying FastSim JECs on NanoAOD
Using NanoAODs and CMSSW NanoAODTools, produces new NanoAODs that have fastsim JEC applied on AK4 Jets and MET.

JEC corrected MET branchname: MET_T1_pt, MET_T1_phi (2016, 2018) or METFixEE2017_T1_pt, METFixEE2017_T1_phi (2017)
JEC corrected AK4 JET branchname: Jet_pt_nom, Jet_mass_nom

## Step 1. Installation

    source /cvmfs/cms.cern.ch/cmsset_default.sh
    cmsrel CMSSW_10_2_22
    cd CMSSW_10_2_22/src
    cmsenv
    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
    scram b

Reference: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#JME_jetmet_HelperRun2

## Step 2. Modify of 2016 FastSIM JEC name in NanoAODTools

Should modify the 2016 FastSim JEC name to be up to date.


In `CMSSW_10_2_22/src/PhysicsTools/NanoAODTools/python/postprocessing/modules/jme/jetmetHelperRun2.py`,
modify the jecTagsFastSim[2016] to Summer16_FastSimV1_MC.

    jecTagsFastSim = {'2016' : 'Summer16_FastSimV1_MC',
                  '2017' : 'Fall17_FastSimV1_MC',
                  '2018' : 'Autumn18_FastSimV1_MC'}

Reference: https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC

## Step 3. Run CMSSW on NanoAOD to apply FastSim JEC
    ./apply_fastsim_jmeCorrections_to_nanoaod.py -o FOLDER -y YEAR -i NANOAOD_PATH...
