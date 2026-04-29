---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_20",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-20/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_20",
  "declaration_slug": "hensel-20",
  "kind": "theorem",
  "name": "hensel_20",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 168,
  "source_line_end": 169,
  "registry_ids": [
    "III.T11"
  ],
  "related_registry_items": [
    {
      "id": "III.T11",
      "title": "Constructive Hensel Lifting",
      "url": "/registry/object/III.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L168-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.HenselLifting",
        "url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L168-L169",
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

- Module: [TauLib.BookIII.Spectral.HenselLifting](/verify/taulib/docs/book-iii-spectral-hensel-lifting/)
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L168-L169)
- Source range: L168-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Hensel lifting [III.T11]
```

## Source Excerpt

```lean
theorem hensel_20 :
    hensel_check 20 = true := by native_decide
```
