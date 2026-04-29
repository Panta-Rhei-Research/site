---
{
  "projection_kind": "taulib_declaration",
  "title": "Generator.toNat",
  "permalink": "/verify/taulib/docs/book-i-kernel-signature/to-nat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Signature`.",
  "declaration_id": "TauLib.BookI.Kernel.Signature::Generator.toNat",
  "declaration_slug": "to-nat",
  "kind": "def",
  "name": "Generator.toNat",
  "module_name": "TauLib.BookI.Kernel.Signature",
  "module_url": "/verify/taulib/docs/book-i-kernel-signature/",
  "source_line_start": 78,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L78-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Signature",
        "url": "/verify/taulib/docs/book-i-kernel-signature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L78-L91",
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

- Module: [TauLib.BookI.Kernel.Signature](/verify/taulib/docs/book-i-kernel-signature/)
- Source path: [`TauLib/BookI/Kernel/Signature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L78-L91)
- Source range: L78-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Canonical ordering index for generators: α=0, π=1, γ=2, η=3, ω=4. -/
```

## Source Excerpt

```lean
def Generator.toNat : Generator → Nat
  | alpha => 0
  | pi    => 1
  | gamma => 2
  | eta   => 3
  | omega => 4

/-- [I.K1 prerequisite] Strict ordering on generators derived from their indices. -/
instance : LT Generator where
  lt a b := a.toNat < b.toNat

/-- The ordering on generators is decidable. -/
instance (a b : Generator) : Decidable (a < b) :=
  inferInstanceAs (Decidable (a.toNat < b.toNat))
```
