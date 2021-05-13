#./run_jer.sh [mass]
mkdir -p log/
for year in {16,17,18}
	do echo "${year}..."
		mkdir -p output/20${year}/$1/

		python apply_fastsim_jec_on_nanoaod.py -o output/20${year}/$1/ -y 20${year} -i /xrootd/store/mc/RunII*${year}NanoAODv7/SMS-T1tbs_RPV_mGluino$1_Tune*_13TeV-madgraphMLM-pythia8/NANOAODSIM/*/*/* > log/20${year}_$1GeV_log.txt &
done
