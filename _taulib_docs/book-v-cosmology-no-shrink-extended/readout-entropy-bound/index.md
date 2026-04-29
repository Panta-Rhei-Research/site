---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutEntropyBound",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/readout-entropy-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::ReadoutEntropyBound",
  "declaration_slug": "readout-entropy-bound",
  "kind": "structure",
  "name": "ReadoutEntropyBound",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 274,
  "source_line_end": 280,
  "registry_ids": [
    "V.T272"
  ],
  "related_registry_items": [
    {
      "id": "V.T272",
      "title": "Readout Channel Entropy Bound",
      "url": "/registry/object/V.T272/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L274-L280",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L274-L280",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L274-L280)
- Source range: L274-L280
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T272` — Readout Channel Entropy Bound

## Immediate Comment / Docstring

```lean
/-- [V.T272] Readout channel entropy bound.
    The readout state ρ_out has von Neumann entropy bounded by
    log(dim H_∂), which is strictly less than S_BH.
    The readout channel cannot carry away full ontic information.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure ReadoutEntropyBound where
  /-- Dimension of boundary Hilbert space (log scale, in nats). -/
  log_dim_boundary : Nat
  /-- BH entropy (log scale, in nats). -/
  s_bh : Nat
  /-- Strict inequality: boundary dimension < total BH entropy. -/
  boundary_lt_bh : log_dim_boundary < s_bh
```
