---
{
  "projection_kind": "taulib_declaration",
  "title": "Formula.tier",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/tier/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::Formula.tier",
  "declaration_slug": "tier",
  "kind": "def",
  "name": "Formula.tier",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 179,
  "source_line_end": 196,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L179-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L179-L196",
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

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L179-L196)
- Source range: L179-L196
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Each connective's tier (multiplicative or additive). -/
```

## Source Excerpt

```lean
def Formula.tier : Formula → Option ConnectiveTier
  | .atom _      => none
  | .tensor _ _  => some .multiplicative
  | .par    _ _  => some .multiplicative
  | .wth    _ _  => some .additive
  | .plus   _ _  => some .additive

@[simp] theorem tensor_is_multiplicative (a b : Formula) :
    (Formula.tensor a b).tier = some .multiplicative := rfl

@[simp] theorem par_is_multiplicative (a b : Formula) :
    (Formula.par a b).tier = some .multiplicative := rfl

@[simp] theorem wth_is_additive (a b : Formula) :
    (Formula.wth a b).tier = some .additive := rfl

@[simp] theorem plus_is_additive (a b : Formula) :
    (Formula.plus a b).tier = some .additive := rfl
```
