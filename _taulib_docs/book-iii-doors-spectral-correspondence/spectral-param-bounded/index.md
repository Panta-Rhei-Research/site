---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_param_bounded",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-param-bounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_param_bounded",
  "declaration_slug": "spectral-param-bounded",
  "kind": "theorem",
  "name": "spectral_param_bounded",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 165,
  "source_line_end": 166,
  "registry_ids": [
    "III.D29"
  ],
  "related_registry_items": [
    {
      "id": "III.D29",
      "title": "Spectral Parameter Λ(s)",
      "url": "/registry/object/III.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L165-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralCorrespondence",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L165-L166",
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

- Module: [TauLib.BookIII.Doors.SpectralCorrespondence](/verify/taulib/docs/book-iii-doors-spectral-correspondence/)
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L165-L166)
- Source range: L165-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D29` — Spectral Parameter Λ(s)

## Immediate Comment / Docstring

```lean
/-- [III.D29] Structural: spectral parameter at depth k is bounded. -/
```

## Source Excerpt

```lean
theorem spectral_param_bounded :
    spectral_parameter 100 4 ≤ 4 := by native_decide
```
