---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV",
  "permalink": "/verify/taulib/docs/book-iv/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV`.",
  "module_name": "TauLib.BookIV",
  "module_slug": "book-iv",
  "book": "BookIV",
  "family": "",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV.lean",
  "sha256": "a03deec660515a3e12dd15a32f112debef56161ff3bfa941e8efe1ef1756ce0a",
  "imports": [
    "TauLib.BookIV.Sectors.SectorParameters",
    "TauLib.BookIV.Sectors.CouplingFormulas",
    "TauLib.BookIV.Sectors.FineStructure",
    "TauLib.BookIV.Sectors.ModeCensus",
    "TauLib.BookIV.Sectors.BoundaryFiltration",
    "TauLib.BookIV.Sectors.SpectralPage",
    "TauLib.BookIV.Physics.QuantityFramework",
    "TauLib.BookIV.Physics.PlanckCharacter",
    "TauLib.BookIV.Physics.DefectFunctional",
    "TauLib.BookIV.Physics.MassEnergy",
    "TauLib.BookIV.Physics.Thermodynamics",
    "TauLib.BookIV.Physics.TickUnits",
    "TauLib.BookIV.Physics.InternalEquations",
    "TauLib.BookIV.Physics.ReadoutFunctor",
    "TauLib.BookIV.Physics.LemniscateCapacity",
    "TauLib.BookIV.Physics.HolonomyCorrection",
    "TauLib.BookIV.Physics.NucleonMassSplitting",
    "TauLib.BookIV.Arena.CoherenceKernel",
    "TauLib.BookIV.Arena.RefinementTower",
    "TauLib.BookIV.Arena.Tau3Arena",
    "TauLib.BookIV.Arena.BoundaryHolonomy",
    "TauLib.BookIV.Arena.FiveSectors",
    "TauLib.BookIV.Arena.ActorsDynamics",
    "TauLib.BookIV.Calibration.SIReference",
    "TauLib.BookIV.Calibration.DimensionlessNearMatch",
    "TauLib.BookIV.Calibration.CalibrationAnchor",
    "TauLib.BookIV.Calibration.DimensionalBridge",
    "TauLib.BookIV.Calibration.CalibrationAnchorExt",
    "TauLib.BookIV.Calibration.DimensionalBridgeExt",
    "TauLib.BookIV.Calibration.ConstantsLedger",
    "TauLib.BookIV.Calibration.SharedOntology",
    "TauLib.BookIV.Calibration.DimensionlessCouplings",
    "TauLib.BookIV.Calibration.DimensionlessCouplings2",
    "TauLib.BookIV.Calibration.DimensionlessAlpha",
    "TauLib.BookIV.Calibration.RunningRegime",
    "TauLib.BookIV.Calibration.ConstantsLedgerExt",
    "TauLib.BookIV.Calibration.EpsteinZeta",
    "TauLib.BookIV.Calibration.MassRatioFormula",
    "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
    "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
    "TauLib.BookIV.QuantumMechanics.HilbertSpace",
    "TauLib.BookIV.QuantumMechanics.Quantization",
    "TauLib.BookIV.QuantumMechanics.AddressObstruction",
    "TauLib.BookIV.QuantumMechanics.Measurement",
    "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
    "TauLib.BookIV.MassDerivation.BreathingModes",
    "TauLib.BookIV.MassDerivation.HolonomyDetail",
    "TauLib.BookIV.MassDerivation.ElectronMass",
    "TauLib.BookIV.Electroweak.PhotonMode",
    "TauLib.BookIV.Electroweak.GaugeInvariance",
    "TauLib.BookIV.Electroweak.GaugeInvariance2",
    "TauLib.BookIV.Electroweak.TauMaxwell",
    "TauLib.BookIV.Electroweak.AlphaDerivation",
    "TauLib.BookIV.Electroweak.WeakChirality",
    "TauLib.BookIV.Electroweak.WeakChirality2",
    "TauLib.BookIV.Electroweak.WeakHolonomy",
    "TauLib.BookIV.Electroweak.WeakHolonomy2",
    "TauLib.BookIV.Electroweak.NeutrinoMode",
    "TauLib.BookIV.Electroweak.MajoranaStructure",
    "TauLib.BookIV.Electroweak.EWMixing",
    "TauLib.BookIV.Electroweak.TauHiggs",
    "TauLib.BookIV.Electroweak.TauHiggs2",
    "TauLib.BookIV.Electroweak.EWSynthesis",
    "TauLib.BookIV.Electroweak.EWProjection",
    "TauLib.BookIV.Electroweak.WeinbergNLO",
    "TauLib.BookIV.Strong.StrongVacuum",
    "TauLib.BookIV.Strong.ColorHolonomy",
    "TauLib.BookIV.Strong.Confinement",
    "TauLib.BookIV.Strong.GapMetaTheorem",
    "TauLib.BookIV.Strong.YangMillsGap",
    "TauLib.BookIV.Strong.StrongCoupling",
    "TauLib.BookIV.Strong.QuarksGluons",
    "TauLib.BookIV.Strong.VacuumCatastrophe",
    "TauLib.BookIV.Particles.SectorAtlas",
    "TauLib.BookIV.Particles.ThreeGenerations",
    "TauLib.BookIV.Particles.BetaDecay",
    "TauLib.BookIV.Particles.HadronsNuclei",
    "TauLib.BookIV.Particles.PeriodicTable",
    "TauLib.BookIV.Particles.SpectrumComplete",
    "TauLib.BookIV.Particles.StrongCP",
    "TauLib.BookIV.ManyBody.DefectFunctionalExt",
    "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
    "TauLib.BookIV.ManyBody.FluidRegimes",
    "TauLib.BookIV.ManyBody.CondensedMatter",
    "TauLib.BookIV.ManyBody.Magnetism",
    "TauLib.BookIV.ManyBody.NFLBoundary",
    "TauLib.BookIV.Coda.LawsAsStructure",
    "TauLib.BookIV.Coda.CompleteLedger",
    "TauLib.BookIV.Coda.SelfDescribing"
  ],
  "imported_by": [
    "TauLib"
  ],
  "registry_ids": [],
  "declaration_counts": {},
  "declarations": [],
  "right_rail": {
    "related": [
      {
        "title": "TauLib Overview",
        "url": "/verify/taulib/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV.lean",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Module",
      "source": "Corpus projection",
      "commit": "cb5e8301"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Module"
}
---

## Corpus TauLib Projection

This page is generated directly from the pinned TauLib Lean source snapshot in `corpus/taulib-sources/project`. It is a Corpus-native module view designed for cross-linking Registry, Construction Spine, Results, and Verify surfaces.

## Source Provenance

- Source repository: `Panta-Rhei-Research/taulib`
- Source commit: [`cb5e8301`](https://github.com/Panta-Rhei-Research/taulib/commit/cb5e83015b54dd72eba560953fe2461820078757)
- Source path: [`TauLib/BookIV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV.lean`
- SHA-256: `a03deec660515a3e12dd15a32f112debef56161ff3bfa941e8efe1ef1756ce0a`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.SectorParameters`
- `TauLib.BookIV.Sectors.CouplingFormulas`
- `TauLib.BookIV.Sectors.FineStructure`
- `TauLib.BookIV.Sectors.ModeCensus`
- `TauLib.BookIV.Sectors.BoundaryFiltration`
- `TauLib.BookIV.Sectors.SpectralPage`
- `TauLib.BookIV.Physics.QuantityFramework`
- `TauLib.BookIV.Physics.PlanckCharacter`
- `TauLib.BookIV.Physics.DefectFunctional`
- `TauLib.BookIV.Physics.MassEnergy`
- `TauLib.BookIV.Physics.Thermodynamics`
- `TauLib.BookIV.Physics.TickUnits`
- `TauLib.BookIV.Physics.InternalEquations`
- `TauLib.BookIV.Physics.ReadoutFunctor`
- `TauLib.BookIV.Physics.LemniscateCapacity`
- `TauLib.BookIV.Physics.HolonomyCorrection`
- `TauLib.BookIV.Physics.NucleonMassSplitting`
- `TauLib.BookIV.Arena.CoherenceKernel`
- `TauLib.BookIV.Arena.RefinementTower`
- `TauLib.BookIV.Arena.Tau3Arena`
- `TauLib.BookIV.Arena.BoundaryHolonomy`
- `TauLib.BookIV.Arena.FiveSectors`
- `TauLib.BookIV.Arena.ActorsDynamics`
- `TauLib.BookIV.Calibration.SIReference`
- `TauLib.BookIV.Calibration.DimensionlessNearMatch`
- `TauLib.BookIV.Calibration.CalibrationAnchor`
- `TauLib.BookIV.Calibration.DimensionalBridge`
- `TauLib.BookIV.Calibration.CalibrationAnchorExt`
- `TauLib.BookIV.Calibration.DimensionalBridgeExt`
- `TauLib.BookIV.Calibration.ConstantsLedger`
- `TauLib.BookIV.Calibration.SharedOntology`
- `TauLib.BookIV.Calibration.DimensionlessCouplings`
- `TauLib.BookIV.Calibration.DimensionlessCouplings2`
- `TauLib.BookIV.Calibration.DimensionlessAlpha`
- `TauLib.BookIV.Calibration.RunningRegime`
- `TauLib.BookIV.Calibration.ConstantsLedgerExt`
- `TauLib.BookIV.Calibration.EpsteinZeta`
- `TauLib.BookIV.Calibration.MassRatioFormula`
- `TauLib.BookIV.QuantumMechanics.CRAddressSpace`
- `TauLib.BookIV.QuantumMechanics.QuantumCharacters`
- `TauLib.BookIV.QuantumMechanics.HilbertSpace`
- `TauLib.BookIV.QuantumMechanics.Quantization`
- `TauLib.BookIV.QuantumMechanics.AddressObstruction`
- `TauLib.BookIV.QuantumMechanics.Measurement`
- `TauLib.BookIV.QuantumMechanics.EnergyEntropy`
- `TauLib.BookIV.MassDerivation.BreathingModes`
- `TauLib.BookIV.MassDerivation.HolonomyDetail`
- `TauLib.BookIV.MassDerivation.ElectronMass`
- `TauLib.BookIV.Electroweak.PhotonMode`
- `TauLib.BookIV.Electroweak.GaugeInvariance`
- `TauLib.BookIV.Electroweak.GaugeInvariance2`
- `TauLib.BookIV.Electroweak.TauMaxwell`
- `TauLib.BookIV.Electroweak.AlphaDerivation`
- `TauLib.BookIV.Electroweak.WeakChirality`
- `TauLib.BookIV.Electroweak.WeakChirality2`
- `TauLib.BookIV.Electroweak.WeakHolonomy`
- `TauLib.BookIV.Electroweak.WeakHolonomy2`
- `TauLib.BookIV.Electroweak.NeutrinoMode`
- `TauLib.BookIV.Electroweak.MajoranaStructure`
- `TauLib.BookIV.Electroweak.EWMixing`
- `TauLib.BookIV.Electroweak.TauHiggs`
- `TauLib.BookIV.Electroweak.TauHiggs2`
- `TauLib.BookIV.Electroweak.EWSynthesis`
- `TauLib.BookIV.Electroweak.EWProjection`
- `TauLib.BookIV.Electroweak.WeinbergNLO`
- `TauLib.BookIV.Strong.StrongVacuum`
- `TauLib.BookIV.Strong.ColorHolonomy`
- `TauLib.BookIV.Strong.Confinement`
- `TauLib.BookIV.Strong.GapMetaTheorem`
- `TauLib.BookIV.Strong.YangMillsGap`
- `TauLib.BookIV.Strong.StrongCoupling`
- `TauLib.BookIV.Strong.QuarksGluons`
- `TauLib.BookIV.Strong.VacuumCatastrophe`
- `TauLib.BookIV.Particles.SectorAtlas`
- `TauLib.BookIV.Particles.ThreeGenerations`
- `TauLib.BookIV.Particles.BetaDecay`
- `TauLib.BookIV.Particles.HadronsNuclei`
- `TauLib.BookIV.Particles.PeriodicTable`
- `TauLib.BookIV.Particles.SpectrumComplete`
- `TauLib.BookIV.Particles.StrongCP`
- `TauLib.BookIV.ManyBody.DefectFunctionalExt`
- `TauLib.BookIV.ManyBody.DefectFunctionalExt2`
- `TauLib.BookIV.ManyBody.FluidRegimes`
- `TauLib.BookIV.ManyBody.CondensedMatter`
- `TauLib.BookIV.ManyBody.Magnetism`
- `TauLib.BookIV.ManyBody.NFLBoundary`
- `TauLib.BookIV.Coda.LawsAsStructure`
- `TauLib.BookIV.Coda.CompleteLedger`
- `TauLib.BookIV.Coda.SelfDescribing`

## Imported By

- `TauLib`

## Declaration Counts

- No declarations detected.

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| — | — | — | — | — |
