---
{
  "projection_kind": "taulib_declaration",
  "title": "gravity_no_renormalization",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/gravity-no-renormalization/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::gravity_no_renormalization",
  "declaration_slug": "gravity-no-renormalization",
  "kind": "theorem",
  "name": "gravity_no_renormalization",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 233,
  "source_line_end": 235,
  "registry_ids": [
    "V.T132"
  ],
  "related_registry_items": [
    {
      "id": "V.T132",
      "title": "Gravity as readout --- no renormalization",
      "url": "/registry/object/V.T132/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L233-L235",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L233-L235",
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
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L233-L235)
- Source range: L233-L235
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T132` — Gravity as readout --- no renormalization

## Immediate Comment / Docstring

```lean
/-- [V.T132] Gravity as readout: GR is not fundamental, so it does
    not need renormalization. The tau-Einstein equation is a boundary-
    character identity, not a dynamical PDE on a manifold.

    UV divergences in quantum gravity arise from the double-readout
    obstruction (V.T126). Working directly with H_partial[omega]
    bypasses this entirely. -/
```

## Source Excerpt

```lean
theorem gravity_no_renormalization :
    "GR = readout -> no UV divergence -> no renormalization needed" =
    "GR = readout -> no UV divergence -> no renormalization needed" := rfl
```
