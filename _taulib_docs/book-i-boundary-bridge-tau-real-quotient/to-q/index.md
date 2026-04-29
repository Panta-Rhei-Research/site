---
{
  "projection_kind": "taulib_declaration",
  "title": "CauchyTauReal.toQ",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/to-q/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealQuotient::CauchyTauReal.toQ",
  "declaration_slug": "to-q",
  "kind": "def",
  "name": "CauchyTauReal.toQ",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "source_line_start": 133,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L133-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L133-L138",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L133-L138)
- Source range: L133-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def CauchyTauReal.toQ (a : CauchyTauReal) : TauRealQ :=
  Quotient.mk CauchyTauReal.setoid a

@[simp] theorem CauchyTauReal.toQ_eq_iff (a b : CauchyTauReal) :
    a.toQ = b.toQ ↔ CauchyTauReal.equiv a b :=
  Quotient.eq
```
