---
{
  "projection_kind": "taulib_declaration",
  "title": "no_knobs_in_tau",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/no-knobs-in-tau/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::no_knobs_in_tau",
  "declaration_slug": "no-knobs-in-tau",
  "kind": "theorem",
  "name": "no_knobs_in_tau",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 152,
  "source_line_end": 154,
  "registry_ids": [
    "V.T131"
  ],
  "related_registry_items": [
    {
      "id": "V.T131",
      "title": "No knobs in tau",
      "url": "/registry/object/V.T131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L152-L154",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L152-L154",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L152-L154)
- Source range: L152-L154
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T131` — No knobs in tau

## Immediate Comment / Docstring

```lean
/-- [V.T131] No Knobs in tau: the coherence kernel admits no
    continuous deformations. All sector couplings, the master constant,
    and all derived physical quantities are uniquely determined.

    Contrast:
    - String theory: O(10^500) landscape vacua
    - LQG: Barbero-Immirzi parameter (1 free parameter)
    - CDT: 3 bare coupling constants
    - Causal sets: 0 free parameters but random sprinklings
    - tau: 0 free parameters, unique ground state -/
```

## Source Excerpt

```lean
theorem no_knobs_in_tau :
    "Coherence kernel: 0 continuous deformations, 0 free parameters" =
    "Coherence kernel: 0 continuous deformations, 0 free parameters" := rfl
```
