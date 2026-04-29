---
{
  "projection_kind": "taulib_declaration",
  "title": "g_tau_well_defined",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/g-tau-well-defined/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::g_tau_well_defined",
  "declaration_slug": "g-tau-well-defined",
  "kind": "theorem",
  "name": "g_tau_well_defined",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 186,
  "source_line_end": 188,
  "registry_ids": [
    "V.P01"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L186-L188",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.GravitationalConstant",
        "url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L186-L188",
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

- Module: [TauLib.BookV.Gravity.GravitationalConstant](/verify/taulib/docs/book-v-gravity-gravitational-constant/)
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L186-L188)
- Source range: L186-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P01] G_τ is well-defined: the gravitational constant structure
    requires a positive numerator and denominator. -/
```

## Source Excerpt

```lean
theorem g_tau_well_defined (g : GravConstant) :
    g.g_numer > 0 ∧ g.g_denom > 0 :=
  ⟨g.g_positive, g.denom_pos⟩
```
