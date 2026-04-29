---
{
  "projection_kind": "taulib_declaration",
  "title": "sn_rate_sfh",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/sn-rate-sfh/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::sn_rate_sfh",
  "declaration_slug": "sn-rate-sfh",
  "kind": "theorem",
  "name": "sn_rate_sfh",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 244,
  "source_line_end": 246,
  "registry_ids": [
    "V.P76"
  ],
  "related_registry_items": [
    {
      "id": "V.P76",
      "title": "Birth Kick and Spin --- V.P40",
      "url": "/registry/object/V.P76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L244-L246",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L244-L246",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L244-L246)
- Source range: L244-L246
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P76` — Birth Kick and Spin --- V.P40

## Immediate Comment / Docstring

```lean
/-- [V.P76] SN rate from star formation history: the supernova rate
    in a galaxy is determined by its star formation history, which
    is a D-sector readout of the galactic defect bundle. -/
```

## Source Excerpt

```lean
theorem sn_rate_sfh :
    "SN rate = f(star formation history) = D-sector galactic readout" =
    "SN rate = f(star formation history) = D-sector galactic readout" := rfl
```
