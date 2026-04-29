---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_primorial_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/goldbach-primorial-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::goldbach_primorial_3",
  "declaration_slug": "goldbach-primorial-3",
  "kind": "theorem",
  "name": "goldbach_primorial_3",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 203,
  "source_line_end": 204,
  "registry_ids": [
    "III.T64"
  ],
  "related_registry_items": [
    {
      "id": "III.T64",
      "title": "Goldbach at Primorial Levels",
      "url": "/registry/object/III.T64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L203-L204",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L203-L204",
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/verify/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L203-L204)
- Source range: L203-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T64` — Goldbach at Primorial Levels

## Immediate Comment / Docstring

```lean
/-- [III.T64] Goldbach at primorial levels up to depth 3. -/
```

## Source Excerpt

```lean
theorem goldbach_primorial_3 :
    goldbach_primorial_check 3 = true := by native_decide
```
