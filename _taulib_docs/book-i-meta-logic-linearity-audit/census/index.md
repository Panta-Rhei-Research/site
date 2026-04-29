---
{
  "projection_kind": "taulib_declaration",
  "title": "census",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/census/",
  "summary_short": "`def` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::census",
  "declaration_slug": "census",
  "kind": "def",
  "name": "census",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 78,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L78-L172",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearityAudit",
        "url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L78-L172",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.MetaLogic.LinearityAudit](/verify/taulib/docs/book-i-meta-logic-linearity-audit/)
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L78-L172)
- Source range: L78-L172
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete census of 82 TauLib modules (pre-MetaLogic).
    Organized by directory.

    Directory counts:
    - Kernel:      3  (Signature, Axioms, Diagonal)
    - Orbit:       8  (Generation, Countability, Closure, Rigidity, Ladder,
                        TooMany, TooFew, Saturation)
    - Denotation:  8  (TauIdx, RankTransfer, ProgramMonoid, Equality, Order,
                        Arithmetic, GrowthEscape, Structural)
    - Coordinates: 8  (NoTie, NormalForm, Descent, ABCD, Hyperfact,
                        TowerAtoms, PrimeEnumeration, Primes*)
    - Polarity:   14  (Spectral, Polarity, PolarizedGerms, Lemniscate,
                        BipolarAlgebra, OmegaRing, OmegaGerms, PrimeBridge,
                        ExtGCD, ChineseRemainder, ModArith, NthPrime,
                        CRTBasis, TeichmuellerLift)
    - Boundary:   11  (NumberTower, Ring, SplitComplex, Iota, Spectral,
                        Characters, Fourier, ConstructiveReals, ComplexField,
                        Quaternions, Cyclotomic)
    - Logic:       3  (Truth4, Explosion, BooleanRecovery)
    - Sets:        7  (Membership, Operations, Powerset, Universe,
                        CantorRefutation, Counting, UniqueInfinity)
    - Holomorphy:  9  (DHolomorphic, TauHolomorphic, DiagonalProtection,
                        IdentityTheorem, SpectralCoefficients*, Thinness,
                        GlobalHartogs, BoundaryInterior, PresheafEssence)
    - Topos:       7  (Functors, EarnedArrows, LimitsSites, EarnedTopos,
                        CartesianProduct, WedgeProduct, InternalHom)
    - Spectrum:    4  (ThreeSAT, InterfaceWidth, KernelHinge, TTM)

    * = non-constructive (see classification below)
