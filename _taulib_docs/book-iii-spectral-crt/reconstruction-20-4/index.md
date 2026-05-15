---
{
  "projection_kind": "taulib_declaration",
  "title": "reconstruction_20_4",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-crt/reconstruction-20-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::reconstruction_20_4",
  "declaration_slug": "reconstruction-20-4",
  "kind": "theorem",
  "name": "reconstruction_20_4",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 229,
  "source_line_end": 230,
  "registry_ids": [
    "III.D20"
  ],
  "related_registry_items": [
    {
      "id": "III.D20",
      "title": "Reconstruction Functor",
      "url": "/registry/object/III.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L229-L230",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/corpus/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L229-L230",
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

- Module: [TauLib.BookIII.Spectral.CRT](/corpus/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L229-L230)
- Source range: L229-L230
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D20` — Reconstruction Functor

## Immediate Comment / Docstring

```lean
-- Reconstruction functor [III.D20]
```

## Source Excerpt

```lean
theorem reconstruction_20_4 :
    reconstruction_functor_check 20 4 = true := by native_decide
```
