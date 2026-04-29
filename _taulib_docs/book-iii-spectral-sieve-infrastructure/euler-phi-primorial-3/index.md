---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_phi_primorial_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::euler_phi_primorial_3",
  "declaration_slug": "euler-phi-primorial-3",
  "kind": "theorem",
  "name": "euler_phi_primorial_3",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 307,
  "source_line_end": 308,
  "registry_ids": [
    "III.T67"
  ],
  "related_registry_items": [
    {
      "id": "III.T67",
      "title": "Sieve-Tower Compatibility",
      "url": "/registry/object/III.T67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L307-L308",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L307-L308",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L307-L308)
- Source range: L307-L308
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T67` — Sieve-Tower Compatibility

## Immediate Comment / Docstring

```lean
/-- [III.T67] Euler phi at primorial 3 = φ(30) = (2-1)(3-1)(5-1) = 8. -/
```

## Source Excerpt

```lean
theorem euler_phi_primorial_3 :
    euler_phi_primorial 3 = 8 := by native_decide
```
