---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_30",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::pi_30",
  "declaration_slug": "pi-30",
  "kind": "theorem",
  "name": "pi_30",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 297,
  "source_line_end": 297,
  "registry_ids": [
    "III.D100"
  ],
  "related_registry_items": [
    {
      "id": "III.D100",
      "title": "Sieve Prime Count",
      "url": "/registry/object/III.D100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L297-L297",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L297-L297",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L297-L297)
- Source range: L297-L297
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D100` — Sieve Prime Count

## Immediate Comment / Docstring

```lean
/-- [III.D100] π(30) = 10. -/
```

## Source Excerpt

```lean
theorem pi_30 : sieve_prime_count 30 = 10 := by native_decide
```
