---
{
  "projection_kind": "taulib_declaration",
  "title": "liarTemplate",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-template/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::liarTemplate",
  "declaration_slug": "liar-template",
  "kind": "def",
  "name": "liarTemplate",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 205,
  "source_line_end": 205,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L205-L205",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L205-L205",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L205-L205)
- Source range: L205-L205
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **Liar template** `Φ_Liar(p) = σ(p)`: the propositional
    template that identifies a proposition with its own negation
    (Belnap–Dunn paraconsistent ¬ on B_σ). -/
```

## Source Excerpt

```lean
def liarTemplate : Truth4 → Truth4 := sigmaSwap
```
