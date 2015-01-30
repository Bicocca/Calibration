import FWCore.ParameterSet.Config as cms

from Calibration.EcalCalibNtuple.simpleNtupleEoverPsingleParticle_cff import *
from Calibration.EcalCalibNtuple.recoTags_cff import *

process = cms.Process("SimpleNtupleEoverPsingleParticle")

from RecoJets.Configuration.RecoPFJets_cff import *
process.kt6PFJetsForRhoCorrection = kt6PFJets.clone(
    doRhoFastjet = True,
    Rho_EtaMax = 2.5
    )

# flags
#GlobalTag = "START53_V14A::All"
#GlobalTag = "START53_V7N::All"
GlobalTag = "START70_V7::All"     # per 700
runOverSandbox   = False
runOverAlcaReco  = False
runOverData      = False
saveRecHitMatrix = False

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
process.MessageLogger.cerr.threshold = cms.untracked.string("DEBUG")
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))

# simpleNtuple
makeSimpleNtuple(process,GlobalTag=GlobalTag,runOverSandbox=runOverSandbox,runOverAlcaReco=runOverAlcaReco,runOverData=runOverData)

#makeRecoTags(process)
#makeSqliteTags(process)

# path
if not saveRecHitMatrix:
    process.simpleNtuple_step = cms.Path(
        process.kt6PFJetsForRhoCorrection *
        process.simpleNtupleEoverPsingleParticle
        )

if saveRecHitMatrix:
    process.simpleNtuple_step = cms.Path(
        process.ecalDigis *
        process.ecalPreshowerDigis *
        process.hcalDigis *
        process.calolocalreco *
        process.kt6PFJetsForRhoCorrection *
        process.simpleNtupleEoverP_singleParticle
        )

    process.simpleNtupleEoverPsingleParticle.saveRecHitMatrix = cms.untracked.bool(True)
    #process.simpleNtupleEoverPsingleParticle.recHitCollection_EB = cms.InputTag("ecalRecHit","EcalRecHitsEB")
    #process.simpleNtupleEoverPsingleParticle.recHitCollection_EE = cms.InputTag("ecalRecHit","EcalRecHitsEE")


process.simpleNtupleEoverPsingleParticle.particleIsEle = cms.untracked.bool(False)

# source
process.source.fileNames = cms.untracked.vstring(
#    '/store/caf/user/amartell/Analysis/Hgg_fnuf/RECO/RERECO_EleFNUF/SingleElectronPt60_RAWRECO_FNUFmodified_1.root'
#'/store/caf/user/amartell/Analysis/Hgg_fnuf/RECO/RERECO_PhoFNUF/SinglePhotonPt60_RAWRECO_FNUFmodified_1.root'
 
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_1.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_10.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_2.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_3.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_4.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_5.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_6.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_7.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_8.root',
'/store/caf/user/amartell/TimingECAL/DIGI_RECO_noPU/SingleGamma_DIGIRECO_noPU_9.root'


   )

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(-1)
)

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("simpleNtuple_Pho_NoPU.root")
    )

process.schedule = cms.Schedule(
    process.simpleNtuple_step
    )