-/
```

## Source Excerpt

```lean
def census : List ModuleEntry :=
  -- Kernel (3)
  [ ⟨"Signature",           "Kernel",      .constructive⟩
  , ⟨"Axioms",              "Kernel",      .constructive⟩
  , ⟨"Diagonal",            "Kernel",      .constructive⟩
  -- Orbit (8)
  , ⟨"Generation",          "Orbit",       .constructive⟩
  , ⟨"Countability",        "Orbit",       .constructive⟩
  , ⟨"Closure",             "Orbit",       .constructive⟩
  , ⟨"Rigidity",            "Orbit",       .constructive⟩
  , ⟨"Ladder",              "Orbit",       .constructive⟩
  , ⟨"TooMany",             "Orbit",       .constructive⟩
  , ⟨"TooFew",              "Orbit",       .constructive⟩
  , ⟨"Saturation",          "Orbit",       .constructive⟩
  -- Denotation (8)
  , ⟨"TauIdx",              "Denotation",  .constructive⟩
  , ⟨"RankTransfer",        "Denotation",  .constructive⟩
  , ⟨"ProgramMonoid",       "Denotation",  .constructive⟩
  , ⟨"Equality",            "Denotation",  .constructive⟩
  , ⟨"Order",               "Denotation",  .constructive⟩
  , ⟨"Arithmetic",          "Denotation",  .constructive⟩
  , ⟨"GrowthEscape",        "Denotation",  .constructive⟩
  , ⟨"Structural",          "Denotation",  .constructive⟩
  -- Coordinates (8) — Primes uses Classical.em
  , ⟨"NoTie",               "Coordinates", .constructive⟩
  , ⟨"NormalForm",          "Coordinates", .constructive⟩
  , ⟨"Descent",             "Coordinates", .constructive⟩
  , ⟨"ABCD",                "Coordinates", .constructive⟩
  , ⟨"Hyperfact",           "Coordinates", .constructive⟩
  , ⟨"TowerAtoms",          "Coordinates", .constructive⟩
  , ⟨"PrimeEnumeration",    "Coordinates", .constructive⟩
  , ⟨"Primes",              "Coordinates", .classical⟩
  -- Polarity (14)
  , ⟨"Spectral",            "Polarity",    .constructive⟩
  , ⟨"Polarity",            "Polarity",    .constructive⟩
  , ⟨"PolarizedGerms",      "Polarity",    .constructive⟩
  , ⟨"Lemniscate",          "Polarity",    .constructive⟩
  , ⟨"BipolarAlgebra",      "Polarity",    .constructive⟩
  , ⟨"OmegaRing",           "Polarity",    .constructive⟩
  , ⟨"OmegaGerms",          "Polarity",    .constructive⟩
  , ⟨"PrimeBridge",         "Polarity",    .constructive⟩
  , ⟨"ExtGCD",              "Polarity",    .constructive⟩
  , ⟨"ChineseRemainder",    "Polarity",    .constructive⟩
  , ⟨"ModArith",            "Polarity",    .constructive⟩
  , ⟨"NthPrime",            "Polarity",    .constructive⟩
  , ⟨"CRTBasis",            "Polarity",    .constructive⟩
  , ⟨"TeichmuellerLift",    "Polarity",    .constructive⟩
  -- Boundary (11)
  , ⟨"NumberTower",         "Boundary",    .constructive⟩
  , ⟨"Ring",                "Boundary",    .constructive⟩
  , ⟨"SplitComplex",        "Boundary",    .constructive⟩
  , ⟨"Iota",                "Boundary",    .constructive⟩
  , ⟨"Spectral",            "Boundary",    .constructive⟩
  , ⟨"Characters",          "Boundary",    .constructive⟩
  , ⟨"Fourier",             "Boundary",    .constructive⟩
  , ⟨"ConstructiveReals",   "Boundary",    .constructive⟩
  , ⟨"ComplexField",        "Boundary",    .constructive⟩
  , ⟨"Quaternions",         "Boundary",    .constructive⟩
  , ⟨"Cyclotomic",          "Boundary",    .constructive⟩
  -- Logic (3)
  , ⟨"Truth4",              "Logic",       .constructive⟩
  , ⟨"Explosion",           "Logic",       .constructive⟩
  , ⟨"BooleanRecovery",     "Logic",       .constructive⟩
  -- Sets (7)
  , ⟨"Membership",          "Sets",        .constructive⟩
  , ⟨"Operations",          "Sets",        .constructive⟩
  , ⟨"Powerset",            "Sets",        .constructive⟩
  , ⟨"Universe",            "Sets",        .constructive⟩
  , ⟨"CantorRefutation",    "Sets",        .constructive⟩
  , ⟨"Counting",            "Sets",        .constructive⟩
  , ⟨"UniqueInfinity",      "Sets",        .constructive⟩
  -- Holomorphy (9) — SpectralCoefficients uses funext tactic
  , ⟨"DHolomorphic",        "Holomorphy",  .constructive⟩
  , ⟨"TauHolomorphic",      "Holomorphy",  .constructive⟩
  , ⟨"DiagonalProtection",  "Holomorphy",  .constructive⟩
  , ⟨"IdentityTheorem",     "Holomorphy",  .constructive⟩
  , ⟨"SpectralCoefficients","Holomorphy",  .kernelAxiom⟩
  , ⟨"Thinness",            "Holomorphy",  .constructive⟩
  , ⟨"GlobalHartogs",       "Holomorphy",  .constructive⟩
  , ⟨"BoundaryInterior",    "Holomorphy",  .constructive⟩
  , ⟨"PresheafEssence",     "Holomorphy",  .constructive⟩
  -- Topos (7)
  , ⟨"Functors",            "Topos",       .constructive⟩
  , ⟨"EarnedArrows",        "Topos",       .constructive⟩
  , ⟨"LimitsSites",         "Topos",       .constructive⟩
  , ⟨"EarnedTopos",         "Topos",       .constructive⟩
  , ⟨"CartesianProduct",    "Topos",       .constructive⟩
  , ⟨"WedgeProduct",        "Topos",       .constructive⟩
  , ⟨"InternalHom",         "Topos",       .constructive⟩
  -- Spectrum (4)
  , ⟨"ThreeSAT",            "Spectrum",    .constructive⟩
  , ⟨"InterfaceWidth",      "Spectrum",    .constructive⟩
  , ⟨"KernelHinge",         "Spectrum",    .constructive⟩
  , ⟨"TTM",                 "Spectrum",    .constructive⟩
  ]
```
