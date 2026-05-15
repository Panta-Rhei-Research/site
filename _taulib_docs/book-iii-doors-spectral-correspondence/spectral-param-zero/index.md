---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_param_zero",
  "permalink": "/corpus/taulib/docs/book-iii-doors-spectral-correspondence/spectral-param-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_param_zero",
  "declaration_slug": "spectral-param-zero",
  "kind": "theorem",
  "name": "spectral_param_zero",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/corpus/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 161,
  "source_line_end": 162,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L161-L162",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralCorrespondence",
        "url": "/corpus/taulib/docs/book-iii-doors-spectral-correspondence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L161-L162",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Doors.SpectralCorrespondence](/corpus/taulib/docs/book-iii-doors-spectral-correspondence/)
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L161-L162)
- Source range: L161-L162
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D29` — Spectral Parameter Λ(s)

## Immediate Comment / Docstring

```lean
/-- [III.D29] Structural: spectral parameter at depth 0 is always 0. -/
```

## Source Excerpt

```lean
theorem spectral_param_zero :
    spectral_parameter 42 0 = 0 := rfl
```
