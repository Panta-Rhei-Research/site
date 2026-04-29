---
{
  "projection_kind": "taulib_declaration",
  "title": "NucleosyntheticWindow",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthetic-window/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::NucleosyntheticWindow",
  "declaration_slug": "nucleosynthetic-window",
  "kind": "structure",
  "name": "NucleosyntheticWindow",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 205,
  "source_line_end": 214,
  "registry_ids": [
    "V.D161"
  ],
  "related_registry_items": [
    {
      "id": "V.D161",
      "title": "Nucleosynthetic Window",
      "url": "/registry/object/V.D161/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L205-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L205-L214",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L205-L214)
- Source range: L205-L214
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D161` — Nucleosynthetic Window

## Immediate Comment / Docstring

```lean
/-- [V.D161] Nucleosynthetic window W_nuc: the interval of refinement
    depths during which light nuclei (D, He-3, He-4, Li-7) can form.

    Opens at n_nuc^open and closes at n_nuc^close. The window width
    determines the primordial element abundances. -/
```

## Source Excerpt

```lean
structure NucleosyntheticWindow where
  /-- Opening depth. -/
  open_depth : Nat
  /-- Closing depth. -/
  close_depth : Nat
  /-- Opens before closing. -/
  opens_before_close : open_depth < close_depth
  /-- Both positive. -/
  open_pos : open_depth > 0
  deriving Repr
```
