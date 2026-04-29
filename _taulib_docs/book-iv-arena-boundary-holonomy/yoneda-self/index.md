---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_self",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::yoneda_self",
  "declaration_slug": "yoneda-self",
  "kind": "def",
  "name": "yoneda_self",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 52,
  "source_line_end": 91,
  "registry_ids": [
    "IV.T96"
  ],
  "related_registry_items": [
    {
      "id": "IV.T96",
      "title": "Central Theorem --- physical form",
      "url": "/registry/object/IV.T96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L52-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L52-L91",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L52-L91)
- Source range: L52-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T96` — Central Theorem --- physical form

## Immediate Comment / Docstring

```lean
/-- Canonical Yoneda self-image. -/
```

## Source Excerpt

```lean
def yoneda_self : YonedaSelfImage where
  arena_dim := 5
  arena_eq := rfl
  complete := true
  complete_true := rfl

-- ============================================================
-- CENTRAL THEOREM — PHYSICAL FORM [IV.T96]
-- ============================================================

/- [IV.T96] Central Theorem (physical form): O(τ³) ≅ A_spec(L).

   The ring of holomorphic functions on τ³ equals the spectral
   algebra of the lemniscate boundary.

   RETIRED AS AN AXIOM (2026-04-19, peer-review-fixes-v1).
   Pre-publication simulated peer review identified the previously
   shipping declaration

     axiom central_theorem_physical : True

   as a null commitment: an axiom of type True is a no-op
   (True is inhabited by `trivial`), so the declaration added
   nothing to the theory while inflating the axiom count.

   The architectural intent — pointing the reader of
   BookIV.Arena at the mathematical Central Theorem proved in
   Book II — is now carried by this regular block comment and by
   the registry cross-reference [IV.T96] → II.T40. The finite
   verification lives in TauLib.BookII.CentralTheorem via
   `central_theorem_check` and `central_theorem_3_15` (closed by
   `native_decide`). No formal declaration is made here; the
   Book II content is not re-proved in Book IV.

   Note on Lean 4 comment syntax: this is a /- ... -/ block comment
   (no attachment to any declaration), not a /-- ... -/ docstring
   (which would need a following declaration to attach to). The
   earlier peer-review-fixes-v1 commit cc9c20c accidentally used a
   docstring here, which was fixed in a follow-up commit after CI
   flagged the orphaned-docstring parse error. -/
```
