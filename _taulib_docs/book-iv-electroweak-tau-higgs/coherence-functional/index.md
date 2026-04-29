---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceFunctional",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/coherence-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::CoherenceFunctional",
  "declaration_slug": "coherence-functional",
  "kind": "structure",
  "name": "CoherenceFunctional",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 86,
  "source_line_end": 97,
  "registry_ids": [
    "IV.D135"
  ],
  "related_registry_items": [
    {
      "id": "IV.D135",
      "title": "Finite-Stage Coherence Functional",
      "url": "/registry/object/IV.D135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L86-L97",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L86-L97",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L86-L97)
- Source range: L86-L97
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D135` — Finite-Stage Coherence Functional

## Immediate Comment / Docstring

```lean
/-- [IV.D135] The coherence functional V_n on crossing excitations.
    V_n measures the coherence cost of displacing the ω-sector field
    from its equilibrium. The subscript n indicates evaluation at
    tower level n of the refinement tower.

    V_n has the form of a Mexican hat potential, but this form is
    DERIVED from coherence constraints, not postulated. -/
```

## Source Excerpt

```lean
structure CoherenceFunctional where
  /-- Tower level at which V_n is evaluated. -/
  tower_level : Nat
  /-- Tower level is positive. -/
  level_pos : tower_level > 0
  /-- The functional has a Mexican hat shape. -/
  mexican_hat : Bool := true
  /-- Minimum exists. -/
  minimum_exists : Bool := true
  /-- Minimum is unique (up to S¹ degeneracy). -/
  minimum_unique_mod_circle : Bool := true
  deriving Repr
```
