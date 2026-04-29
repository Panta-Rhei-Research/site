---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsMechanism",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/higgs-mechanism/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::HiggsMechanism",
  "declaration_slug": "higgs-mechanism",
  "kind": "structure",
  "name": "HiggsMechanism",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 60,
  "source_line_end": 71,
  "registry_ids": [
    "IV.D134"
  ],
  "related_registry_items": [
    {
      "id": "IV.D134",
      "title": "Coherence Fixing (Formal)",
      "url": "/registry/object/IV.D134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L60-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L60-L71",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L60-L71)
- Source range: L60-L71
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D134` — Coherence Fixing (Formal)

## Immediate Comment / Docstring

```lean
/-- [IV.D134] The Higgs mechanism in the τ-framework: the ω-sector
    (crossing of B and C lobes) provides a smooth resolution of
    the crossing singularity at the lemniscate junction.

    This is NOT a separate field — it is the structural content
    of the fifth generator ω acting at the B∩C intersection. -/
```

## Source Excerpt

```lean
structure HiggsMechanism where
  /-- The mediating sector. -/
  sector : Sector := .Omega
  /-- The resolved sectors. -/
  resolved_B : Sector := .B
  resolved_C : Sector := .C
  /-- The crossing coupling κ(B,C) governs the mechanism. -/
  coupling_numer : Nat := kappa_BC.numer
  coupling_denom : Nat := kappa_BC.denom
  /-- Not a separate field — structural resolution. -/
  is_structural : Bool := true
  deriving Repr
```
