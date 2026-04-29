---
{
  "projection_kind": "taulib_declaration",
  "title": "d_sector_holonomy_gap",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/d-sector-holonomy-gap/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::d_sector_holonomy_gap",
  "declaration_slug": "d-sector-holonomy-gap",
  "kind": "theorem",
  "name": "d_sector_holonomy_gap",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 279,
  "source_line_end": 281,
  "registry_ids": [
    "V.T20"
  ],
  "related_registry_items": [
    {
      "id": "V.T20",
      "title": "Gravity as frame holonomy gap",
      "url": "/registry/object/V.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L279-L281",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L279-L281",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L279-L281)
- Source range: L279-L281
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T20` — Gravity as frame holonomy gap

## Immediate Comment / Docstring

```lean
/-- [V.T20] The D-sector holonomy gap equals the frame holonomy gap.

    The gravitational frame holonomy at depth n is determined entirely
    by the D-sector boundary character. The gap is the minimal
    non-trivial holonomy element: gap_numer = 1 (in normalized units). -/
```

## Source Excerpt

```lean
theorem d_sector_holonomy_gap (h : FrameHolonomy) :
    h.gap_numer = 1 :=
  h.gap_minimal.1
```
