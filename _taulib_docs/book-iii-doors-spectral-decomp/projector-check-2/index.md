---
{
  "projection_kind": "taulib_declaration",
  "title": "projector_check_2",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/projector-check-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::projector_check_2",
  "declaration_slug": "projector-check-2",
  "kind": "theorem",
  "name": "projector_check_2",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 208,
  "source_line_end": 209,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L208-L209",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L208-L209",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/verify/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L208-L209)
- Source range: L208-L209
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Projectors correct at N = 2. -/
```

## Source Excerpt

```lean
theorem projector_check_2 :
    projector_check 2 = true := by native_decide
```
