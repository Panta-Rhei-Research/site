---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_div_6",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/primorial-div-6/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::primorial_div_6",
  "declaration_slug": "primorial-div-6",
  "kind": "theorem",
  "name": "primorial_div_6",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 158,
  "source_line_end": 159,
  "registry_ids": [
    "III.D19"
  ],
  "related_registry_items": [
    {
      "id": "III.D19",
      "title": "Primorial Ladder",
      "url": "/registry/object/III.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L158-L159",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.PrimorialLadder",
        "url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L158-L159",
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

- Module: [TauLib.BookIII.Spectral.PrimorialLadder](/verify/taulib/docs/book-iii-spectral-primorial-ladder/)
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L158-L159)
- Source range: L158-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D19` — Primorial Ladder

## Immediate Comment / Docstring

```lean
-- Primorial divisibility [III.D19]
```

## Source Excerpt

```lean
theorem primorial_div_6 :
    primorial_divisibility_check 6 = true := by native_decide
```
