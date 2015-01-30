import FWCore.ParameterSet.Config as cms

def makeSimpleNtuple(process,GlobalTag,runOverSandbox,runOverAlcaReco,runOverData):
    
    # Source
    process.source = cms.Source(
        "PoolSource",
        fileNames = cms.untracked.vstring()
        )
    
    
    # Out
    process.out = cms.OutputModule(
        "PoolOutputModule",
        fileName = cms.untracked.string('out.root'),
        outputCommands = cms.untracked.vstring()
        )
    
    # Standard Sequences
    process.load('Configuration.StandardSequences.Services_cff')
    process.load('Configuration.StandardSequences.GeometryDB_cff')
    process.load("Configuration.StandardSequences.MagneticField_cff")
    process.load('Configuration.StandardSequences.RawToDigi_Data_cff')    
    process.load('Configuration.StandardSequences.L1Reco_cff')
    process.load('Configuration.StandardSequences.Reconstruction_cff')
    process.load('Configuration.StandardSequences.EndOfProcess_cff')
    
    # GlobalTag
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = GlobalTag
    
    
    #--------------------------
    # Ntuple
    #--------------------------
    
    process.load("Calibration/EcalCalibNtuple/simpleNtupleEoverPsingleParticle_cfi")

    if runOverAlcaReco:
        process.simpleNtupleEoverPsingleParticle.recHitCollection_EB =  cms.InputTag("alCaIsolatedElectrons","alcaBarrelHits")
        process.simpleNtupleEoverPsingleParticle.recHitCollection_EE =  cms.InputTag("alCaIsolatedElectrons","alcaEndcapHits")
        process.simpleNtupleEoverPsingleParticle.rhoTag              =  cms.InputTag("kt6PFJetsForRhoCorrection","rho")
    
    if runOverSandbox:                
        process.simpleNtupleEoverPsingleParticle.recHitCollection_EB =  cms.InputTag("alCaIsolatedElectrons","alCaRecHitsEB","ALCARERECO")
        process.simpleNtupleEoverPsingleParticle.recHitCollection_EE =  cms.InputTag("alCaIsolatedElectrons","alCaRecHitsEE","ALCARERECO")
        process.simpleNtupleEoverPsingleParticle.EleTag              =  cms.InputTag("electronRecalibSCAssociator","","ALCARERECO")
        process.simpleNtupleEoverPsingleParticle.rhoTag              =  cms.InputTag("kt6PFJetsForRhoCorrection","rho")
    
    if not runOverData:
        process.simpleNtupleEoverPsingleParticle.dataFlag            = cms.untracked.bool(False)
        process.simpleNtupleEoverPsingleParticle.saveMCPU            = cms.untracked.bool(True)
        process.simpleNtupleEoverPsingleParticle.saveMCInfo          = cms.untracked.bool(True)
