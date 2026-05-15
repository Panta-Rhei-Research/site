---
{
  "projection_kind": "taulib_declaration",
  "title": "measure_total_30",
  "permalink": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/measure-total-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::measure_total_30",
  "declaration_slug": "measure-total-30",
  "kind": "theorem",
  "name": "measure_total_30",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 220,
  "source_line_end": 221,
  "registry_ids": [
    "III.D81"
  ],
  "related_registry_items": [
    {
      "id": "III.D81",
      "title": "Spectral Projector",
      "url": "/registry/object/III.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L220-L221",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L220-L221",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/corpus/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L220-L221)
- Source range: L220-L221
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D81` — Spectral Projector

## Immediate Comment / Docstring

```lean
/-- [III.D81] Spectral measure total at N = 30. -/
```

## Source Excerpt

```lean
theorem measure_total_30 :
    measure_total_check 30 = true := by native_decide
```
