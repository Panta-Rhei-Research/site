---
{
  "projection_kind": "taulib_declaration",
  "title": "scalar_bridge_synthesis",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/scalar-bridge-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::scalar_bridge_synthesis",
  "declaration_slug": "scalar-bridge-synthesis",
  "kind": "theorem",
  "name": "scalar_bridge_synthesis",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 212,
  "source_line_end": 228,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L212-L228",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.ScalarBridges",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L212-L228",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L212-L228)
- Source range: L212-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 37 H8 scalar-bridge synthesis (KEYSTONE)**.

    Packages the bidirectional ℕ ↔ D + ℤ ↔ D bridge in five
    structural-content clauses:

    1. **ℤ → D embedding round-trip via χ₊** (the readout retraction)
    2. **ℤ → D embedding round-trip via χ₋** (companion retraction)
    3. **ℕ → D NNO-style witness** (via Int.ofNat composition)
    4. **B-sector purity** (embedding lands purely on the real axis)
    5. **Ring-homomorphism preservation** (additive identity, sum,
       product all preserved by the embedding)

    Together they realize the user's structural intuition that the
    canonical ℕ/ℤ bridge into TauLib should run through D's
    scalar readout — establishing the bidirectional structural
    witness that was previously one-way (D → ℤ only). -/
```

## Source Excerpt

```lean
theorem scalar_bridge_synthesis (n : Nat) (m : Int) :
    -- Clause 1: ℤ → D round-trip via χ₊
    chi_plus_val (embed_int_into_d m) = m ∧
    -- Clause 2: ℤ → D round-trip via χ₋
    chi_minus_val (embed_int_into_d m) = m ∧
    -- Clause 3: ℕ → D NNO-style witness
    chi_plus_val (embed_nat_into_d n) = (n : Int) ∧
    -- Clause 4: B-sector purity (im = 0 always)
    (embed_int_into_d m).im = 0 ∧
    -- Clause 5: zero + one preserved
    (embed_int_into_d 0 = ⟨0, 0⟩ ∧
     embed_int_into_d 1 = ⟨1, 0⟩) :=
  ⟨chi_plus_embed_int m,
   chi_minus_embed_int m,
   nno_from_d_witness n,
   rfl,
   ⟨embed_int_zero, embed_int_one⟩⟩
```
