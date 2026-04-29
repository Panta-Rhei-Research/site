---
{
  "projection_kind": "taulib_declaration",
  "title": "gravity_coupling_positive",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/gravity-coupling-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::gravity_coupling_positive",
  "declaration_slug": "gravity-coupling-positive",
  "kind": "theorem",
  "name": "gravity_coupling_positive",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L191-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L191-L193",
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
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L191-L193)
- Source range: L191-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The gravity self-coupling is positive (1 − ι_τ > 0 since ι_τ < 1). -/
```

## Source Excerpt

```lean
theorem gravity_coupling_positive :
    gravity_self_coupling_numer > 0 := by
  simp [gravity_self_coupling_numer, iotaD, iota, iota_tau_denom, iota_tau_numer]
```
