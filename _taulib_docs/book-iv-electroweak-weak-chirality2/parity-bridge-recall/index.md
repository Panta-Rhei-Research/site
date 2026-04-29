---
{
  "projection_kind": "taulib_declaration",
  "title": "ParityBridgeRecall",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/parity-bridge-recall/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::ParityBridgeRecall",
  "declaration_slug": "parity-bridge-recall",
  "kind": "structure",
  "name": "ParityBridgeRecall",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 88,
  "source_line_end": 94,
  "registry_ids": [
    "IV.T122"
  ],
  "related_registry_items": [
    {
      "id": "IV.T122",
      "title": "Parity Bridge --- recalled from III.T07",
      "url": "/registry/object/IV.T122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L88-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L88-L94",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L88-L94)
- Source range: L88-L94
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T122` — Parity Bridge --- recalled from III.T07

## Immediate Comment / Docstring

```lean
/-- [IV.T122] Parity Bridge Recall (III.T07): the A-sector is the unique
    sector where the sigma-involution acts non-trivially on chirality.
    This is the physical consequence of the Parity Bridge theorem
    from Book III. The balanced polarity (chi_plus = chi_minus = 50)
    implies maximal parity violation. -/
```

## Source Excerpt

```lean
structure ParityBridgeRecall where
  /-- The A-sector has balanced polarity. -/
  a_balanced : pol_A.chi_plus = pol_A.chi_minus
  /-- Only A is balanced among primitive sectors. -/
  d_not_balanced : pol_D.chi_plus ≠ pol_D.chi_minus
  b_not_balanced : pol_B.chi_plus ≠ pol_B.chi_minus
  c_not_balanced : pol_C.chi_plus ≠ pol_C.chi_minus
```
