---
{
  "projection_kind": "taulib_declaration",
  "title": "LinearConfinementPotential",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/linear-confinement-potential/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::LinearConfinementPotential",
  "declaration_slug": "linear-confinement-potential",
  "kind": "structure",
  "name": "LinearConfinementPotential",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 197,
  "source_line_end": 204,
  "registry_ids": [
    "IV.P96"
  ],
  "related_registry_items": [
    {
      "id": "IV.P96",
      "title": "Linear Confinement Potential",
      "url": "/registry/object/IV.P96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L197-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L197-L204",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L197-L204)
- Source range: L197-L204
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P96` — Linear Confinement Potential

## Immediate Comment / Docstring

```lean
/-- [IV.P96] The defect functional for a quark-antiquark pair:
    D_C(delta) = D_C(0) + sigma_tau * delta + O(delta^2),
    where sigma_tau = kappa(C;3) * g[omega]_s is the tau-string tension.

    The linear growth with separation delta is the structural origin
    of the confining flux tube / QCD string. -/
```

## Source Excerpt

```lean
structure LinearConfinementPotential where
  /-- Linear growth with separation. -/
  linear_growth : Bool := true
  /-- String tension involves kappa(C;3). -/
  tension_involves_kappa_C : Bool := true
  /-- Produces flux tube / string. -/
  flux_tube : Bool := true
  deriving Repr
```
