import FWCore.ParameterSet.Config as cms

#from RecoJets.JetProducers.kt4PFJets_cfi import *
#kt6PFJets = kt4PFJets.clone(rParam = 0.6, doAreaFastjet = cms.bool(True), src = cms.InputTag("particleFlow"), doPUOffsetCorr = cms.bool(False), doRhoFastjet = cms.bool(True))

#from RecoJets.JetProducers.kt4PFJets_cfi import *
#ak5PFJetsNew = kt4PFJets.clone( rParam = 0.6, doRhoFastjet = True, doAreaFastjet = cms.bool(True) )

simpleNtupleEoverP = cms.EDAnalyzer(
    "SimpleNtupleEoverP",
    MCPileupTag         = cms.InputTag("addPileupInfo"),
    PVTag               = cms.InputTag("offlinePrimaryVerticesWithBS"),
    recHitCollection_EB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollection_EE = cms.InputTag("reducedEcalRecHitsEE"),
    SRFlagCollection_EB = cms.InputTag("ecalDigis"),
    SRFlagCollection_EE = cms.InputTag("ecalDigis"),
    digiCollection_EB   = cms.InputTag("ecalDigis","ebDigis"),
    digiCollection_EE   = cms.InputTag("ecalDigis","eeDigis"),
    theBeamSpotTag      = cms.InputTag("offlineBeamSpot"),
    EleTag              = cms.InputTag("gedGsfElectrons"),
    PFMetTag            = cms.InputTag("pfMet"),
    MCtruthTag          = cms.InputTag("genParticles"),
    rhoTag              = cms.InputTag("kt6PFJets","rho"),
    conversionsInputTag = cms.InputTag("allConversions"),
    jsonFileName        = cms.string("dummy.txt"),
    dataRun             = cms.string("noCorrection"),
    jsonFlag            = cms.untracked.bool(False),
    verbosity           = cms.untracked.bool(False),
    doWZSelection       = cms.untracked.bool(True),
    applyCorrections    = cms.untracked.bool(False),
    saveMCPU            = cms.untracked.bool(False),
    saveMCInfo          = cms.untracked.bool(False),
    dataFlag            = cms.untracked.bool(False),
    saveRecHitMatrix    = cms.untracked.bool(False),
    saveFbrem           = cms.untracked.bool(False) # set False if running on AOD
    )
