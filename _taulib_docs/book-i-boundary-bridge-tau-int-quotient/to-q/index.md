---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInt.toQ",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-q/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauInt.toQ",
  "declaration_slug": "to-q",
  "kind": "def",
  "name": "TauInt.toQ",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 80,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L80-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L80-L84",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L80-L84)
- Source range: L80-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Canonical projection `TauInt → TauIntQ`. -/
```

## Source Excerpt

```lean
def TauInt.toQ (a : TauInt) : TauIntQ := Quotient.mk TauInt.setoid a

@[simp] theorem TauInt.toQ_eq_iff (a b : TauInt) :
    a.toQ = b.toQ ↔ TauInt.equiv a b :=
  Quotient.eq
```
