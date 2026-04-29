---
{
  "projection_kind": "taulib_declaration",
  "title": "NativeHolography",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/native-holography/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::NativeHolography",
  "declaration_slug": "native-holography",
  "kind": "structure",
  "name": "NativeHolography",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 223,
  "source_line_end": 232,
  "registry_ids": [
    "V.T130"
  ],
  "related_registry_items": [
    {
      "id": "V.T130",
      "title": "Native holography",
      "url": "/registry/object/V.T130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L223-L232",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L223-L232",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L223-L232)
- Source range: L223-L232
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T130` — Native holography

## Immediate Comment / Docstring

```lean
/-- [V.T130] Native holography: H_partial[omega] encodes the
    complete E1 physics of tau^3 isomorphically.

    This is NOT AdS/CFT holography (which is a duality conjecture).
    It is a structural consequence of the Central Theorem (Book II):
    O(tau^3) = A_spec(L). The boundary L = S^1 v S^1 carries all
    physical information; the bulk tau^3 is reconstructed from it.

    Key difference from AdS/CFT:
    - AdS/CFT: conjectured duality, requires negative Lambda
    - tau: structural theorem, Lambda = 0, works in all signatures -/
```

## Source Excerpt

```lean
structure NativeHolography where
  /-- Encoding is isomorphic (not approximate). -/
  is_isomorphic : Bool := true
  /-- Does NOT require negative Lambda. -/
  requires_negative_lambda : Bool := false
  /-- Is a theorem, not a conjecture. -/
  is_theorem : Bool := true
  /-- Works in all signatures (not just AdS). -/
  all_signatures : Bool := true
  deriving Repr
```
