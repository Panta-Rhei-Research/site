---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_tauint_mathlib_bridge_synthesis",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/h8-tauint-mathlib-bridge-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::h8_tauint_mathlib_bridge_synthesis",
  "declaration_slug": "h8-tauint-mathlib-bridge-synthesis",
  "kind": "theorem",
  "name": "h8_tauint_mathlib_bridge_synthesis",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 335,
  "source_line_end": 352,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L335-L352",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L335-L352",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L335-L352)
- Source range: L335-L352
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 39 H8 Mathlib-Ring-Bridge synthesis (KEYSTONE)**.

    Packages the structural significance of the τ-native integer
    construction satisfying classical ring axioms:

    1. **TauIntQ is a `CommRing`**: full Mathlib typeclass instance
    2. **TauIntQ ≃+* ℤ**: ring isomorphism to Mathlib's `Int`
    3. **toInt homomorphism**: respects +, *, neg, 0, 1
    4. **Round-trip**: `ofInt ∘ toInt = id` and `toInt ∘ ofInt = id`

    Together these establish that the τ-native integer construction
    (formal differences over TauIdx, with explicit equiv quotient) is
    a **bridge into Mathlib's algebraic ecosystem** — every Mathlib
    theorem about CommRings now automatically applies to TauIntQ. -/
```

## Source Excerpt

```lean
theorem h8_tauint_mathlib_bridge_synthesis :
    -- Clause 1: ring isomorphism to ℤ exists
    Nonempty (TauIntQ ≃+* ℤ) ∧
    -- Clause 2: toInt preserves addition
    (∀ x y : TauIntQ, (x + y).toInt = x.toInt + y.toInt) ∧
    -- Clause 3: toInt preserves multiplication
    (∀ x y : TauIntQ, (x * y).toInt = x.toInt * y.toInt) ∧
    -- Clause 4: toInt preserves zero and one
    (TauIntQ.zero.toInt = 0 ∧ TauIntQ.one.toInt = 1) ∧
    -- Clause 5: round-trip
    (∀ n : Int, (TauIntQ.ofInt n).toInt = n) :=
  ⟨⟨TauIntQ.ringEquivInt⟩,
   TauIntQ.toInt_add,
   TauIntQ.toInt_mul,
   ⟨TauIntQ.toInt_zero, TauIntQ.toInt_one⟩,
   TauIntQ.ofInt_toInt⟩

end Tau.Boundary
```
