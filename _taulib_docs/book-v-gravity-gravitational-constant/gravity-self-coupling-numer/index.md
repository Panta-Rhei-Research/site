---
{
  "projection_kind": "taulib_declaration",
  "title": "gravity_self_coupling_numer",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/gravity-self-coupling-numer/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::gravity_self_coupling_numer",
  "declaration_slug": "gravity-self-coupling-numer",
  "kind": "def",
  "name": "gravity_self_coupling_numer",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 164,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L164-L164",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L164-L164",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.Gravity.GravitationalConstant](/verify/taulib/docs/book-v-gravity-gravitational-constant/)
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L164-L164)
- Source range: L164-L164
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The gravity sector self-coupling κ(D;1) = 1 − ι_τ connects to G_τ. -/
```

## Source Excerpt

```lean
def gravity_self_coupling_numer : Nat := iotaD - iota
```
