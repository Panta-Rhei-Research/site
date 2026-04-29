---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_fiber_check",
  "permalink": "/verify/taulib/docs/book-ii-interior-omega-readout/primorial-fiber-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::primorial_fiber_check",
  "declaration_slug": "primorial-fiber-check",
  "kind": "def",
  "name": "primorial_fiber_check",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/verify/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 81,
  "source_line_end": 82,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L81-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/verify/taulib/docs/book-ii-interior-omega-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L81-L82",
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/verify/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L81-L82)
- Source range: L81-L82
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T02` — Fiber Degeneration at Omega

## Immediate Comment / Docstring

```lean
/-- [II.T02] Primorial path fiber degeneration.
    Along the primorial tower, B = C = 1 always: balanced (crossing point). -/
```

## Source Excerpt

```lean
def primorial_fiber_check : Bool :=
  primorial_witness.all fun (_, p) => p.fiber_dominance == .balanced
```
