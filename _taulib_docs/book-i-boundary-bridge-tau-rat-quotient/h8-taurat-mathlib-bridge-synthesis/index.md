---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_taurat_mathlib_bridge_synthesis",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/h8-taurat-mathlib-bridge-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::h8_taurat_mathlib_bridge_synthesis",
  "declaration_slug": "h8-taurat-mathlib-bridge-synthesis",
  "kind": "theorem",
  "name": "h8_taurat_mathlib_bridge_synthesis",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 426,
  "source_line_end": 443,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L426-L443",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L426-L443",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L426-L443)
- Source range: L426-L443
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 40 H8 Mathlib-Field-Bridge synthesis (KEYSTONE)**.

    Five-clause structural significance:

    1. **TauRatQ is a `Field`**: full Mathlib typeclass instance
    2. **TauRatQ ≃+* ℚ**: ring isomorphism to Mathlib's `Rat`
    3. **toRat homomorphism**: respects +, *, neg, inv, 0, 1
    4. **Round-trip**: `ofRat ∘ toRat = id` and `toRat ∘ ofRat = id`
    5. **Inverse for nonzero**: `q ≠ 0 → q * inv q = 1` -/
```

## Source Excerpt

```lean
theorem h8_taurat_mathlib_bridge_synthesis :
    -- Clause 1: ring isomorphism to ℚ exists
    Nonempty (TauRatQ ≃+* ℚ) ∧
    -- Clause 2: toRat preserves addition
    (∀ x y : TauRatQ, (x + y).toRat = x.toRat + y.toRat) ∧
    -- Clause 3: toRat preserves multiplication
    (∀ x y : TauRatQ, (x * y).toRat = x.toRat * y.toRat) ∧
    -- Clause 4: toRat preserves zero, one
    (TauRatQ.zero.toRat = 0 ∧ TauRatQ.one.toRat = 1) ∧
    -- Clause 5: round-trip
    (∀ q : Rat, (TauRatQ.ofRat q).toRat = q) :=
  ⟨⟨TauRatQ.ringEquivRat⟩,
   TauRatQ.toRat_add,
   TauRatQ.toRat_mul,
   ⟨TauRatQ.toRat_zero, TauRatQ.toRat_one⟩,
   TauRatQ.ofRat_toRat⟩

end Tau.Boundary
```
