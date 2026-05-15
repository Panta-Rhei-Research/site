---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_path_check",
  "permalink": "/corpus/taulib/docs/book-ii-interior-omega-readout/tower-path-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::tower_path_check",
  "declaration_slug": "tower-path-check",
  "kind": "def",
  "name": "tower_path_check",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/corpus/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 95,
  "source_line_end": 97,
  "registry_ids": [
    "II.T02"
  ],
  "related_registry_items": [
    {
      "id": "II.T02",
      "title": "Fiber Degeneration at Omega",
      "url": "/registry/object/II.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L95-L97",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L95-L97",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/corpus/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L95-L97)
- Source range: L95-L97
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.T02` — Fiber Degeneration at Omega

## Immediate Comment / Docstring

```lean
/-- [II.T02] Tower path (X_n = 2^n) is B-dominant. -/
```

## Source Excerpt

```lean
def tower_path_check : Bool :=
  let points := [4, 8, 16, 32, 64, 128, 256].map from_tau_idx
  points.all fun p => p.b > p.c
```
