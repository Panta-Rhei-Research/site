---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.ringEquivRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/ring-equiv-rat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.ringEquivRat",
  "declaration_slug": "ring-equiv-rat",
  "kind": "def",
  "name": "TauRatQ.ringEquivRat",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 401,
  "source_line_end": 411,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L401-L411",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L401-L411",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L401-L411)
- Source range: L401-L411
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 40 keystone-of-keystones: `TauRatQ ≃+* ℚ` ring isomorphism**.

    Witnesses that our τ-native rational construction is isomorphic
    AS A FIELD to Mathlib's `Rat`. -/
```

## Source Excerpt

```lean
def TauRatQ.ringEquivRat : TauRatQ ≃+* ℚ where
  toFun := TauRatQ.toRat
  invFun := TauRatQ.ofRat
  left_inv := TauRatQ.toRat_ofRat
  right_inv := TauRatQ.ofRat_toRat
  map_add' x y := by
    show TauRatQ.toRat (x + y) = TauRatQ.toRat x + TauRatQ.toRat y
    exact TauRatQ.toRat_add x y
  map_mul' x y := by
    show TauRatQ.toRat (x * y) = TauRatQ.toRat x * TauRatQ.toRat y
    exact TauRatQ.toRat_mul x y
```
