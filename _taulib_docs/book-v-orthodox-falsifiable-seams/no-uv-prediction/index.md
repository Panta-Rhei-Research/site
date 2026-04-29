---
{
  "projection_kind": "taulib_declaration",
  "title": "no_uv_prediction",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/no-uv-prediction/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::no_uv_prediction",
  "declaration_slug": "no-uv-prediction",
  "kind": "def",
  "name": "no_uv_prediction",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 138,
  "source_line_end": 143,
  "registry_ids": [
    "V.T137"
  ],
  "related_registry_items": [
    {
      "id": "V.T137",
      "title": "No UV divergences in tau",
      "url": "/registry/object/V.T137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L138-L143",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.FalsifiableSeams",
        "url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L138-L143",
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

- Module: [TauLib.BookV.Orthodox.FalsifiableSeams](/verify/taulib/docs/book-v-orthodox-falsifiable-seams/)
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L138-L143)
- Source range: L138-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T137` — No UV divergences in tau

## Immediate Comment / Docstring

```lean
/-- [V.T137] No UV divergences: every spectral sum converges.

    For any sector X and depth N:
      sum_{n=1}^{N} ||chi_X(alpha_n)||^2 <= kappa(X)^2 * N

    The bound is linear in N, not divergent. Physical predictions
    are finite at every order. -/
```

## Source Excerpt

```lean
def no_uv_prediction : FalsifiablePrediction where
  name := "No UV divergences"
  prediction := "All spectral sums converge; finite at every order"
  falsifier := "Confirmed QED discrepancy beyond uncertainty budget"
  strength := .Strong
  registry_id := "V.T137"
```
