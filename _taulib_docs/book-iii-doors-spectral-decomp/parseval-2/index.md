---
{
  "projection_kind": "taulib_declaration",
  "title": "parseval_2",
  "permalink": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/parseval-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::parseval_2",
  "declaration_slug": "parseval-2",
  "kind": "theorem",
  "name": "parseval_2",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 224,
  "source_line_end": 225,
  "registry_ids": [
    "III.T56"
  ],
  "related_registry_items": [
    {
      "id": "III.T56",
      "title": "Parseval Identity",
      "url": "/registry/object/III.T56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L224-L225",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L224-L225",
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
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L224-L225)
- Source range: L224-L225
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.T56` — Parseval Identity

## Immediate Comment / Docstring

```lean
/-- [III.T56] Parseval identity at N = 2. -/
```

## Source Excerpt

```lean
theorem parseval_2 :
    parseval_check 2 = true := by native_decide
```
