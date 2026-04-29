---
{
  "projection_kind": "taulib_declaration",
  "title": "causal_disconnection",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/causal-disconnection/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::causal_disconnection",
  "declaration_slug": "causal-disconnection",
  "kind": "theorem",
  "name": "causal_disconnection",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 345,
  "source_line_end": 347,
  "registry_ids": [
    "V.T37"
  ],
  "related_registry_items": [
    {
      "id": "V.T37",
      "title": "Horizon as present-surface contraction",
      "url": "/registry/object/V.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L345-L347",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L345-L347",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L345-L347)
- Source range: L345-L347
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T37` — Horizon as present-surface contraction

## Immediate Comment / Docstring

```lean
/-- [V.T37] Causal disconnection at the τ-horizon: beyond the
    horizon radius, no null intertwiner escapes.

    The τ-horizon is causally disconnecting by construction:
    the NF iteration cannot extend null transport past the
    horizon boundary at the given depth. -/
```

## Source Excerpt

```lean
theorem causal_disconnection (h : TauHorizon) :
    h.causal_disconnect = true ∧ h.radius_numer > 0 :=
  ⟨h.causal_proof, h.radius_positive⟩
```
