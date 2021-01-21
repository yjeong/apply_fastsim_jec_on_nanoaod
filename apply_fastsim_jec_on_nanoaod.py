#!/usr/bin/env python
# Using NanoAODs and CMSSW NanoAODTools, produces new NanoAODs that have fastsim JEC applied.
# JEC corrected MET branchname: MET_T1_pt, MET_T1_phi (2016, 2018) or METFixEE2017_T1_pt, METFixEE2017_T1_phi (2017)
# JEC corrected JET branchname: Jet_pt_nom, Jet_mass_nom
# Example: python apply_fastsim_jmeCorrections_to_nanoaod.py -o FOLDER -y YEAR -i NANOAOD_PATH...
import os, sys
import argparse
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

parser = argparse.ArgumentParser()
parser.add_argument('-o','--output_directory', required=True)
parser.add_argument('-y','--year', required=True, default="2016")
parser.add_argument('-i','--input_files', required=True, nargs='+')
parser.add_argument('-c','--cut_string', default=None)
args = parser.parse_args()

metBranchName = "MET" if args.year != "2017" else "METFixEE2017"

jmeCorrections = createJMECorrector(isMC=True, dataYear=args.year, runPeriod="A", jesUncert="Total", jetType="AK4PFchs", noGroom=False, metBranchName=metBranchName, applySmearing=True, isFastSim=True)
p=PostProcessor(outputDir=args.output_directory,inputFiles=args.input_files,cut=args.cut_string,modules=[jmeCorrections()],provenance=True, postfix="")
p.run()
