---
{
  "projection_kind": "taulib_declaration",
  "title": "brun_30_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-30-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::brun_30_3",
  "declaration_slug": "brun-30-3",
  "kind": "theorem",
  "name": "brun_30_3",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 304,
  "source_line_end": 304,
  "registry_ids": [
    "III.D101"
  ],
  "related_registry_items": [
    {
      "id": "III.D101",
      "title": "Brun Sieve Count",
      "url": "/registry/object/III.D101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L304-L304",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.SieveInfrastructure",
        "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L304-L304",
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

- Module: [TauLib.BookIII.Spectral.SieveInfrastructure](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/)
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L304-L304)
- Source range: L304-L304
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D101` — Brun Sieve Count

## Immediate Comment / Docstring

```lean
/-- [III.D101] Brun sieve at (30, 3): 8 integers in [1..30] coprime
    to {2,3,5}. These are: 1, 7, 11, 13, 17, 19, 23, 29. -/
```

## Source Excerpt

```lean
theorem brun_30_3 : brun_sieve_count 30 3 = 8 := by native_decide
```
