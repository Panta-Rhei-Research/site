---
{
  "projection_kind": "taulib_declaration",
  "title": "TauIntQ.ringEquivInt",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/ring-equiv-int/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauIntQ.ringEquivInt",
  "declaration_slug": "ring-equiv-int",
  "kind": "def",
  "name": "TauIntQ.ringEquivInt",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 305,
  "source_line_end": 315,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L305-L315",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L305-L315",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L305-L315)
- Source range: L305-L315
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 39 keystone-of-keystones: `TauIntQ ≃+* ℤ` ring isomorphism**.

    This is the formal statement that our τ-native integer construction
    is **isomorphic as a ring** to Mathlib's `Int`. Every ring property
    transfers cleanly between the two via this isomorphism. -/
```

## Source Excerpt

```lean
def TauIntQ.ringEquivInt : TauIntQ ≃+* ℤ where
  toFun := TauIntQ.toInt
  invFun := TauIntQ.ofInt
  left_inv := TauIntQ.toInt_ofInt
  right_inv := TauIntQ.ofInt_toInt
  map_add' x y := by
    show TauIntQ.toInt (x + y) = TauIntQ.toInt x + TauIntQ.toInt y
    exact TauIntQ.toInt_add x y
  map_mul' x y := by
    show TauIntQ.toInt (x * y) = TauIntQ.toInt x * TauIntQ.toInt y
    exact TauIntQ.toInt_mul x y
```
