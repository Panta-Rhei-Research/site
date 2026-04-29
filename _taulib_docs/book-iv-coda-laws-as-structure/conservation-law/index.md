---
{
  "projection_kind": "taulib_declaration",
  "title": "ConservationLaw",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/conservation-law/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::ConservationLaw",
  "declaration_slug": "conservation-law",
  "kind": "inductive",
  "name": "ConservationLaw",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 102,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L102-L119",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L102-L119",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/verify/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L102-L119)
- Source range: L102-L119
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Conservation laws known to be tower-natural. -/
```

## Source Excerpt

```lean
inductive ConservationLaw where
  /-- Energy conservation from temporal tower-naturality. -/
  | Energy
  /-- Momentum conservation from spatial tower-naturality. -/
  | Momentum
  /-- Angular momentum from rotational tower-naturality on T^2. -/
  | AngularMomentum
  /-- Electric charge from U(1) holonomy on B-sector. -/
  | ElectricCharge
  /-- Color charge from SU(3) holonomy on C-sector. -/
  | ColorCharge
  /-- Baryon number from eta-sector winding. -/
  | BaryonNumber
  /-- Lepton number from gamma-sector winding. -/
  | LeptonNumber
  /-- Topological charge from pi_1(T^2). -/
  | TopologicalCharge
  deriving Repr, DecidableEq, BEq
```
