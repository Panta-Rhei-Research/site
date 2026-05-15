---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_kelvin_budget",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/remark-kelvin-budget/",
  "summary_short": "`def` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::remark_kelvin_budget",
  "declaration_slug": "remark-kelvin-budget",
  "kind": "def",
  "name": "remark_kelvin_budget",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 82,
  "source_line_end": 83,
  "registry_ids": [
    "IV.R170"
  ],
  "related_registry_items": [
    {
      "id": "IV.R170",
      "title": "Kelvin theorem as budget law",
      "url": "/registry/object/IV.R170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L82-L83",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L82-L83",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/corpus/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L82-L83)
- Source range: L82-L83
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `IV.R170` — Kelvin theorem as budget law

## Immediate Comment / Docstring

```lean
/-- [IV.R170] Kelvin's circulation theorem (integral v dot dl conserved in
    inviscid barotropic flow) is the chart-level readout of the tau-Euler
    budget law: the ontic content is budget conservation in D. -/
```

## Source Excerpt

```lean
def remark_kelvin_budget : String :=
  "Kelvin circulation theorem = chart-level readout of tau-Euler budget law"
```
