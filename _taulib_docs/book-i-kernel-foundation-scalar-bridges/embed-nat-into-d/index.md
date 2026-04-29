---
{
  "projection_kind": "taulib_declaration",
  "title": "embed_nat_into_d",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/embed-nat-into-d/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::embed_nat_into_d",
  "declaration_slug": "embed-nat-into-d",
  "kind": "def",
  "name": "embed_nat_into_d",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 113,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L113-L143",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L113-L143",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L113-L143)
- Source range: L113-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Canonical embedding ℕ → D** via Int.ofNat composition. -/
```

## Source Excerpt

```lean
def embed_nat_into_d (n : Nat) : SplitComplex :=
  embed_int_into_d (Int.ofNat n)

@[simp] theorem embed_nat_re (n : Nat) :
    (embed_nat_into_d n).re = (n : Int) := rfl

@[simp] theorem embed_nat_im (n : Nat) :
    (embed_nat_into_d n).im = 0 := rfl

-- ============================================================
-- PART 2: Round-trip witness — χ₊ ∘ embed = id
-- ============================================================

/-- **NNO-style witness for χ₊**: applying the B-sector character to
    an embedded scalar recovers the original integer.

    `chi_plus_val (embed_int n) = n + 0 = n`. -/
@[simp] theorem chi_plus_embed_int (n : Int) :
    chi_plus_val (embed_int_into_d n) = n := by
  unfold chi_plus_val embed_int_into_d; simp

/-- **NNO-style witness for χ₋**: applying the C-sector character to
    an embedded scalar also recovers the original integer.

    `chi_minus_val (embed_int n) = n - 0 = n`.

    Both characters give the same value on the embedded scalar
    because the embedding lands purely in the B-sector. -/
@[simp] theorem chi_minus_embed_int (n : Int) :
    chi_minus_val (embed_int_into_d n) = n := by
  unfold chi_minus_val embed_int_into_d; simp
```
