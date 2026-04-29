---
{
  "projection_kind": "taulib_declaration",
  "title": "BookIVMetaclosure",
  "permalink": "/verify/taulib/docs/book-iv-coda-self-describing/book-ivmetaclosure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.SelfDescribing`.",
  "declaration_id": "TauLib.BookIV.Coda.SelfDescribing::BookIVMetaclosure",
  "declaration_slug": "book-ivmetaclosure",
  "kind": "structure",
  "name": "BookIVMetaclosure",
  "module_name": "TauLib.BookIV.Coda.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-iv-coda-self-describing/",
  "source_line_start": 146,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L146-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.SelfDescribing",
        "url": "/verify/taulib/docs/book-iv-coda-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L146-L161",
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

- Module: [TauLib.BookIV.Coda.SelfDescribing](/verify/taulib/docs/book-iv-coda-self-describing/)
- Source path: [`TauLib/BookIV/Coda/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L146-L161)
- Source range: L146-L161
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Metaclosure summary: what Book IV has achieved.

    Inputs:
    - 7 axioms K0-K6 (Book I)
    - 1 empirical anchor: m_n = 939.565 MeV
    - 0 free parameters

    Outputs (fiber T^2 physics):
    - Complete particle spectrum (quarks, leptons, bosons, 3 generations)
    - Quantum mechanics (uncertainty, measurement, Born rule)
    - Electroweak sector (EM, weak, Weinberg mixing, Higgs)
    - Strong sector (confinement, mass gap, color)
    - Many-body physics (9 regimes, phase transitions)
    - Condensed matter (crystal, glass, superfluid, superconductor)
    - Constants: 10 couplings, alpha, R, m_e, M_W, M_Z, M_H, ...

    What remains for Book V: base tau^1 physics (gravity, cosmology). -/
```

## Source Excerpt

```lean
structure BookIVMetaclosure where
  /-- Number of axioms. -/
  num_axioms : Nat := 9
  /-- Empirical anchors. -/
  num_anchors : Nat := 1
  /-- Free parameters. -/
  free_params : Nat := 0
  /-- Parts in Book IV. -/
  num_parts : Nat := 7
  /-- Chapters. -/
  num_chapters : Nat := 57
  /-- Fiber physics complete. -/
  fiber_complete : Bool := true
  /-- Base physics deferred to Book V. -/
  base_deferred : Bool := true
  deriving Repr
```
